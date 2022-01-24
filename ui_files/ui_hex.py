# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hex.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from gui_classes import HexGridView


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1200, 800)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(66, 66, 66, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(99, 99, 99, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(82, 82, 82, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(33, 33, 33, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(44, 44, 44, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush7 = QBrush(QColor(255, 255, 220, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush8 = QBrush(QColor(255, 255, 255, 128))
        brush8.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        mainWindow.setPalette(palette)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stack = QStackedWidget(self.centralwidget)
        self.stack.setObjectName(u"stack")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(80)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.PlainText)
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setPointSize(30)
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.label_5)

        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(16)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_3.addWidget(self.label_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.playerOneInputLine = QLineEdit(self.page)
        self.playerOneInputLine.setObjectName(u"playerOneInputLine")
        self.playerOneInputLine.setMinimumSize(QSize(250, 30))
        self.playerOneInputLine.setMaxLength(70)

        self.horizontalLayout_2.addWidget(self.playerOneInputLine)

        self.playerOneColor = QGraphicsView(self.page)
        self.playerOneColor.setObjectName(u"playerOneColor")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerOneColor.sizePolicy().hasHeightForWidth())
        self.playerOneColor.setSizePolicy(sizePolicy)
        self.playerOneColor.setMaximumSize(QSize(35, 35))

        self.horizontalLayout_2.addWidget(self.playerOneColor)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.playerTwoInputLine = QLineEdit(self.page)
        self.playerTwoInputLine.setObjectName(u"playerTwoInputLine")
        self.playerTwoInputLine.setMinimumSize(QSize(250, 30))
        self.playerTwoInputLine.setMaxLength(70)

        self.horizontalLayout_3.addWidget(self.playerTwoInputLine)

        self.playerTwoColor = QGraphicsView(self.page)
        self.playerTwoColor.setObjectName(u"playerTwoColor")
        sizePolicy.setHeightForWidth(self.playerTwoColor.sizePolicy().hasHeightForWidth())
        self.playerTwoColor.setSizePolicy(sizePolicy)
        self.playerTwoColor.setMaximumSize(QSize(35, 35))

        self.horizontalLayout_3.addWidget(self.playerTwoColor)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.label_3)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.boardRadiusInput = QSpinBox(self.page)
        self.boardRadiusInput.setObjectName(u"boardRadiusInput")
        self.boardRadiusInput.setMinimum(1)
        self.boardRadiusInput.setMaximum(7)

        self.horizontalLayout_5.addWidget(self.boardRadiusInput)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.label_6 = QLabel(self.page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.label_6)

        self.setupConfirmButton = QPushButton(self.page)
        self.setupConfirmButton.setObjectName(u"setupConfirmButton")
        font3 = QFont()
        font3.setPointSize(14)
        self.setupConfirmButton.setFont(font3)

        self.verticalLayout_3.addWidget(self.setupConfirmButton)

        self.stack.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_5 = QVBoxLayout(self.page_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.currentPlayer = QLabel(self.page_2)
        self.currentPlayer.setObjectName(u"currentPlayer")
        self.currentPlayer.setFont(font3)
        self.currentPlayer.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_6.addWidget(self.currentPlayer)

        self.currentPlayerColor = QGraphicsView(self.page_2)
        self.currentPlayerColor.setObjectName(u"currentPlayerColor")
        sizePolicy.setHeightForWidth(self.currentPlayerColor.sizePolicy().hasHeightForWidth())
        self.currentPlayerColor.setSizePolicy(sizePolicy)
        self.currentPlayerColor.setMaximumSize(QSize(35, 35))

        self.horizontalLayout_6.addWidget(self.currentPlayerColor)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.hexBoard = HexGridView(self.page_2)
        self.hexBoard.setObjectName(u"hexBoard")
        palette1 = QPalette()
        brush9 = QBrush(QColor(59, 59, 59, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        self.hexBoard.setPalette(palette1)
        self.hexBoard.setFont(font3)

        self.verticalLayout_4.addWidget(self.hexBoard)

        self.winnerPrompt = QLabel(self.page_2)
        self.winnerPrompt.setObjectName(u"winnerPrompt")
        self.winnerPrompt.setMinimumSize(QSize(0, 55))
        font4 = QFont()
        font4.setPointSize(17)
        self.winnerPrompt.setFont(font4)
        self.winnerPrompt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_4.addWidget(self.winnerPrompt)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.rematchButton = QPushButton(self.page_2)
        self.rematchButton.setObjectName(u"rematchButton")

        self.horizontalLayout_7.addWidget(self.rematchButton)

        self.restartButton = QPushButton(self.page_2)
        self.restartButton.setObjectName(u"restartButton")
        self.restartButton.setEnabled(True)

        self.horizontalLayout_7.addWidget(self.restartButton)

        self.exitButton = QPushButton(self.page_2)
        self.exitButton.setObjectName(u"exitButton")

        self.horizontalLayout_7.addWidget(self.exitButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.stack.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stack)


        self.horizontalLayout.addLayout(self.verticalLayout)

        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        self.stack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Hex", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"HEX GAME", None))
        self.label_5.setText(QCoreApplication.translate("mainWindow", u"SETUP", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"Player names (leave empty for default names):", None))
        self.playerOneInputLine.setPlaceholderText(QCoreApplication.translate("mainWindow", u"Player 1", None))
        self.playerTwoInputLine.setPlaceholderText(QCoreApplication.translate("mainWindow", u"Player 2", None))
        self.label_3.setText(QCoreApplication.translate("mainWindow", u"First to move", None))
        self.label_4.setText(QCoreApplication.translate("mainWindow", u"Board radius:", None))
        self.label_6.setText(QCoreApplication.translate("mainWindow", u"From 1 to 7", None))
        self.setupConfirmButton.setText(QCoreApplication.translate("mainWindow", u"START GAME", None))
        self.currentPlayer.setText("")
        self.winnerPrompt.setText("")
        self.rematchButton.setText(QCoreApplication.translate("mainWindow", u"REMATCH", None))
        self.restartButton.setText(QCoreApplication.translate("mainWindow", u"RESTART", None))
        self.exitButton.setText(QCoreApplication.translate("mainWindow", u"EXIT", None))
    # retranslateUi

