import sys
from PyQt5 import QtWidgets,uic
import csv

class clsLogin(QtWidgets.QMainWindow):
    def __init__(self):
        super(clsLogin,self).__init__()
        uic.loadUi("PARCIAL 2019/ejercicio3/login.ui",self)

        self.setUiComponents()

    def setUiComponents(self):
        self.btnLogin.clicked.connect(self.login)
        self.btnClose.clicked.connect(self.close)

    # def generaDiccionario(self):
    #     aux={}
    #     archivo=open("PARCIAL 2019/ejercicio3/users.csv","r")

    #     try:
    #         reader=csv.reader(archivo,delimiter=",")
    #     finally:
    #         archivo.close()

    #     return aux

    def login(self):
        archivo=open("PARCIAL 2019/ejercicio3/users.csv","r")
        aux=[]
        
        try:
            for linea in archivo:
                #linea=linea.rsplit("\n")
                columnas=linea.split(",")
                aux.append((columnas[0],columnas[1]))
        finally:
            archivo.close()

        user=self.lineEditUser.text()
        password=self.lineEditPassword.text()

        if (user,password) in aux:
            print("login")
        else:
            print("error")

    def close(self):
        self.hide()

def main():
    app=QtWidgets.QApplication(sys.argv)

    objeto=clsLogin()
    objeto.show()
    app.exec_()

if __name__=='__main__':
    main()