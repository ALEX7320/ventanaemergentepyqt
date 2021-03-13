# modulos de PySide2 utilizados
from PySide2.QtWidgets import QApplication,QMainWindow

# importar diseño
from view.ui_VentanaUno import Ui_VentanaUno

# importar efecto opacidad
from efectos import Clase_Opacidad,abrirVenOpaci

# importar ventana emergente
from vendos import Vista_Ventana_Dos

# VENTANA 1 -*-*-*-
class Vista_Ventana_Uno(QMainWindow):
    def __init__(self):
        super(Vista_Ventana_Uno, self).__init__()

        self.raizuno = Ui_VentanaUno()
        self.raizuno.setupUi(self)

        # instanciar clase opacidad antes de todo
        self.raizOpacidad = Clase_Opacidad(self)
        self.raizOpacidad.close() # por defecto cerrado

        # abrir ventana emergente
        self.raizuno.btnabrirventana.clicked.connect(lambda : 
            abrirVenOpaci(self, # clase
                          self.raizOpacidad, # clase opacidad
                          Vista_Ventana_Dos(self) # ventana nueva
                          )
                        )

