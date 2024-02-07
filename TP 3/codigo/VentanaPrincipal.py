import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from  DateDialog import DateDialog

class WinForm(QWidget):
    def __init__(self,parent=None):
        super(WinForm, self).__init__(parent)
        self.resize(400,90)
        self.setWindowTitle('Ejemplo de devolver el valor a la ventana principal cuando el diálogo está cerrado')

        self.lineEdit=QLineEdit(self)
        self.button1=QPushButton('Cuadro de diálogo emergente 1')
        self.button1.clicked.connect(self.onButton1Clicked)

        self.button2=QPushButton('Cuadro de diálogo emergente 2')
        self.button2.clicked.connect(self.onButton2Clicked)

        gridLayout=QGridLayout(self)
        gridLayout.addWidget(self.lineEdit)
        gridLayout.addWidget(self.button1)
        gridLayout.addWidget(self.button2)

    def onButton1Clicked( self ):
        dialog=DateDialog(self)
        result=dialog.exec_()
        date=dialog.dateTime()
        self.lineEdit.setText(date.date().toString())
        print('\ nVolver el valor del diálogo de fecha')
        print('date=%s'%str(date.date))
        print('time=%s'%str(date.time()))
        print('result=%s'%result)
    def onButton2Clicked( self ):
        date,time,result=DateDialog.getDateTime()
        self.lineEdit.setText(date.toString())
        print('\ n Valor de retorno del diálogo de fecha')
        print('date=%s' %str(date))
        print('time=%s' %str(time))
        print('result=%s' %result)





if __name__ == '__main__':
    app=QApplication(sys.argv)
    form=WinForm()
    form.show()
    sys.exit(app.exec_())