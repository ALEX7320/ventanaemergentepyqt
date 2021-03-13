# modulos de PySide2 utilizados
from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPainter,QColor,QPen

# CLASE DE OPACIDAD
class Clase_Opacidad(QWidget):

    def __init__(self, parent = None):
        super(Clase_Opacidad, self).__init__(parent)

    # evento de QPainter
    def paintEvent(self, event):
        
        qp = QPainter()
        qp.begin(self)

        pen = QPen()
        pen.setColor(QColor(0,0,0,0)) # pincel por defecto invisible
        qp.setPen(pen)

        # COLOR DE LA TANSPARENCIA /*/*/*/*/*/*/*/*/*/*/
        # color (r, g, b, a)
        # a = 0 → 255 (transparencia)
        qp.setBrush(QColor(0, 0, 0, 150))
        # poner el efecto al tamaño que se le aplico a esta clase
        qp.drawRect(0, 0, self.size().width(), self.size().height())
        qp.end()

# CLASE PARA ABRIR VENTANAS
def abrirVenOpaci(parent, opacidad, ventana):
    # mostramo la "Clase_Opacidad" tomando el tamaño actual 
    # de nuestra ventana principal
    opacidad.resize(parent.width(), parent.height())
    opacidad.show()

    # abrimos la ventana secundaria
    ventana.exec_()