from PySide2.QtWidgets import QWidget, QGraphicsPolygonItem, QGraphicsScene, \
     QGraphicsView, QDialog
from PySide2.QtGui import QPolygonF, QPen
from PySide2.QtCore import QPointF, Qt, Signal
from ui_files.ui_error_dialog import Ui_errorDialog
from typing import Tuple
import math


class HexagonItem(QGraphicsPolygonItem):
    """
    represents a clickable regular hexagon tile item with transparent interior
    and white borders and a transform origin point at its center

    Attributes
    --------
    side_len: float
        length of one side of the hexagon
    pen_width: float
        width of pen used for painting sides of the hexagon
    _coords: Tuple[int, int]
        coordinates of the tile in the game board
        ((1, 2) is first row, second column)

    Methods
    --------
    mouseDoubleClickEvent()
        sets the double click to emit a signal
    hoverEnterEvent()
        sets mouse hover-over to enlarge the item slightly
    hoverLeaveEvent()
        sets the item to original size when mouse hover-over is over
    coords()
        _coords attribute getter
    """
    def __init__(self, coords: Tuple, side_len: float,
                 scene: QGraphicsScene, parent: QWidget = None):
        """
        creates the hexagon item, adds itself to a given scene

        Parameters
        --------
            coords: Tuple
                coordinates of the tile in the game board
            side_len: float
                length of one side of the hexagon
            scene: QGraphicsScene
                scene for the item to be added to
            parent: QWidget, optional
                widget parent; defaults to None
        """
        polygon = QPolygonF()
        self.side_len = side_len
        # pen width value proportional to side len, set experimentally
        self.pen_width = self.side_len / 9
        sqrt3 = math.sqrt(3)

        # adds nodes of the hexagon
        polygon.append(QPointF(0.0, 0.0))
        polygon.append(QPointF(side_len * 0.5, side_len * 0.5 * sqrt3))
        polygon.append(QPointF(3 * side_len * 0.5, side_len * 0.5 * sqrt3))
        polygon.append(QPointF(2 * side_len, 0))
        polygon.append(QPointF(1.5 * side_len, -side_len * 0.5 * sqrt3))
        polygon.append(QPointF(side_len * 0.5, -side_len * 0.5 * sqrt3))
        super().__init__(polygon, parent)

        self.setTransformOriginPoint(self.side_len, 0.0)
        self.setPen(QPen(Qt.white, self.pen_width))

        self._coords = coords
        x, y = self._coords

        # sets desired position within the hex grid, adds to scene
        self.setPos((x + y) * 1.5 * side_len, (x - y) * side_len * 0.5 * 1.732)
        scene.addItem(self)
        self.setAcceptHoverEvents(True)

    def mousePressEvent(self, event):
        self.scene().itemClicked.emit(self)

    def hoverEnterEvent(self, event):
        self.setScale(1.05)

    def hoverLeaveEvent(self, event):
        self.setScale(1)

    def coords(self) -> Tuple[int, int]:
        return self._coords


class InteractiveGraphicsScene(QGraphicsScene):
    """
    a scene whose items can emit a signal throgh it when doubleclicked
    """
    itemClicked = Signal(object)


class ErrorDialog(QDialog):
    """
    a dialog with settable error information text and a confirmation button

    Methods
    --------
    set_error_message(message)
        sets desired error message to be shown in the dialog
    _finish()
        closes the dialog
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_errorDialog()
        self.ui.setupUi(self)
        self.ui.okButton.clicked.connect(self._finish)

    def set_error_message(self, message: str) -> None:
        self.ui.errorMessage.setText(message)

    def _finish(self) -> None:
        self.accept()


class HexGridView(QGraphicsView):
    """
    QGraphicsView object which allows for scrolling-based
    zoom in and zoom out
    """
    def wheelEvent(self, event) -> None:
        super().wheelEvent(event)
        if event.delta() > 0:
            self.scale(1.25, 1.25)
        else:
            self.scale(0.8, 0.8)
