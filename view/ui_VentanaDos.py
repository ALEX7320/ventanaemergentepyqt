# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_VentanaDosFAUyNX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_VentanaDos(object):
    def setupUi(self, VentanaDos):
        if not VentanaDos.objectName():
            VentanaDos.setObjectName(u"VentanaDos")
        VentanaDos.resize(370, 170)
        self.label = QLabel(VentanaDos)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 20, 211, 61))
        self.label.setStyleSheet(u"font-size:18px;")
        self.label.setAlignment(Qt.AlignCenter)
        self.btncerrar = QPushButton(VentanaDos)
        self.btncerrar.setObjectName(u"btncerrar")
        self.btncerrar.setGeometry(QRect(120, 90, 141, 41))
        self.btncerrar.setFocusPolicy(Qt.NoFocus)

        self.retranslateUi(VentanaDos)

        QMetaObject.connectSlotsByName(VentanaDos)
    # setupUi

    def retranslateUi(self, VentanaDos):
        VentanaDos.setWindowTitle(QCoreApplication.translate("VentanaDos", u"Ventana Dos", None))
        self.label.setText(QCoreApplication.translate("VentanaDos", u"Ventana Dos", None))
        self.btncerrar.setText(QCoreApplication.translate("VentanaDos", u"Cerrar", None))
    # retranslateUi

