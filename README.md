# Efecto opacidad (ventana emergente) PyQt

**Indice**
  * [Personalización](#personalización)
  * [Parametros](#parametros)
  * [Cerrar ventana y efecto](#cerrar-ventana-y-efecto)
  * [Tener en cuenta](#tener-en-cuenta)
  * [Previsualización](#previsualización)

# Recursos utilizados

`pip install PySide2`

# Personalización

El color es definido por el tipo RGBA donde A indica la transparencia del la capa,  teniendo en cuenta que la transparencia de esta va desde `0` a `255`

```python
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
```

# Parametros

Para ello tenemos que tener en cuenta estos dos puntos.

Modulo `venuno.py`
```python
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
```

Modulo `efectos.py`

```python
# CLASE PARA ABRIR VENTANAS
def abrirVenOpaci(parent, opacidad, ventana):
    # mostramo la "Clase_Opacidad" tomando el tamaño actual 
    # de nuestra ventana principal
    opacidad.resize(parent.width(), parent.height())
    opacidad.show()

    # abrimos la ventana secundaria
    ventana.exec_()
```

**Referencias**

|  Parametros | Ingreso  |  Definición |
| :------------: | :------------: | :------------: |
| parent  | self  |  clase principal |
|  opacidad |   self.raizOpacidad |  clase opacidad previamente instanciada |
|  ventana |  Vista_Ventana_Dos(self) |  ventana que se desea abrir |

# Cerrar ventana y efecto

Para ello se instancia el parent, esto para tener acceso a la clase `raizOpacidad` que fue instanciada previamente en la ventana principal (`venuno.py`), despues de ello simplemente conectamos el evento de cerrado de ventana

```python
        self.parent = parent

        # boton cerrar ventana
        self.raizdos.btncerrar.clicked.connect(lambda : self.close())
```

Es en el `closeEvent` donde realizamos el cierre de `raizOpacidad` y la ventana actual.

```python
    # CERRADO DE VENTANA
    def closeEvent(self, event):
        # la "raizOpacidad" por defecto debe estar instanciada 
        # en la ventana principal para poder cerrarlo
        self.parent.raizOpacidad.close()
        event.accept()
```

# Tener en cuenta

El focus del objeto `btncerrar` se le cambio a `NoFocus` esto para evitar cerrar la ventana con la tecla `Enter`.  

![](https://1.bp.blogspot.com/-JvqvmEJNVN8/YEwmG5ow17I/AAAAAAAAAF4/0C528reszpwecAFgb77-UZBJ0oU1GgiTQCLcBGAsYHQ/s1600/Pointofix%2B12_03_2021%2B09_39_12%2BPM.png)

Al igual que con el boton, la tecla `Esc` tabien tiene el acceso de cerrar la ventana, es por ello que solo se ignoro el evento al tocar dicho teclado.

Modulo `vendos.py`
```python
    def keyPressEvent(self, event):
        # evitar el cierre de la ventan con la tecla "esc"
        if event.key() == 16777216:
            event.ignore()
```


# Previsualización

![](https://1.bp.blogspot.com/-AAXMXGOe4M8/YEwhFDpOHII/AAAAAAAAAFw/kjwv3ubCfxYIxcxy5RPCEq2p4wAL1j_CACLcBGAsYHQ/s1600/A2.jpg)