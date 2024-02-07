from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTableWidgetItem
import csv
import sys


from tempfile import NamedTemporaryFile
import shutil
import clsForm as loadForm

from multipledispatch import dispatch

# https://www.geeksforgeeks.org/pyqt5-qtablewidget/
# https://doc.qt.io/qt-5/qtablewidget.html
# https://doc.qt.io/qt-5/qtablewidgetitem.html
# https://www.programiz.com/python-programming/writing-csv-files
# https://stackoverflow.com/questions/46126082/how-to-update-rows-in-a-csv-file

# doble clic
# https://ifelse.info/questions/12924/associate-event-double-click-qtablewidget-slot-and-get-row


class clsTable(QtWidgets.QMainWindow):
	def __init__(self, fileName, parent=None):
		super(clsTable, self).__init__(parent)
		
		uic.loadUi('TP 3/ejercicios/ejercicio_3/cuatro.ui',self)

		self.fileName = fileName
		self.auxFile = 'TP 3/ejercicios/ejercicio_3/temporary.csv'

		self.setupUiComponents()		



	def setupUiComponents(self):
		self.tblData.resizeColumnsToContents()
		self.tblData.resizeRowsToContents()

		self.loadTable()
		self.btnGuardar.clicked.connect(self.updateCSV)
		self.tblData.doubleClicked.connect(self.loadForm)
		self.btnSalir.clicked.connect(self.cerrar)


	@QtCore.pyqtSlot(QtCore.QModelIndex)
	def loadForm(self,index):
		
		column = index.column()
		if column ==4:
			# abro el form
			row = index.row()			

			sl = self.tblData.item(row, 0).text()
			sw = self.tblData.item(row, 1).text()
			pl = self.tblData.item(row, 2).text()
			pw = self.tblData.item(row, 3).text()
			variety = self.tblData.item(row, 4).text()

			self.w = loadForm.clsForm(sl,sw,pl,pw,variety,self,row)
			self.w.show()
			#self.w.btnGuardar.clicked.connect(lambda: self.updateCSV(row)) primera idea

	def loadTable(self):
		myFile = open(self.fileName, 'r')
		try:
			reader = csv.reader(myFile, delimiter=',')

			rowI=0
			for row in reader:
				self.tblData.setRowCount(rowI+1)

				if rowI==0:
					columns =len(row)
					self.tblData.setColumnCount(columns)

				columns = len(row)
				for columnJ in range(columns):
					myValue = row[columnJ]
					cell = QTableWidgetItem(str(myValue))
					
					self.tblData.setItem(rowI,columnJ,cell)
					
				rowI = rowI + 1
		finally:
			myFile.close()
	
	@dispatch(int)
	def updateCSV(self,fila):
		rows = self.tblData.rowCount()
		cols = self.tblData.columnCount()

		newList=[]
		for i in range(rows):
			auxList = []
			if(i==fila):
				newList.append(self.w.recuperaDatos())
			else:
				for j in range(cols):
					cell = self.tblData.item(i, j).text()
					auxList.append(cell)

					print("i " + str(i) + " j " + str(j) + " " + str(cell))

				newList.append(auxList)


		with open(self.auxFile, 'w', newline='') as file:
			writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
			writer.writerows(newList)


		shutil.move(self.auxFile, self.fileName)
		self.loadTable()

		print("Update de csv exitoso")

	@dispatch()
	def updateCSV(self):
		rows = self.tblData.rowCount()
		cols = self.tblData.columnCount()

		newList=[]
		for i in range(rows):
			auxList = []
			for j in range(cols):
				cell = self.tblData.item(i, j).text()
				auxList.append(cell)

				print("i " + str(i) + " j " + str(j) + " " + str(cell))

			newList.append(auxList)


		with open(self.auxFile, 'w', newline='') as file:
			writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
			writer.writerows(newList)


		shutil.move(self.auxFile, self.fileName)
		self.loadTable()

		print("Update de csv exitoso")

	def cerrar(self):
		self.close()


def main():
	app = QApplication(sys.argv)
	
	fileName='TP 3/ejercicios/ejercicio_3/iris.csv'
	
	objeto = clsTable(fileName)
	objeto.show()
	app.exec_()

if __name__ == '__main__':
	main()