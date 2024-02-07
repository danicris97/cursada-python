
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

import sys

# https://www.geeksforgeeks.org/pyqt5-digital-stopwatch/
# https://www.qtcentre.org/threads/39942-How-to-show-the-seconds-in-the-digital-clock-using-QLcd-Number


class clsClock(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		super(clsClock, self).__init__(parent)
		
		uic.loadUi('TP 3/codigo/tres.ui',self)

		self.setWindowTitle('Dipy 2021: Cronometro')
		self.setGeometry(100, 100, 370, 160)
		self.setupUiComponents()

	def setupUiComponents(self):
		self.counter = 0
		self.flag = False
		self.lcdNumber.setDigitCount(5)
		self.lcdNumber.display('00:00.0')

		self.btnStart.clicked.connect(self.start)
		self.btnPause.clicked.connect(self.pause)
		self.btnReset.clicked.connect(self.reset)

		self.timer = QTimer(self)
		self.timer.timeout.connect(self.showTime)
		self.timer.start(100)

	def start(self):
		self.flag = True

	def pause(self):
		self.flag = False

	def reset(self):
		self.flag = False
		self.counter = 0
		self.lcdNumber.display('00:00.0')

	def showTime(self):
		if self.flag:
			self.counter +=1

		number = str(self.counter / 10)

		t = self.counter
		
		D = t%10
		t //= 10
		
		C = t%10
		t //= 10
		
		B = t % 6
		t //= 6
		
		A = t % 10
		

		self.lcdNumber.display(str(A) + ':' + str(B) + str(C) + '.' + str(D))		

		#self.lcdNumber.display(number)
		if self.flag:
			print(str(A) + '-' + str(B) + '-' + str(C) + '-' + str(D))

def main():
	app = QApplication(sys.argv)
	objeto = clsClock()
	objeto.show()
	app.exec_()

if __name__ == '__main__':
	main()