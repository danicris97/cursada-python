from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication

import sys

import clsSuma as sumaGui

def main():
    app = QApplication(sys.argv)
    objeto = sumaGui.clsSuma()
    objeto.show
    app.exec_()
    
if __name__ == '__main__':
    main()