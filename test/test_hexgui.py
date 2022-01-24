from main import HexWindow
from hex_classes.game import HexGame
from PySide2.QtGui import QBrush
from PySide2.QtCore import Qt
import PySide2.QtCore as QtCore


def test_setup_screen(qtbot):
    window = HexWindow()
    qtbot.mouseClick(window.ui.setupConfirmButton, QtCore.Qt.LeftButton)
    assert isinstance(window._game, HexGame)
    assert window._game.first_player.name == 'Player 1'
    assert window._game.second_player.name == 'Player 2'
    assert window._game.current_player().name == 'Player 1'
    assert len(window._game.game_board()) == 3
    assert len(window._hex_grid) == 3


def test_setup_screen_enter_name(qtbot):
    window = HexWindow()
    window.ui.playerOneInputLine.setText("P1")
    window.ui.playerTwoInputLine.setText("P2")
    window.ui.boardRadiusInput.setValue(3)
    qtbot.mouseClick(window.ui.setupConfirmButton, QtCore.Qt.LeftButton)
    assert window._game.first_player.name == 'P1'
    assert window._game.second_player.name == 'P2'
    assert window._game.current_player().name == 'P1'
    assert len(window._game.game_board()) == 7
    assert len(window._hex_grid) == 7


def test_game_screen_make_move(qtbot):
    window = HexWindow()
    qtbot.mouseClick(window.ui.setupConfirmButton, QtCore.Qt.LeftButton)
    assert window._current_player_color_scene.backgroundBrush() == QBrush(Qt.red)
    assert window.ui.currentPlayer.text() == 'Current player: Player 1'

    window._hexagon_clicked(window._hex_grid[0][0])
    assert window._game.game_board()[0][0] == '1'
    assert window._game.current_player().name == 'Player 2'
    assert window._current_player_color_scene.backgroundBrush() == QBrush(Qt.blue)
    assert window.ui.currentPlayer.text() == 'Current player: Player 2'
    assert window._hex_grid[0][0].brush() == QBrush(Qt.red)

    window._hexagon_clicked(window._hex_grid[0][1])
    assert window._game.game_board()[0][1] == '2'
    assert window._game.current_player().name == 'Player 1'
    assert window._current_player_color_scene.backgroundBrush() == QBrush(Qt.red)
    assert window.ui.currentPlayer.text() == 'Current player: Player 1'
    assert window._hex_grid[0][1].brush() == QBrush(Qt.blue)


def test_game_screen_make_moves_to_win(qtbot):
    window = HexWindow()
    qtbot.mouseClick(window.ui.setupConfirmButton, QtCore.Qt.LeftButton)
    window._hexagon_clicked(window._hex_grid[0][0])
    window._hexagon_clicked(window._hex_grid[0][1])
    window._hexagon_clicked(window._hex_grid[1][0])
    window._hexagon_clicked(window._hex_grid[0][2])
    assert window._game.is_finished() is False
    assert window._game.get_winner() is None
    assert window.ui.winnerPrompt.text() == ''

    window._hexagon_clicked(window._hex_grid[2][0])
    assert window._game.is_finished() is True
    assert window._game.get_winner().name == 'Player 1'
    assert window.ui.winnerPrompt.text() == 'GAME OVER! Player 1 has won!'


def test_restart(qtbot):
    window = HexWindow()
    qtbot.mouseClick(window.ui.setupConfirmButton, QtCore.Qt.LeftButton)
    window._hexagon_clicked(window._hex_grid[0][0])
    assert window._game.game_board()[0][0] == '1'
    assert window._hex_grid[0][0].brush() == QBrush(Qt.red)

    qtbot.mouseClick(window.ui.restartButton, QtCore.Qt.LeftButton)
    qtbot.mouseClick(window.ui.setupConfirmButton, QtCore.Qt.LeftButton)
    assert window.ui.currentPlayer.text() == 'Current player: Player 1'
    assert window._game.game_board()[0][0] is None
    assert window._hex_grid[0][0].brush() == QBrush(Qt.NoBrush)


def test_game_screen_rematch(qtbot):
    window = HexWindow()
    qtbot.mouseClick(window.ui.setupConfirmButton, QtCore.Qt.LeftButton)
    window._hexagon_clicked(window._hex_grid[0][0])
    window._hexagon_clicked(window._hex_grid[0][1])
    window._hexagon_clicked(window._hex_grid[1][0])
    window._hexagon_clicked(window._hex_grid[0][2])
    window._hexagon_clicked(window._hex_grid[2][0])
    qtbot.mouseClick(window.ui.rematchButton, QtCore.Qt.LeftButton)
    assert window._game.current_player().name == 'Player 2'
    assert window._game.current_player().started_first is True
    assert len(window._hex_grid) == 3
    assert window._game.game_board()[0][0] is None
    assert window._hex_grid[0][0].brush() == QBrush(Qt.NoBrush)
    assert window.ui.winnerPrompt.text() == ''
