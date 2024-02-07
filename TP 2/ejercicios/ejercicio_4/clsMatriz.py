import random
#mejorar y completar
class clsMatriz:

    def __init__(self,CantFilas,CantColumnas):
        self.__CantFilas=CantFilas
        self.__CantColumnas=CantColumnas
        self.__matriz=self.generaMatrizRandom()

    def setCantFilas(self,CantFilas):
        self.__CantFilas=CantFilas

    def setCantColumnas(self,CantColumnas):
        self.__CantColumnas=CantColumnas

    def getCantFilas(self):
        return self.__CantFilas

    def getCantColumnas(self):
        return self.__CantColumnas

    def getElemento(self,i,j):
        return self.__matriz[i][j]

    def setElemento(self,i,j,elemento):
        self.__matriz[i][j]=elemento

    def generaMatrizRandom(self):
        matriz=[]
        print(str(self.getCantFilas()))
        for i in range(self.getCantFilas()):
            matriz.append([])
            for j in range(self.getCantColumnas()):
               matriz[i].append(random.randint(0,255))

        return matriz

    def muestraMatriz(self):
        for linea in self.__matriz:
            for elemento in linea:
                print(str(elemento),end=" ")
            print()