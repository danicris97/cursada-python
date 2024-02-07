from asyncore import write
from dis import dis
from PyQt5 import QtWidgets, uic

import sys

# http://zetcode.com/pyqt/qspinbox/
# https://stackoverflow.com/questions/45589751/pyqt5-connect-a-change-in-qtwidgets-qdoublespinbox
# https://www.geeksforgeeks.org/pyqt5-qdoublespinbox-setting-value/
# https://www.geeksforgeeks.org/pyqt5-qdoublespinbox-getting-minimum-possible-value/

# https://nitratine.net/blog/post/how-to-import-a-pyqt5-ui-file-in-a-python-gui/
# http://zetcode.com/pyqt/qcombobox/
#  https://www.geeksforgeeks.org/pyqt5-setting-current-text-in-combobox/
# https://www.geeksforgeeks.org/pyqt5-getting-the-text-of-selected-item-in-combobox/


class clsForm(QtWidgets.QMainWindow):
	def __init__(self, sl=None, sw=None, pl=None, pw=None, variety=None,table=None,row=None):
		super(clsForm, self).__init__()
		uic.loadUi('TP 3/ejercicios/ejercicio_3/csvForm.ui',self)
		self.table=table
		self.setupUi()

		#sl='0.5'
		#sw='0.6'
		#pl='0.7'
		#pw='0.8'
		#variety='Versicolor'
		
		if sl!=None and sw!=None and pl!=None and pw!=None and variety!=None:
			self.loadValues(sl, sw, pl, pw, variety)

		#segunda idea
		if row!=None:
			self.row=row

	def setupUi(self):
		self.btnGuardar.clicked.connect(self.guardar)
		self.btnCerrar.clicked.connect(self.cerrar)

		self.data = ["Setosa", "Versicolor", "Virginica"]
		self.cboVariety.addItems(self.data)


	def guardar(self):
		sl=self.dspSL.value()
		sw=self.dsbSW.value()
		pl=self.dsbPL.value()
		pw=self.dsbPW.value()
		variety=self.cboVariety.currentText()

		print('sl ' + str(sl) + ' sw ' + str(sw) + ' pl ' + str(pl) + ' pw ' + str(pw) + ' cbo ' + str(variety))

		print(type(self.table))
		#segunda idea
		self.table.updateCSV(self.row)

		self.close()

	def recuperaDatos(self):
		datos=[self.dspSL.value(),self.dsbSW.value(),self.dsbPL.value(),self.dsbPW.value(),self.cboVariety.currentText()]

		return datos

	def cerrar(self):
		self.close()

	def loadValues(self, sl, sw, pl, pw, variety):
		errorMsg=''

		slValue = float(sl)
		if slValue>=self.dspSL.minimum() and slValue<=self.dspSL.maximum():
			self.dspSL.setValue(slValue)
		else:
			errorMsg += 'Sepal length fuera de los limites. '


		swValue = float(sw)
		if swValue>=self.dsbSW.minimum() and swValue<=self.dsbSW.maximum():
			self.dsbSW.setValue(swValue)
		else:
			errorMsg += 'Sepal width fuera de los limites. '


		plValue = float(pl)
		if plValue>=self.dsbPL.minimum() and plValue<=self.dsbPL.maximum():
			self.dsbPL.setValue(plValue)
		else:
			errorMsg += 'Petal length fuera de los limites. '


		pwValue = float(pw)
		if pwValue>=self.dsbPW.minimum() and pwValue<=self.dsbPW.maximum():
			self.dsbPW.setValue(pwValue)
		else:
			errorMsg += 'Petal width fuera de los limites. '


		if variety in self.data:
			self.cboVariety.setCurrentText(variety)
		else:
			errorMsg += 'El elemento no corresponde a una variedad valida. '


		if errorMsg!='':
			print(errorMsg)


def main():
	app = QtWidgets.QApplication(sys.argv)	
	
	form = clsForm()
	form.show()
	app.exec_()

if __name__ == '__main__':
	main()