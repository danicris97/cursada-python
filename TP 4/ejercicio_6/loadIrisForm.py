from PyQt5 import QtCore, QtWidgets, uic

import sys

import clsIrisF
import clsIrisTypeF

from multipledispatch import dispatch

class clsIrisForm(QtWidgets.QMainWindow):
    @dispatch()
    def __init__(self):
        super(clsIrisForm, self).__init__()
        uic.loadUi('TP 4/ejercicio_6/form.ui',self)

        self.objIris =  clsIrisF.clsIris()
        self.objIrisType = clsIrisTypeF.clsIrisType()
        
        self.setupUiComponents()

    @dispatch(float,float,float,float,str,int)
    def __init__(self,sl,sw,pl,pw,variety,ID):
        super(clsIrisForm, self).__init__()
        uic.loadUi('TP 4/ejercicio_6/form.ui',self)

        self.objIris =  clsIrisF.clsIris()
        self.objIrisType = clsIrisTypeF.clsIrisType()
        self.ID=ID
        
        self.setupUiComponents(sl,sw,pl,pw,variety)

    @dispatch()
    def setupUiComponents(self):
        self.btnGuardar.clicked.connect(self.insert)
        self.btnCerrar.clicked.connect(self.close)

        self.data = self.getComboList()
        self.cboVariety.addItems(self.data)

    @dispatch(float,float,float,float,str)
    def setupUiComponents(self,sl,sw,pl,pw,variety):
        self.btnGuardar.clicked.connect(self.update)
        self.btnCerrar.clicked.connect(self.close)

        self.data = self.getComboList()
        self.cboVariety.addItems(self.data)

        self.dspSL.setValue(sl)
        self.dsbSW.setValue(sw)
        self.dsbPL.setValue(pl)
        self.dsbPW.setValue(pw)
        self.cboVariety.setCurrentText(variety)

    def getComboList(self):     
        result = self.objIrisType.getData()

        comboList=[]
        for elem in result:
            comboList.append(str(elem[1]) + ":" + str(elem[0]))        
        return comboList


    def getidDataType(self,elem):
        value = -1

        if (elem!=''):
            aux = elem.split(':')
            value = int(aux[1])

        return value

    def insert(self):
        try:
            sl=float(self.dspSL.value())
            sw=float(self.dsbSW.value())
            pl=float(self.dsbPL.value())
            pw=float(self.dsbPW.value())
            variety=int(self.getidDataType(self.cboVariety.currentText()))
            
            self.objIris.insert(sl,sw,pl,pw,variety)

            print (str(sl) + ' ' + str(sw) + ' ' + str(pl) + ' ' + str(pw) + ' ' + str(variety))            
            
            print('Exito. Insercion correcta')

            self.hide()
        
        except Exception as e:
            print('Error en la insercion ' + str(e))
            traceback.print_exception(*exc_info)


    def update(self):
        try:
            sl=float(self.dspSL.value())
            sw=float(self.dsbSW.value())
            pl=float(self.dsbPL.value())
            pw=float(self.dsbPW.value())
            variety=int(self.getidDataType(self.cboVariety.currentText()))
            
            self.objIris.update(self.ID,sl,sw,pl,pw,variety)

            print("actualizacion correcta")

            self.hide()
        except:
            print("Error al actualizar datos")

    def close(self):
        self.hide()


def main():
    app = QtWidgets.QApplication(sys.argv)
    
    form = clsIrisForm()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
