#hecho con tuplas
class clsComplejo2:
    def __init__(self,real=0,imaginario=0):
        self.__complejo=(real,imaginario)

    def getComplejo(self):
        return self.__complejo

    def setComplejo(self,complejo):
        self.__complejo = complejo
    
    def getReal(self):
        return self.__complejo[0]

    def setReal(self,real):
        self.__complejo[0]=real

    def getImaginario(self):
        return self.__complejo[1]

    def setImaginario(self,imaginario):
        self.__complejo[1]=imaginario
#completar las operaciones