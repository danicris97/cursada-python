import sys
from PyQt5 import QtWidgets,uic

class clsCalculator(QtWidgets.QMainWindow):
    def __init__(self):
        super(clsCalculator,self).__init__()
        uic.loadUi('TP 3/ejercicios/ejercicio_1/calculadora.ui',self)
        self.setUpUiComponents()


    def setUpUiComponents(self):
        #setea botones de numeros
        self.btn0.clicked.connect(lambda: self.insertaTextoFinal("0"))
        self.btn1.clicked.connect(lambda: self.insertaTextoFinal("1"))
        self.btn2.clicked.connect(lambda: self.insertaTextoFinal("2"))
        self.btn3.clicked.connect(lambda: self.insertaTextoFinal("3"))
        self.btn4.clicked.connect(lambda: self.insertaTextoFinal("4"))
        self.btn5.clicked.connect(lambda: self.insertaTextoFinal("5"))
        self.btn6.clicked.connect(lambda: self.insertaTextoFinal("6"))
        self.btn7.clicked.connect(lambda: self.insertaTextoFinal("7"))
        self.btn8.clicked.connect(lambda: self.insertaTextoFinal("8"))
        self.btn9.clicked.connect(lambda: self.insertaTextoFinal("9"))
        #setea botones operandos
        self.btnsuma.clicked.connect(lambda: self.insertaTextoFinal("+"))
        self.btnresta.clicked.connect(lambda: self.insertaTextoFinal("-"))
        self.btndivide.clicked.connect(lambda: self.insertaTextoFinal("/"))
        self.btnproducto.clicked.connect(lambda: self.insertaTextoFinal("*"))
        #setea botones extras
        self.btnpari.clicked.connect(lambda: self.insertaTextoFinal("("))
        self.btnpard.clicked.connect(lambda: self.insertaTextoFinal(")"))
        self.btncoma.clicked.connect(lambda: self.insertaTextoFinal("."))
        #setea botones con otras funciones
        self.btnce.clicked.connect(lambda: self.borraTexto())
        self.btnigual.clicked.connect(lambda: self.evalua())

    def insertaTextoFinal(self, caracter):
        texto = self.pantalla.toPlainText()
        self.pantalla.setText(texto + caracter)

    def borraTexto(self):
        self.pantalla.setText("")

    def evalua(self):
        texto = self.pantalla.toPlainText()
        try:
            self.pantalla.setText(str(eval(texto)))
        except:
            self.pantalla.setText("Syntaxis Error")

def main():
    app=QtWidgets.QApplication(sys.argv)

    objeto=clsCalculator()
    objeto.show()
    app.exec_()

if __name__=='__main__':
    main()