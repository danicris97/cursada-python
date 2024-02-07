class clsMonomio:

    def __init__(self,coeficiente,exponente):
        self.__coeficiente=coeficiente
        self.__exponente=exponente

    def getCoeficiente(self):
        return self.__coeficiente

    def setCoeficiente(self,coeficiente):
        self.__coeficiente=coeficiente

    def getExponente(self):
        return self.__exponente

    def setExponente(self,exponente):
        self.__exponente=exponente

    def toString(self):
        cadena="("
        cadena+=str(self.__coeficiente)+"x"+"**"+str(self.__exponente)
        cadena+=")"
        
        return cadena