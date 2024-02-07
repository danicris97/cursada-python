import sys
from PyQt5 import QtWidgets,uic

class clsHello(QtWidgets.QMainWindow):
    def __init__(self):
        super(clsHello, self).__init__()
        uic.loadUi("TP 3/ejemplos/ejemplo1/uno.ui",self)

def main():
    app=QtWidgets.QApplication(sys.argv)

    objeto=clsHello()
    objeto.show()
    app.exec_()

if __name__=='__main__':
    main()