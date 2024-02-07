
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
        self.setImaginario(objA.getImaginario()+objB.getImaginario())

    def restaComplejo(self,objA,objB):
        self.setReal(objA.getReal()-objB.getReal())
        self.setImaginario(objA.getImaginario()-objB.getImaginario())

    def productoEscalar(self,objA,escalar):
        self.setReal(objA.getReal()*escalar)
        self.setImaginario(objA.getImaginario()*escalar)

    def productoComplejo(self,objA,objB):
        real=(objA.getReal()*objB.getReal())-(objA.getImaginario()*objB.getImaginario())
        imaginario=(objA.getReal()*objB.getImaginario())-(objA.getImaginario()*objB.getReal())
        self.setReal(real)
        self.setImaginario(imaginario)

    def divisionComplejo(self,objA,objB):
        self.setReal((objA.getReal()*objB.getReal()+objA.getReal()*objB.getImaginario())/pow(objB.getReal(),2)+pow(objB.getImaginario(),2))
        self.setImaginario((objA.getImaginario()*objB.getReal()+objA.getImaginario()*objB.getReal())/pow(objB.getReal(),2)+pow(objB.getImaginario(),2))
    
    def conjugadoComplejo(self,objA):
        self.setReal(objA.getReal())
        self.setImaginario(objA.getImaginario()*-1)

    def toString(self):
        cadena="" +"("+ str(self.getReal()) +","+ str(self.getImaginario()) + "i)"

        return cadena