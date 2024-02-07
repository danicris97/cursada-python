import clsIrisF

import sys
from PyQt5 import QtWidgets,uic

class clsLogin(QtWidgets.QMainWindow):
    def __init__(self):
        super(clsLogin,self).__init__()
        uic.loadUi("TP 4/ejercicio_6/login.ui",self)

        self.objIris =  clsIrisF.clsIris()
        self.setUiComponents()

    def setUiComponents(self):
        self.btnLogin.clicked.connect(self.login)
        self.btnClose.clicked.connect(self.close)

    def login(self):
        try:
            result = self.objIris.getLogin()
            print(result)

            usuario=self.lineEditUser.text()
            print(usuario)
            password=self.lineEditPassword.text()
            print(password)

            for i in range(len(result)):
                if usuario in result[i]:
                    if password in result[i][3]:
                        print("logueado")

        except:
            print("error al obtener datos")

    def close(self):
        None

def main():
    app=QtWidgets.QApplication(sys.argv)

    objeto=clsLogin()
    objeto.show()
    app.exec_()

if __name__=='__main__':
    main()