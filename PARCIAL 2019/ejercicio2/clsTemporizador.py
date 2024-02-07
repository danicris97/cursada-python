import sys

from PyQt5 import QtWidgets,uic
from PyQt5.QtCore import QTimer


class clsTemporizador(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(clsTemporizador,self).__init__(parent)

        uic.loadUi("PARCIAL 2019/ejercicio2/temporizador.ui",self)

        self.setUiComponents()
        self.setInuputTiempo()
    
    def setUiComponents(self):
        self.bandera=False
        self.contador=0
        #setea texto
        self.resetInputTiempo()
        #setea pantalla
        self.pantalla.setDigitCount(6)
        self.pantalla.display("00:00:00")
        #setea botones
        self.btnstart.clicked.connect(self.start)
        self.btnpause.clicked.connect(self.pause)
        self.btnreset.clicked.connect(self.reset)
        #set tiempo
        self.timer=QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(100)

    def resetInputTiempo(self):
        self.lineEditHora.setText("0")
        self.lineEditMinuto.setText("0")
        self.lineEditSegundo.setText("0")
    
    def setInuputTiempo(self):
        self.horas=int(self.lineEditHora.text())
        self.minutos=int(self.lineEditMinuto.text())
        self.segundos=int(self.lineEditSegundo.text())

    def start(self):
        self.setInuputTiempo()
        self.bandera=True
        self.contador=self.horas*3600
        self.contador+=self.minutos*60
        self.contador+=self.segundos

    def pause(self):
        self.bandera=False

    def reset(self):
        self.bandera=False
        self.contador=0
        self.pantalla.display("00:00:00")
        self.resetInputTiempo()
        self.setInuputTiempo()

    def showTime(self):

        if self.bandera:
            self.contador-=1

        t=self.contador

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
    objeto=clsTemporizador()
    objeto.show()
    app.exec_()

if __name__=="__main__":
    main()