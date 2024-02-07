from PyQt5 import QtCore, QtWidgets, uic


import sys
import clsIrisF
import clsIrisTypeF

#https://stackoverflow.com/questions/59960494/pyqt5-recursionerror-maximum-recursion-depth-exceeded-while-calling-a-python-o
# como salvar recursion x ventanas que se llaman


class clsIrisForm(QtWidgets.QMainWindow):
    def __init__(self):
        super(clsIrisForm, self).__init__()
        uic.loadUi('TP 4/codigo/form.ui',self)

        
        self.objIris =  clsIrisF.clsIris()
        self.objIrisType = clsIrisTypeF.clsIrisType()
        
        self.setupUiComponents()

               

    def setupUiComponents(self):
        self.btnGuardar.clicked.connect(self.insert)
        self.btnCerrar.clicked.connect(self.close)

        self.data = self.getComboList()
        self.cboVariety.addItems(self.data)



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


    def close(self):
        self.hide()


def main():
    app = QtWidgets.QApplication(sys.argv)
    
    form = clsIrisForm()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
