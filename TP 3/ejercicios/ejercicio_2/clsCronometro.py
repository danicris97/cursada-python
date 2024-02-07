import sys

from PyQt5 import QtWidgets,uic
from PyQt5.QtCore import QTimer

class clsCronometro(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(clsCronometro,self).__init__(parent)

        uic.loadUi('TP 3/ejercicios/ejercicio_2/cronometro.ui',self)

        self.setWindowTitle("cronometro")
        self.setGeometry(100,100,400,160)
        self.setUiComponents()

    def setUiComponents(self):
        self.bandera=False
        self.contador=0
        #setea pantalla
        self.pantalla.setDigitCount(6)
        self.pantalla.display("00:00:0.0")
        #setea botones
        self.btnstart.clicked.connect(self.start)
        self.btnpause.clicked.connect(self.pause)
        self.btnreset.clicked.connect(self.reset)
        #set tiempo
        self.timer=QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(100)

    def start(self):
        self.bandera=True

    def pause(self):
        self.bandera=False

    def reset(self):
        self.bandera=False
        self.contador=0
        self.pantalla.display("00:00:0.0")

    def showTime(self):
        if self.bandera:
            self.contador+=1

        t = self.contador
        
        D = t%10
        t //= 10
        C = t%10
        t //= 10
        B = t % 6
        t //= 6
        A = t % 10
        t //= 6
        E = t % 10

        self.pantalla.display(str(E) + ":" + str(A) + ':' + str(B) + str(C) + '.' + str(D))


def main():
    app=QtWidgets.QApplication(sys.argv)
    objeto=clsCronometro()
    objeto.show()
    app.exec_()

if __name__=="__main__":
    main()