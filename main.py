from ui_files.ui_hex import Ui_mainWindow
from PySide2.QtWidgets import QApplication, QGraphicsScene, QMainWindow

from PySide2.QtGui import QBrush, QPen, QPainter
from PySide2.QtCore import Qt, QLineF

import sys
import math

from hex_classes.errors import IdenticalPlayerNamesError, InvalidMoveError
from hex_classes.game import HexGame
from gui_classes import HexagonItem, ErrorDialog, InteractiveGraphicsScene


class HexWindow(QMainWindow):
    """
    window for Hex game, includes setup phase for input of game properties,
    creation of the grid to play on and making moves on Game object based on
    user input

    Attributes
    --------
    ui: Ui_mainWindow
        object generated through qt-designer, contains graphics views, buttons,
        text labels, etc.
    _current_player_color_scene: QGraphicsScene
        scene containing the tile color of current player
    _game: HexGame
        HexGame object representing the game being played through this window
    _hex_grid_scene: InteractiveGraphicsScene
        graphics scene on which the hex grid is painted
    _hex_grid: List[List[Optional[HexagonItem]]]
        a list of columns of hexagon items in the grid

    Methods
    --------
    _show_game_setup()
        sets the window to show the setup screen
    _initialize_game()
        creates HexGame object based on input, sets it as _game attribute,
        sets the window to show the game screen
    _setup_hex_grid()
        sets up the game screen, creates hex grid, paints it on a scene
    _hexagon_clicked()
        handles doubleclick of hex tile, makes move or shows error dialog
    _update_hex_grid()
        colors hex tiles, updates information on the game screen
    _setup_rematch()
        sets up a rematch game with players reversed and same board radius
    _show_error_dialog(dialog_message)
        shows simple error dialog with given error message
    _create_hex_grid_outline()
        paints outline of the borders of the hex grid with players' colors
    _finish()
        closes the window
    """
    def __init__(self, parent=None):
        """
        sets up UI, sets scenes for permanent graphics views
        and sets effects of clicking of permanent buttons, shows setup screen
        """
        super().__init__(parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        self.ui.hexBoard.setRenderHint(QPainter.Antialiasing)
        self._current_player_color_scene = QGraphicsScene()
        self.ui.currentPlayerColor.setScene(self._current_player_color_scene)

        red_scene = QGraphicsScene()
        red_scene.setBackgroundBrush(QBrush(Qt.red))
        self.ui.playerOneColor.setScene(red_scene)
        blue_scene = QGraphicsScene()
        blue_scene.setBackgroundBrush(QBrush(Qt.blue))
        self.ui.playerTwoColor.setScene(blue_scene)

        self.ui.rematchButton.clicked.connect(self._setup_rematch)
        self.ui.restartButton.clicked.connect(self._show_game_setup)
        self.ui.exitButton.clicked.connect(self._finish)
        self.ui.setupConfirmButton.clicked.connect(self._initialize_game)

        self._show_game_setup()

    def _show_game_setup(self):
        """
        sets the window to show game setup screen, clears input lines
        """
        self.ui.stack.setCurrentIndex(0)
        self.ui.playerOneInputLine.setText("")
        self.ui.playerTwoInputLine.setText("")

    def _initialize_game(self, player_one_name: str = None,
                         player_two_name: str = None,
                         board_radius: int = None) -> None:
        """
        creates HexGame object based on setup screen input or based on
        attributes if provided, sets the window to show the game screen
        and runs hex grid setup

        Parameters
        --------
            player_one_name: str, optional
                name of player to move first
            player_two_name: str, optional
                name of player to move second
            board_radius: int, optional
                HexGame board radius
        """
        if not (player_one_name and player_two_name and board_radius):
            player_one_name = self.ui.playerOneInputLine.text()
            player_two_name = self.ui.playerTwoInputLine.text()
            board_radius = self.ui.boardRadiusInput.value()
        try:
            self._game = HexGame(board_radius,
                                 player_one_name, player_two_name)
            self.ui.stack.setCurrentIndex(1)
            self._setup_hex_grid()
        except IdenticalPlayerNamesError:
            message = "Player names are identical. Please set unique player names."
            self._show_error_dialog(message)

    def _setup_hex_grid(self) -> None:
        """
        sets up game screen by creating the hex grid, painting it on a scene
        and setting button and information visibility, runs hex grid outline
        creation and hex grid update
        """
        self._hex_grid_scene = InteractiveGraphicsScene()
        self.ui.hexBoard.setScene(self._hex_grid_scene)
        self._hex_grid_scene.itemDoubleClicked.connect(self._hexagon_clicked)

        self.ui.currentPlayer.setVisible(True)
        self.ui.currentPlayerColor.setVisible(True)
        self.ui.rematchButton.setEnabled(False)
        self.ui.rematchButton.setVisible(False)
        self.ui.winnerPrompt.setText("")

        size = self._game.board_size()
        # length of one side of hexagon inversely proportional to board size
        len = 270 / size
        scene = self._hex_grid_scene
        self._hex_grid = [[HexagonItem((x, y), len, scene) for y in range(size)]
                          for x in range(size)]

        self._create_hex_grid_outline()
        self._update_hex_grid()

    def _hexagon_clicked(self, item: HexagonItem) -> None:
        """
        makes move for current player on selected hex tile if possible
        and updates grid, otherwise shows error dialog; idle if game is over
        """
        if not self._game.is_finished():
            try:
                self._game.make_move(item.coords())
                self._update_hex_grid()
            except InvalidMoveError:
                error_message = "Invalid move! Select non-occupied tile."
                self._show_error_dialog(error_message)

    def _update_hex_grid(self) -> None:
        """
        sets game screen information text and player color based on state
        of the game, paints hex tiles according to which player they
        belong to, checks for end of game, changes info accordingly
        """
        current_player = self._game.current_player()
        self.ui.currentPlayer.setText(f"Current player: {current_player}")
        color = Qt.red if current_player.started_first else Qt.blue
        self._current_player_color_scene.setBackgroundBrush(QBrush(color))

        game_board_data = self._game._state.game_board()
        for x_coord, column in enumerate(self._hex_grid):
            for y_coord, hexagon in enumerate(column):
                player_char = game_board_data[x_coord][y_coord]
                if player_char:
                    color = Qt.red if player_char == '1' else Qt.blue
                    hexagon.setBrush(QBrush(color))
                else:
                    hexagon.setBrush(QBrush(Qt.NoBrush))

        if self._game.is_finished():
            winner = str(self._game.get_winner())
            self.ui.winnerPrompt.setText(f"GAME OVER! {winner} has won!")
            self.ui.currentPlayer.setText("")
            color = Qt.black
            self._current_player_color_scene.setBackgroundBrush(QBrush(color))
            self.ui.rematchButton.setVisible(True)
            self.ui.rematchButton.setEnabled(True)

    def _setup_rematch(self) -> None:
        """
        runs game initialization with player names reversed and same
        board radius so that setup screen can be skipped for quick rematch
        """
        player_one_name = self._game.second_player.name
        player_two_name = self._game.first_player.name
        board_radius = int((self._game.board_size() - 1) / 2)
        self._initialize_game(player_one_name, player_two_name,
                              board_radius)

    def _show_error_dialog(self, dialog_message: str) -> None:
        """
        displays simple error message dialog with given message

        Parameters
        --------
        dialog_message: str
            text message to be shown in dialog's body
        """
        dialog = ErrorDialog(self)
        dialog.set_error_message(dialog_message)
        dialog.exec_()

    def _create_hex_grid_outline(self) -> None:
        """
        draws an outline around the hex grid border, opposite
        sides are painted with the color that represents a player
        who needs to connect them to win
        """
        board_size = self._game.board_size()

        # gets single hex tile measurements
        side_len = self._hex_grid[0][0].side_len
        width = self._hex_grid[0][0].pen_width

        red_pen = QPen(Qt.red, width, c=Qt.RoundCap)
        blue_pen = QPen(Qt.blue, width, c=Qt.RoundCap)

        # x_mas is the x coordinate of the right-most node
        x_max = (board_size * 3 * side_len) - side_len

        # size of separation of the outline from the grid
        separation = width / 2
        sqrt3 = math.sqrt(3)

        for tile_nr in range(board_size):
            # (x1, y1) -> (x2, y2) - line outlining the first side of hex tile
            # (x2, y2) -> (x3, y3) - analogically
            # calculations stem from the nature of a regular hexagon
            x1 = -(width * sqrt3 / 3) + (1.5 * side_len * tile_nr) - separation
            y1 = width + ((side_len * sqrt3 * 0.5) * tile_nr) + (separation * sqrt3)
            x2 = x1 + (side_len / 2)
            y2 = y1 + (side_len * sqrt3 * 0.5)
            x3 = x2 + side_len
            y3 = y2

            # outlines lower left border's tile
            first_line = QLineF(x1, y1, x2, y2)
            second_line = QLineF(x2, y2, x3, y2)
            self._hex_grid_scene.addLine(first_line, blue_pen)
            self._hex_grid_scene.addLine(second_line, blue_pen)

            # outlines upper left border's tile
            first_line = QLineF(x1, -y1, x2, -y2)
            second_line = QLineF(x2, -y2, x3, -y3)
            self._hex_grid_scene.addLine(first_line, red_pen)
            self._hex_grid_scene.addLine(second_line, red_pen)

            # outlines upper right border's tile
            first_line = QLineF(x_max - x1, -y1, x_max - x2, -y2)
            second_line = QLineF(x_max - x2, -y2, x_max - x3, -y3)
            self._hex_grid_scene.addLine(first_line, blue_pen)
            self._hex_grid_scene.addLine(second_line, blue_pen)

            # outlines lower right border's tile
            first_line = QLineF(x_max - x1, y1, x_max - x2, y2)
            second_line = QLineF(x_max - x2, y2, x_max - x3, y3)
            self._hex_grid_scene.addLine(first_line, red_pen)
            self._hex_grid_scene.addLine(second_line, red_pen)

    def _finish(self) -> None:
        self.close()


def guiMain(args):
    """
    runs the game
    """
    app = QApplication([])
    window = HexWindow()
    window.show()
    return app.exec_()


if __name__ == '__main__':
    guiMain(sys.argv)
