import gettext
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QDialog

import sys

class clsSuma(QtWidgets.QMainWindow):
    
    def __init__(self, parent=None):
        super(clsSuma, self).__init__()
        
        uic.loadUi('TP 3/TP4_EjerPractica 1/sumaGUI.ui', self)
        
        self.setWindowTitle('Suma - DyPy 2022')
        
        self.setupComponents()
        
    def setupComponents(self):
        self.pushBtn2.clicked.connect(lambda: self.borrarTexto())
        
        self.pushBtn1.clicked.connect(lambda: self.evaluarSuma())
        
        self.pushBtn3.clicked.connect(lambda: self.cerrar())
        
    def borrarTexto(self):
        self.texto1.setText("")
        self.texto2.setText("")
        
    def evaluarSuma(self):
        text1 = self.texto1.toPlainText()
        text2 = self.texto2.toPlainText()
        
        resultado = int(text1) + int(text2)
        
        self.texto3.setText(str(resultado))
        
    def cerrar(self):
        self.close()
        

def main():
    app = QApplication(sys.argv)
    objeto = clsSuma()
    objeto.show()
    app.exec_()
    
if __name__ == '__main__':
    main()