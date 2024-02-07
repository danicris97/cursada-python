
from PyQt5 import QtWidgets,uic

import sys

class clsFormResultado(QtWidgets.QMainWindow):
    def __init__(self, listaAlumnos, listaCond):
        super(clsFormResultado,self).__init__()
        uic.loadUi("Parcial 2022/ejercicio4/formResultado.ui",self)

        self.listaAlumnos=listaAlumnos
        self.listaCond=listaCond

        self.setGuiComponents()
        self.loadTable()


    def setGuiComponents(self):
        self.btnCerrar.clicked.connect(self.cerrar)

    def loadTable(self):
        self.tblResultado.setColumnCount(3)
        self.tblResultado.setRowCount(10)

        for i in range(10):
            for j in range(2):
                valor=QtWidgets.QTableWidgetItem(str(self.listaAlumnos[i][j]))
                self.tblResultado.setItem(i,j,valor)
            #agrega la condicion del alumno
            valor=QtWidgets.QTableWidgetItem(str(self.listaCond[i]))
            self.tblResultado.setItem(i,2,valor)

    def cerrar(self):
        self.hide()

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = clsFormResultado()
    form.show()
    app.exec_()

if __name__=="__main__":
    main()