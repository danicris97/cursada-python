class clsComplejo:
    def __init__(self,real=0,imaginario=0):
        self.__real=real
        self.__imaginario=imaginario

    def getReal(self):
        return self.__real

    def getImaginario(self):
        return self.__imaginario

    def setReal(self,real):
        self.__real=real

    def setImaginario(self,imaginario):
        self.__imaginario=imaginario

    def sumaComplejo(self,objA,objB):
        self.setReal(objA.getReal()+objB.getReal())
        self.setImaginario(objA.getImaginario+objB.getImaginario())

    def restaComplejo(self,objA,objB):
        self.setReal(objA.getReal()-objB.getReal())
        self.setImaginario(objA.getImaginario()-objB.getImaginario())

    def productoEscalar(self,objA,escalar):
        self.setReal(objA.getReal()*escalar)
        self.setImaginario(objA.getImaginario()*escalar)

    def productoComplejo(self,objA,objB):
        self.setReal(objA.getReal()*objB.getReal()-objA.getImaginario()*objB.getImaginario)
        self.setImaginario(objA.getReal()*objB.getImaginario()-objA.getImaginario()*objB.getReal())