# modulos de PySide2 utilizados
from PySide2.QtWidgets import QApplication

# primera ventana en ser ejecutada
from venuno import Vista_Ventana_Uno

if __name__ == "__main__":

    import sys

    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    mi_aplicacion = Vista_Ventana_Uno()
    mi_aplicacion.show()
    sys.exit(app.exec_())
