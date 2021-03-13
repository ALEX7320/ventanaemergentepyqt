# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_VentanaUnoCzlTIs.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_VentanaUno(object):
    def setupUi(self, VentanaUno):
        if not VentanaUno.objectName():
            VentanaUno.setObjectName(u"VentanaUno")
        VentanaUno.resize(785, 529)
        self.centralwidget = QWidget(VentanaUno)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size:25px;")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 3)

        self.btnabrirventana = QPushButton(self.frame)
        self.btnabrirventana.setObjectName(u"btnabrirventana")
        self.btnabrirventana.setMinimumSize(QSize(250, 100))
        self.btnabrirventana.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_2.addWidget(self.btnabrirventana, 3, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 3, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 4, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        VentanaUno.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaUno)

        QMetaObject.connectSlotsByName(VentanaUno)
    # setupUi

    def retranslateUi(self, VentanaUno):
        VentanaUno.setWindowTitle(QCoreApplication.translate("VentanaUno", u"Ventana Uno - ALEX7320", None))
        self.label.setText(QCoreApplication.translate("VentanaUno", u"Ventana Uno", None))
        self.btnabrirventana.setText(QCoreApplication.translate("VentanaUno", u"Abrir ventana", None))
    # retranslateUi

