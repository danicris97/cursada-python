
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication
import sys


class clsCalculator(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(clsCalculator, self).__init__()
        uic.loadUi('TP 3/codigo/dos.ui',self)
        self.setupUiComponents()
        

    def setupUiComponents(self):
    	# click 
        self.btnBorraTodo.clicked.connect(self.borrarTexto)

        self.btn0.clicked.connect(lambda: self.insertaFin('0'))
        self.btn1.clicked.connect(lambda: self.insertaFin('1'))
        self.btn2.clicked.connect(lambda: self.insertaFin('2'))
        self.btnSuma.clicked.connect(lambda: self.insertaFin('+'))    	
        self.btnIgual.clicked.connect(lambda: self.evalua())


    def borrarTexto(self):
    	self.edtTexto.setText("")
        
    def insertaFin(self, caracter):
        texto = self.edtTexto.toPlainText()
        self.edtTexto.setText(texto + caracter)

    def evalua(self):
        texto = self.edtTexto.toPlainText()
        self.edtTexto.setText(str(eval(texto)))



def main():
    app = QApplication(sys.argv)
    objeto = clsCalculator()
    objeto.show()
    app.exec_()

if __name__ == '__main__':
    main()