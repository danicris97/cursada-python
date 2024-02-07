
class clsEntero:

    def __init__(self,numero):
        self.__numero=numero

    def getNumero(self):
        return self.__numero

    def setNumero(self,numero):
        self.__numero=numero

    def esPar(self):
        if (self.getNumero()%2)==0:
            return True
        else:
            return False

    def devuelveDivisores(self):
        divisores=[]
        aux=abs(self.getNumero())

        for i in range(1,aux):
            if(aux%i==0):
                divisores.append(i)
        divisores.append(aux)

        return divisores

    def mcd(self,operando2):
        if(abs(self.getNumero())>abs(operando2.getNumero())):
            a=abs(self.getNumero())
            b=abs(operando2.getNumero())
        else:
            b=abs(self.getNumero())
            a=abs(operando2.getNumero())

        while(b!=0 and a%b!=0):
            aux=a
            a=b
            b=aux%b

        if(b==0):
            return abs(self.getNumero())
        else:
            return b

    def mcm(self,operando2):
        return ((self.getNumero()*operando2.getNumero())//self.mcd(operando2))