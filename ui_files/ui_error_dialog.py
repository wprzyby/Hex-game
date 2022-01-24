# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'error_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_errorDialog(object):
    def setupUi(self, errorDialog):
        if not errorDialog.objectName():
            errorDialog.setObjectName(u"errorDialog")
        errorDialog.resize(400, 150)
        self.verticalLayout_2 = QVBoxLayout(errorDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.errorMessage = QLabel(errorDialog)
        self.errorMessage.setObjectName(u"errorMessage")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.errorMessage.sizePolicy().hasHeightForWidth())
        self.errorMessage.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(18)
        self.errorMessage.setFont(font)
        self.errorMessage.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.errorMessage)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.okButton = QPushButton(errorDialog)
        self.okButton.setObjectName(u"okButton")

        self.horizontalLayout.addWidget(self.okButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(errorDialog)

        QMetaObject.connectSlotsByName(errorDialog)
    # setupUi

    def retranslateUi(self, errorDialog):
        errorDialog.setWindowTitle(QCoreApplication.translate("errorDialog", u"Error!", None))
        self.errorMessage.setText(QCoreApplication.translate("errorDialog", u"Error", None))
        self.okButton.setText(QCoreApplication.translate("errorDialog", u"OK", None))
    # retranslateUi

