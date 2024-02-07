from asyncore import write
from PyQt5 import QtWidgets, uic

import sys

class clsForm(QtWidgets.QMainWindow):
	def __init__(self, n=None,a=None,e=None,dni=None,lu=None,p=None,r=None,tf=None,c=None,table=None,row=None):
		super(clsForm, self).__init__()
		uic.loadUi('TP 3/ejercicios/ejercicio_4/csvForm.ui',self)
		self.table=table

		self.setupUi()
		
		if n!=None and a!=None and e!=None and dni!=None and lu!=None and p!=None and r!=None and tf!=None and c!=None:
			self.loadValues(n,a,e,dni,lu,p,r,tf,c)

		if row!=None:
			self.row=row


	def setupUi(self):
		self.btnGuardar.clicked.connect(self.guardar)
		self.btnCerrar.clicked.connect(self.cerrar)

		self.data = ["Regularizó", "Nunca asistió", "Abandonó", "No Regularizó"]
		self.cboVariety.addItems(self.data)


	def guardar(self):
		self.table.updateCSV(self.row)
		self.close()

	def recuperaDatos(self):
		apellido=self.textApellido.toPlainText()
		nombre=self.textNombre.toPlainText()
		email=self.textEmail.toPlainText()
		dni=self.textDNI.toPlainText()
		lu=self.textLU.toPlainText()
		parcial=self.textParcial.toPlainText()
		recuperatorio=self.textRecu.toPlainText()
		tfinal=self.textTFinal.toPlainText()
		condicion=self.cboVariety.currentText()
		datos=[apellido,nombre,email,dni,lu,parcial,recuperatorio,tfinal,condicion]

		return datos

	def cerrar(self):
		self.close()

	def loadValues(self,n,a,e,dni,lu,p,r,tf,c):
		errorMsg=''

		self.textApellido.setText(a)
		self.textNombre.setText(n)
		self.textEmail.setText(e)
		self.textDNI.setText(dni)
		self.textLU.setText(lu)

		valor = int(p)
		if valor>=0 and valor<=100:
			self.textParcial.setText(p)
		else:
			errorMsg += 'Sepal length fuera de los limites. '


		valor = int(r)
		if valor>=0 and valor<=100:
			self.textRecu.setText(r)
		else:
			errorMsg += 'Sepal width fuera de los limites. '


		valor = int(tf)
		if valor>=0 and valor<=100:
			self.textTFinal.setText(tf)
		else:
			errorMsg += 'Petal length fuera de los limites. '

		if c in self.data:
			self.cboVariety.setCurrentText(c)
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