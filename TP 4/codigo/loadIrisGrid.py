from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem

import sys
import clsIrisF
import clsIrisTypeF
import loadIrisForm

# https://realpython.com/python-pyqt-database/
# https://stackoverflow.com/questions/14588479/retrieving-cell-data-from-a-selected-cell-in-a-tablewidget/14589213
# https://www.learnpyqt.com/tutorials/creating-multiple-windows/

class clsIrisGrid(QtWidgets.QMainWindow):
	def __init__(self):
		super(clsIrisGrid, self).__init__()
		uic.loadUi('TP 4/codigo/grid.ui',self)

		self.row=-1
		self.column=-1

		self.objIris =  clsIrisF.clsIris()
		self.setupUiComponents()

		print ("Entreeee")


	def setupUiComponents(self):
		self.tblData.resizeColumnsToContents()
		self.tblData.resizeRowsToContents()


		self.loadTable()
		self.tblData.cellClicked.connect(self.cell_was_clicked)
		
		self.tblData.doubleClicked.connect(self.loadForm)
		

		self.btnInsertar.clicked.connect(self.insert)
		self.btnEditar.clicked.connect(self.update)
		self.btnEliminar.clicked.connect(self.delete)

		self.btnSalir.clicked.connect(self.close)


	def cell_was_clicked(self, row, column):
		self.row=row
		self.column=column


	@QtCore.pyqtSlot(QtCore.QModelIndex)
	def loadForm(self,index):
		
		column = index.column()
		row = index.row()			

		print(row, column)


	def loadTable(self):
		try:
			result = self.objIris.getData()
			self.tblData.setRowCount(0)
			self.tblData.setColumnCount(6)
			self.tblData.setHorizontalHeaderLabels(["ID", "SL", "SW", "PL", "PW", "description"])

			for elem in result:
				rows = self.tblData.rowCount()

				self.tblData.setRowCount(rows + 1)
				self.tblData.setItem(rows, 0, QTableWidgetItem(str(elem[0])))
				self.tblData.setItem(rows, 1, QTableWidgetItem(str(elem[1])))
				self.tblData.setItem(rows, 2, QTableWidgetItem(str(elem[2])))
				self.tblData.setItem(rows, 3, QTableWidgetItem(str(elem[3])))
				self.tblData.setItem(rows, 4, QTableWidgetItem(str(elem[4])))
				self.tblData.setItem(rows, 5, QTableWidgetItem(str(elem[6])))

			self.tblData.resizeColumnsToContents()

		except:
			print('Error al cargar datos en grilla')


	def delete(self):
		if self.row>-1 and self.column>-1:
			ID = int(self.tblData.item(self.row, 0).text())
			try:
				self.objIris.delete(ID)

				print ("Exito. Eliminacion correcta de iris ID= " + str(ID))

				self.tblData.removeRow(self.row)

			except Exception as e:
				print('Error en la eliminacion ' + str(e))

		else:
			print ("Error. No seleccionó fila")


	def update(self):
		if(self.row>-1 and self.column>-1):
			ID = int(self.tblData.item(self.row,0).text())
			
			sl=float(self.tblData.item(self.row,1).text())
			sw=float(self.tblData.item(self.row,2).text())
			pl=float(self.tblData.item(self.row,3).text())
			pw=float(self.tblData.item(self.row,4).text())
			variety=str(self.tblData.item(self.row,5).text())
			self.w = loadIrisForm.clsIrisForm(sl,sw,pl,pw,variety,ID)
			self.w.show()
			
		else:
			print("Error. No seleccionó fila")

	def insert(self):
		self.w = loadIrisForm.clsIrisForm()
		self.w.show()

	def close(self):
		None
		

def main():
	app = QtWidgets.QApplication(sys.argv)
	
	form = clsIrisGrid()
	form.show()
	app.exec_()

if __name__ == '__main__':
	main()