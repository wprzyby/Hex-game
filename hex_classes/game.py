from typing import List, Optional, Tuple
from hex_classes.player import HexPlayer
from hex_classes.state import HexState
from hex_classes.errors import IdenticalPlayerNamesError, InvalidMoveError


class HexGame:
    """
    Game interface to interact with through which game's state changes

    Attributes
    --------
    first_player: HexPlayer
        player to move first as HexPlayer object
    second_player: HexPlayer
        player to move second as HexPlayer object
    _state: HexState
        current state of the game

    Methods
    --------
    game_board()
        returns current state's game board
    current_player()
        returns current player as HexPlayer object
    is_finished()
        returns whether the game has finished
    board_size()
        returns the length of the game board's side
    get_moves()
        returns possible moves to make in current state as list of coords
    get_winner()
        returns the winner of the game as HexPlayer object
    make_move(move_coords)
        assigns new game state after making a move
    """
    def __init__(self, board_radius: int,
                 first_player_name: str = None,
                 second_player_name: str = None):
        """
        Parameters
        --------
        board_radius: int
            distance from board's center to the sides; defaults to None
        first_player_name: str, optional
            name of player to move first; defaults to None
        second_player_name: str, optional
            name of player to move second; defaults to None
        """
        if not first_player_name:
            first_player_name = 'Player 1'
        if not second_player_name:
            second_player_name = 'Player 2'
        if first_player_name == second_player_name:
            raise IdenticalPlayerNamesError("Player names must be unique")
        self.first_player = HexPlayer(first_player_name, started_first=True)
        self.second_player = HexPlayer(second_player_name, started_first=False)

        state = HexState(self.first_player, self.second_player, board_radius)
        self._state = state

    def game_board(self) -> List[List[Optional[str]]]:
        return self._state.game_board()

    def current_player(self) -> HexPlayer:
        return self._state.current_player()

    def is_finished(self) -> bool:
        return self._state.is_finished()

    def board_size(self) -> int:
        return self._state.board_size()

    def get_moves(self) -> List[Tuple[int, int]]:
        return self._state.get_moves()

    def get_winner(self) -> Optional[HexPlayer]:
        return self._state.get_winner()

    def make_move(self, move_coords: Tuple[int, int]) -> None:
        """
        makes move and sets the new state after the move has
        been made as current game state

        Parameters
        --------
        move_coords: Tuple[int, int]
            coordinates of the move to make
        """
        if move_coords not in self.get_moves():
            raise InvalidMoveError("Move outside of scope or illegal")
        self._state = self._state.make_move(move_coords)

    def __str__(self) -> str:
        return str(self._state)
