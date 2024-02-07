from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QAction, QMainWindow, qApp, QFileDialog
from PyQt5.QtGui import QIcon

import sys
import clsTable as loadCuatro



# http://zetcode.com/gui/pyqt5/menustoolbars/
# https://realpython.com/python-menus-toolbars/#using-icons-and-resources-in-pyqt
# http://zetcode.com/gui/pyqt5/dialogs/


class clsMenu(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		
		self.initUi()

		self.fileName=''
	

	def initUi(self):
		self.statusBar().showMessage('Listo')
		
		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')

		exitAction = QAction(QIcon('resources/icons/download.png'), '&Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit application')
		exitAction.triggered.connect(qApp.quit)

		openAction = QAction(QIcon('resources/icons/open-share.png'), '&Open', self)
		openAction.setShortcut('Ctrl+O')
		openAction.setStatusTip('Open CSV')
		openAction.triggered.connect(self.openCSV)
		
		fileMenu.addAction(openAction)
		fileMenu.addAction(exitAction)


		self.setGeometry(300,300,250,150)
		self.setWindowTitle('Dipy 2021 - Menu')
		self.show()
		

	def openCSV(self):
		fname = QFileDialog.getOpenFileName(self, 'Open file', '/home/',"CSV files (*.csv)")
		if fname[0]:
			self.fileName = fname[0]
			self.statusBar().showMessage('Archivo abierto ' + self.fileName)

			self.w = loadCuatro.clsTable(self.fileName)
			self.w.show()


		else:
			self.fileName=''
			self.statusBar().showMessage("No eligio archivo")



def main():
	app = QApplication(sys.argv)
	
	objeto = clsMenu()
	objeto.show()
	app.exec_()

if __name__ == '__main__':
	main()