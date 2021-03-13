# modulos de PySide2 utilizados
from PySide2.QtWidgets import QDialog
from PySide2.QtWidgets import QHeaderView

# importar diseño
from view.ui_VentanaDos import Ui_VentanaDos

# VENTANA 2 -*-*-*-
class Vista_Ventana_Dos(QDialog):
    def __init__(self, parent):
        super(Vista_Ventana_Dos, self).__init__()

        self.raizdos = Ui_VentanaDos()
        self.raizdos.setupUi(self)

        # se necesita el parent para acceder al cerrado 
        # del efecto, por ello se declara el "parent"
        self.parent = parent

        # boton cerrar ventana
        self.raizdos.btncerrar.clicked.connect(lambda : self.close())

    def keyPressEvent(self, event):
        # evitar el cierre de la ventan con la tecla "esc"
        if event.key() == 16777216:
            event.ignore()

    # CERRADO DE VENTANA
    def closeEvent(self, event):
        # la "raizOpacidad" por defecto debe estar instanciada 
        # en la ventana principal para poder cerrarlo
        self.parent.raizOpacidad.close()
        event.accept()