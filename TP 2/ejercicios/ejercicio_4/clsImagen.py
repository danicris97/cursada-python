import clsMatriz as matriz

class clsImagen:
    def __init__(self,horizontal,vertical):
        self.__intensidad=matriz.clsMatriz(horizontal,vertical)
        self.__frecuencia={}

    
    def determinaFrecuencia(self):
        for i in range(self.__intensidad.getCantFilas()):
            for j in range(self.__intensidad.getCantColumnas()):
                aux=self.__intensidad.getElemento(i,j)
                if aux in self.__frecuencia:
                    self.__frecuencia[aux]=self.__frecuencia[aux]+1
                else:
                    self.__frecuencia[aux]=1

    def getFrecuencia(self):
        return self.__frecuencia

    def getMatrizIntensidad(self):
        self.__intensidad.muestraMatriz()
        return self.__intensidad