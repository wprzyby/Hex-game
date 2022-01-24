from typing import Optional, List, Tuple, Set
from hex_classes.errors import StateDataMissingError
from hex_classes.player import HexPlayer


class HexState:
    """
    Represents state of hex game, contains the game board
    as a list, defines making a move on the board.

    Attributes
    ----------
    _game_board: List[List[Optional[str]]]
        lists within list representation of hex tiles
    _current_player: HexPlayer
        player to move as HexPlayer object
    _other_player: HexPlayer
        player waiting for their move as HexPlayer object
    _board_size: int
        length of game board's side (in number of hex tiles)
    _is_finished: bool
        whether the game has finished or not

    Methods
    --------
    game_board()
        _game_board attribute getter
    current_player()
        _current_player attribute getter
    is_finished()
        _is_finished attribute getter
    board_size()
        _board_size attribute getter
    get_moves()
        returns possible moves
    get_winner()
        returns player who won the game as HexPlayer object or None
    get_neighbors(hex_coords)
        returns list of hex tiles neighboring given tile
    make_move(move_coords)
        returns new state after given move is made, checks if game has been won
    update_connections(move_coords)
        updates current player's sets of connected tiles after move is made
    check_for_win(connection)
        checks connected tiles set for possible game winning connection
    """
    def __init__(self, current_player: HexPlayer, other_player: HexPlayer,
                 board_radius: int = None,
                 game_board: List[List[Optional[str]]] = None,
                 is_finished=False):
        """
        initializes state with given game board and players
        or creates empty game board based on given board radius

        Parameters
        --------
            current_player: HexPlayer
                player to move
            other_player: HexPlayer
                player waiting for their move
            board_radius: int, optional
                distance from board's center to the sides; defaults to None
            game_board: List[List[Optional[str]]], optional
                current game board's list representation; defaults to None
            is_finished: bool, optional
                whether the game has already finished; defaults to False

        Raises
        --------
            ValueError
                raised when parameter value is not valid
            StateDataMissingError
                raised when not enough data to initialize object
                (e.g. when no game board and no radius was entered)
        """

        if game_board:
            self._game_board = game_board
        elif board_radius is not None:
            if board_radius <= 0:
                raise ValueError("Board radius must be positive")
            size = (board_radius * 2) + 1
            self._game_board = [[None for _ in range(size)]
                                for _ in range(size)]
        else:
            raise StateDataMissingError("Could not initialize state object")

        self._current_player = current_player
        self._other_player = other_player
        self._board_size = len(self._game_board)
        self._is_finished = is_finished

    def game_board(self) -> List[List[Optional[str]]]:
        return self._game_board

    def current_player(self) -> HexPlayer:
        return self._current_player

    def is_finished(self) -> bool:
        return self._is_finished

    def board_size(self) -> int:
        return self._board_size

    def get_moves(self) -> List[Tuple[int, int]]:
        """
        creates a list of legal moves to make

        Returns
        --------
        List[Tuple[int, int]]
            list of possible move coordinates
        """
        possible_moves = list()
        for x in range(self._board_size):
            for y in range(self._board_size):
                if self._game_board[x][y] is None:
                    possible_moves.append((x, y))
        return possible_moves

    def get_winner(self) -> Optional[HexPlayer]:
        """
        returns player who won the game as HexPlayer object
        or None if winner is not yet determined

        Returns
        --------
        Player
            the player that won or None
        """
        if self._is_finished:
            if self._current_player.is_winner:
                return self._current_player
            else:
                return self._other_player
        return None

    def get_neighbors(self, hex_coords: Tuple) -> List[Tuple]:
        """
        determines neighboring hex tiles, returns them as list

        Parameters:
        --------
        hex_coords: Tuple
            coordinates of a hex tile

        Returns
        --------
        neighbors: List[tuple]
            list of coordinates of neighboring hex tiles
        """
        neighbors = list()
        x, y = hex_coords
        # neighbor coordinates stem from the character of hex tiles,
        # one has a maximum of 6 neighbors
        possible_neighbors = [(x, y - 1),
                              (x, y + 1),
                              (x - 1, y),
                              (x + 1, y),
                              (x + 1, y - 1),
                              (x - 1, y + 1)]
        for coords in possible_neighbors:
            if coords[0] in range(self.board_size()) \
               and coords[1] in range(self.board_size()):
                neighbors.append(coords)
        return neighbors

    def make_move(self, move_coords: Tuple[int, int]) -> 'HexState':
        """
        Creates a new state after making the move

        Parameters
        --------
        move_coords: Tuple[int, int]
            coordinates of the move to make as tuple

        Returns
        --------
        HexState
            Game state after the move
        """
        x, y = move_coords
        self._game_board[x][y] = self._current_player.char

        # updates player's connected tiles, checks the newest for win
        potential_win = self.update_connections(move_coords)
        if self.check_for_win(potential_win):
            self._is_finished = True
            self._current_player.is_winner = True

        # creates new state with updated game board and players
        board_radius = (self._board_size - 1) / 2
        return HexState(self._other_player, self._current_player,
                        board_radius, self._game_board, self._is_finished)

    def update_connections(self, move_coords: Tuple[int, int]) \
            -> Set[Tuple[int, int]]:
        """
        Updates current player's sets of connected tiles after moving

        If existing connections contain tiles neighboring move_coords,
        it combines those connections into one and adds move_coord to it.
        If not, it adds a new connection set containing only move_coords.

        Parameters
        --------
        move_coords: Tuple[int, int]
            coordinates of made move.

        Returns
        --------
        the connection set which has been updated/added
        """
        neighbor_hexes = self.get_neighbors(move_coords)
        temp_index_list = list()
        new_connection = set()

        if self._current_player.connections:
            # gets indexes of sets connected to given hex tile
            for idx, connection in enumerate(self._current_player.connections):
                for neighbor in neighbor_hexes:
                    if neighbor in connection and idx not in temp_index_list:
                        temp_index_list.append(idx)

        # merges connecting sets into one, adds new tile into it
        if temp_index_list:
            for idx in temp_index_list[::-1]:
                new_connection.update(self._current_player.connections.pop(idx))
        new_connection.add(move_coords)
        self._current_player.connections.append(new_connection)
        return new_connection

    def check_for_win(self, connection: set) -> bool:
        """
        checks connected tiles set for possible game winning connection
        by checking if the set has tiles from both opposite sides

        Parameters
        --------
        connection: set
            set of connected tiles' coordinates to check for win

        Returns
        --------
        bool
            whether the connection is a game-winning connection
        """
        # changes the set into list of all x_coord and list of all y_coords
        x_coords, y_coords = zip(*list(connection))
        if self._current_player.started_first:
            return 0 in x_coords and (self._board_size - 1) in x_coords
        else:
            return 0 in y_coords and (self._board_size - 1) in y_coords

    def __str__(self) -> str:
        """
        creates text representation of the game's state

        Returns
        --------
        str
            text representation of the game's state
        """
        if self.is_finished():
            text_repr = "Game over!\n"
        else:
            text_repr = f"Current player: {self._current_player.name}\n\n  "
        for number in range(self.board_size()):
            text_repr += f"{number}   "
        text_repr += "\n"
        for idx, column in enumerate(self._game_board):
            text_repr += f"{str(idx)}   "
            for element in column:
                if element is None:
                    text_repr += "o   "
                else:
                    text_repr += element
                    text_repr += "   "
            text_repr += "\n"
            text_repr += "  " * (idx + 1)
        return text_repr
