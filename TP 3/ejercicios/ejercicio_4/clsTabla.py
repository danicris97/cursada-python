import sys
import csv
import shutil
from PyQt5 import QtCore,QtWidgets,uic
import clsForm as loadForm

class clsTabla(QtWidgets.QMainWindow):
    def __init__(self, nombreArchivo, parent=None):
        super(clsTabla,self).__init__(parent)

        uic.loadUi("TP 3/ejercicios/ejercicio_4/tabla.ui",self)

        self.nombreArchivo=nombreArchivo
        self.archivoAux="TP 3/ejercicios/ejercicio_4/temporary.csv"
        self.setUiComponents()

    def setUiComponents(self):
        self.tblData.resizeColumnsToContents()
        self.tblData.resizeRowsToContents()
        self.tblData.doubleClicked.connect(self.loadForm)

        self.loadTabla()
        self.btnGuardar.clicked.connect(self.guardarCSV)
        self.btnCerrar.clicked.connect(self.cerrar)

    def guardarCSV(self):
        rows = self.tblData.rowCount()
        cols = self.tblData.columnCount()
        
        newList=[]
        for i in range(rows):
            auxList = []
            for j in range(cols):
                cell = self.tblData.item(i, j).text()
                auxList.append(cell)
                
            newList.append(auxList)
        with open(self.archivoAux, 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
            writer.writerows(newList)
        
        shutil.move(self.archivoAux, self.nombreArchivo)
        self.loadTabla()

    def cerrar(self):
        self.close()

    def loadTabla(self):
        archivo=open(self.nombreArchivo,"r")
        try:
            reader=csv.reader(archivo,delimiter=",")
            
            rowI=0
            for row in reader:
                self.tblData.setRowCount(rowI+1)

                if rowI==0:
                    columns=len(row)
                    self.tblData.setColumnCount(columns)

                columns = len(row)
                for columnJ in range(columns):
                    myValue = row[columnJ]
                    cell=QtWidgets.QTableWidgetItem(str(myValue))
                    self.tblData.setItem(rowI,columnJ,cell)

                rowI=rowI+1
        finally:
            archivo.close()

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def loadForm(self,index):
        
        column = index.column()
        if column ==8:
            row = index.row()			
            n = self.tblData.item(row, 0).text()
            a = self.tblData.item(row, 1).text()
            e = self.tblData.item(row, 2).text()
            dni = self.tblData.item(row, 3).text()
            lu = self.tblData.item(row, 4).text()
            p = self.tblData.item(row, 5).text()
            r = self.tblData.item(row, 6).text()
            tf = self.tblData.item(row, 7).text()
            c = self.tblData.item(row, 8).text()
            self.w = loadForm.clsForm(n,a,e,dni,lu,p,r,tf,c,self,row)
            self.w.show()
            #self.w.btnGuardar.clicked.connect(lambda: self.updateCSVFila(row))

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
                
                newList.append(auxList)
                
        with open(self.archivoAux, 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
            writer.writerows(newList)
        
        shutil.move(self.archivoAux, self.nombreArchivo)
        self.loadTabla()

def main():
    app = QtWidgets.QApplication(sys.argv)

    archivo="TP 3/ejercicios/ejercicio_4/estudiantes.csv"

    objeto=clsTabla(archivo)
    objeto.show()
    app.exec_()

if __name__=="__main__":
    main()