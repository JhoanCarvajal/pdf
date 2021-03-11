from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.uic import loadUi
import controlador
import pdf2img

class CrearRoiOperador(QtWidgets.QMainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super(CrearRoiOperador, self).__init__(parent)
        loadUi('plantillas/crear_roi_operador.ui', self)

        self.posicion_1 = [0,0]
        self.posicion_2 = [0,0]

        self.btn_seleccionar.clicked.connect(self.seleccionar)

    def seleccionar(self):
        self.statusBar().showMessage('seleccionando archivo')
        pdf_ruta, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Abrir pdf", None, "pdf files (*.pdf)")
        # self.lb_ruta.setText(pdf_ruta)
        if pdf_ruta != "":
            self.statusBar().showMessage('Cargando el pdf seleccionado...')
            lista_imagenes = pdf2img.pdf2img(pdf_ruta)
            print(lista_imagenes)
            for ruta_img in lista_imagenes:
                print(ruta_img)
                pixmap = QtGui.QPixmap(ruta_img)
                self.img_operador.setPixmap(pixmap)
        else:
            self.statusBar().showMessage('No se ha seleccionado un pdf')
        
    def paintEvent(self, event):
        ancho = self.posicion_2[0] - self.posicion_1[0]
        alto = self.posicion_2[1] - self.posicion_1[1]

        painter = QtGui.QPainter()
        painter.begin(self)
        painter.drawRect(self.posicion_1[0], self.posicion_1[1], ancho, alto)
        painter.end()

    def mousePressEvent(self, event):
        if event.buttons() & Qt.Qt.LeftButton:
            self.posicion_1[0] = event.pos().x()
            self.posicion_1[1] = event.pos().y()

    def mouseReleaseEvent(self, event):
        self.posicion_2[0] = event.pos().x()
        self.posicion_2[1] = event.pos().y()

        self.update()
    
    def abrir_ventana_principal(self):
        self.parent().show()
        self.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    ventana = CrearRoiOperador()
    ventana.show()
    app.exec_()