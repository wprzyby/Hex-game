from hex_classes.errors import IdenticalPlayerNamesError, InvalidMoveError
from hex_classes.game import HexGame
import pytest


def test_game_init():
    player_one_name = "Player 1"
    player_two_name = "Player 2"
    game = HexGame(6, player_one_name, player_two_name)
    assert game.board_size() == 13
    assert game.first_player.name == "Player 1"
    assert game.second_player.name == "Player 2"
    assert game.current_player().name == "Player 1"
    assert game.first_player.char == '1'
    assert game.second_player.char == '2'
    assert game.first_player.started_first is True
    assert game.second_player.started_first is False


def test_game_no_names():
    game = HexGame(6)
    assert game.board_size() == 13
    assert game.first_player.name == 'Player 1'
    assert game.second_player.name == 'Player 2'


def test_game_same_player_names():
    player_one_name = "Player 1"
    player_two_name = "Player 1"
    with pytest.raises(IdenticalPlayerNamesError):
        HexGame(6, player_one_name, player_two_name)


def test_game_invalid_radius():
    with pytest.raises(ValueError):
        HexGame(0)
    with pytest.raises(ValueError):
        HexGame(-1)


def test_game_make_move():
    game = HexGame(6)
    assert game.current_player().name == 'Player 1'
    game.make_move((0, 0))
    game_board = game.game_board()
    assert game.current_player().name == 'Player 2'
    assert game_board[0][0] == game.first_player.char


def test_game_make_move_tile_taken():
    game = HexGame(6)
    game.make_move((0, 0))
    with pytest.raises(InvalidMoveError):
        game.make_move((0, 0))
    assert game.current_player().name == 'Player 2'
    assert game.game_board()[0][0] == '1'


def test_game_make_move_outside_scope():
    game = HexGame(6)
    with pytest.raises(InvalidMoveError):
        game.make_move((0, 18))
    with pytest.raises(InvalidMoveError):
        game.make_move((-1, -1))


def test_game_make_move_make_connection():
    game = HexGame(6)
    game.make_move((0, 0))
    game.make_move((3, 3))
    game.make_move((1, 1))
    assert game.first_player.connections == [{(0, 0)}, {(1, 1)}]
    game.make_move((3, 4))
    game.make_move((1, 0))
    assert game.first_player.connections == [{(0, 0), (1, 0), (1, 1)}]


def test_game_no_win():
    game = HexGame(6)
    game.make_move((0, 0))
    game.make_move((1, 2))
    game.make_move((1, 0))
    game.make_move((2, 2))
    game.make_move((2, 0))
    assert game.is_finished() is False
    assert game.get_winner() is None


def test_game_win_first_player():
    game = HexGame(1)
    game.make_move((0, 0))
    game.make_move((1, 2))
    game.make_move((1, 0))
    game.make_move((2, 2))
    game.make_move((2, 0))
    assert game.is_finished() is True
    assert game.get_winner().name == 'Player 1'


def test_game_win_second_player():
    game = HexGame(1)
    game.make_move((1, 1))
    game.make_move((0, 2))
    game.make_move((2, 1))
    game.make_move((0, 1))
    game.make_move((2, 0))
    game.make_move((0, 0))
    assert game.is_finished() is True
    assert game.get_winner().name == 'Player 2'


def test_game_first_player_would_win_as_second():
    game = HexGame(1)
    game.make_move((0, 1))
    game.make_move((1, 0))
    game.make_move((0, 0))
    game.make_move((1, 1))
    game.make_move((0, 2))
    assert game.is_finished() is False
    assert game.get_winner() is None


def test_game_second_player_would_win_as_first():
    game = HexGame(1)
    game.make_move((0, 1))
    game.make_move((1, 0))
    game.make_move((1, 1))
    game.make_move((2, 0))
    game.make_move((0, 2))
    game.make_move((0, 0))
    assert game.is_finished() is False
    assert game.get_winner() is None


def test_game_moves_at_border_no_win():
    game = HexGame(1)
    game.make_move((0, 0))
    game.make_move((1, 2))
    game.make_move((1, 1))
    game.make_move((2, 1))
    game.make_move((2, 2))
    assert game.is_finished() is False
    assert game.get_winner() is None


def test_game_make_move_triple_connection():
    game = HexGame(2)
    game.make_move((1, 2))
    assert len(game.first_player.connections) == 1
    assert {(1, 2)} in game.first_player.connections
    game.make_move((3, 3))
    game.make_move((3, 1))
    assert len(game.first_player.connections) == 2
    assert {(3, 1)} in game.first_player.connections
    game.make_move((2, 1))
    game.make_move((2, 3))
    assert len(game.first_player.connections) == 3
    assert {(2, 3)} in game.first_player.connections
    game.make_move((0, 0))
    game.make_move((2, 2))
    connection = {(1, 2), (3, 1), (2, 3), (2, 2)}
    assert len(game.first_player.connections) == 1
    assert connection in game.first_player.connections


def test_game_win_through_connection():
    game = HexGame(1)
    game.make_move((0, 0))
    game.make_move((1, 2))
    game.make_move((2, 0))
    game.make_move((2, 2))
    game.make_move((1, 0))
    assert game.is_finished() is True
    assert game.get_winner().name == 'Player 1'


def test_game_win_with_invalid_move():
    game = HexGame(1)
    game.make_move((0, 0))
    game.make_move((1, 0))
    game.make_move((2, 0))
    game.make_move((2, 2))
    with pytest.raises(InvalidMoveError):
        game.make_move((1, 0))
    assert game.is_finished() is False
    assert game.get_winner() is None


def test_game_get_moves():
    game = HexGame(1)
    legal_moves = [(0, 0),
                   (0, 1),
                   (0, 2),
                   (1, 0),
                   (1, 1),
                   (1, 2),
                   (2, 0),
                   (2, 1),
                   (2, 2)]
    assert game.get_moves() == legal_moves
    game.make_move((0, 0))
    legal_moves = [(0, 1),
                   (0, 2),
                   (1, 0),
                   (1, 1),
                   (1, 2),
                   (2, 0),
                   (2, 1),
                   (2, 2)]
    assert game.get_moves() == legal_moves
