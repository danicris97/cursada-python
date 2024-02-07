
import clsFormResultado as formResul
from PyQt5 import QtCore,QtWidgets,uic


import sys
import random

class clsTabla(QtWidgets.QMainWindow):
    def __init__(self):
        super(clsTabla,self).__init__()
        
        uic.loadUi("Parcial 2022/ejercicio4/tabla.ui",self)

        self.setGuiComponents()
        self.loadTable()

    def setGuiComponents(self):
        self.btnRegular.clicked.connect(self.obtenerRegularidad)
        self.btnCerrar.clicked.connect(self.cerrar)

    def generaAlumnos(self):#4x10
        a=[]

        for i in range(10):
            alumno=["x" + str(i),"y" + str(10-i),random.randint(-1,100)]

            if(int(alumno[2])<60):
                alumno.append(random.randint(-1,100))
            else:
                alumno.append("''")

            a.append(alumno)

        return a

    def loadTable(self):
        self.alumnos=self.generaAlumnos()

        self.tblData.setColumnCount(4)
        self.tblData.setRowCount(10)
        
        for i in range(10):
            for j in range(4):
                valor=QtWidgets.QTableWidgetItem(str(self.alumnos[i][j]))
                self.tblData.setItem(i,j,valor)

    def obtenerRegularidad(self):
        condicion=[]

        for i in range(10):
            #print(type(self.tblData.item(i,2).text()))
            if(int(self.tblData.item(i,2).text())>59 or int(self.tblData.item(i,3).text())>59):
                condicion.append("Regularizo")
            elif(int(self.tblData.item(i,3).text())==-1):
                condicion.append("Abandono")
            else:
                condicion.append("No Regularizo")

        print(condicion)
        lista=self.alumnos
        print(lista)
        self.w = formResul.clsFormResultado(lista ,condicion)
        self.w.show()

    def cerrar(self):
        self.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    obj = clsTabla()
    obj.show()
    app.exec_()

if __name__=="__main__":
    main()