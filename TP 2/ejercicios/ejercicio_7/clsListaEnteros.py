import clsEntero as entero

class clsListaEnteros:
    def __init__(self):
        self.__lista=[]

    def getLista(self):
        return self.__lista

    def setLista(self,lista):
        self.__lista=lista

    def setEntero(self,entero):
        self.__lista.append(entero)

    def agregaNumero(self,numero):
        nuevoEntero=entero.clsEntero(numero)
        self.getLista().append(nuevoEntero)

    def eliminaNumero(self,numero):
        aux=self.getLista()
        for i in aux:
            if aux[i].getNumero()==numero:
                for j in range(i,len(aux)-1):
                    aux[j]=aux[j+1]
                if(i==len(aux)):
                    aux[i]=None
        
        self.setLista(aux)

    def buscaNumero(self,numero):
        aux=self.getLista()
        for i in aux:
            if(aux[i].getNumero()==numero):
                return i
        
        if(i>=len(aux)):
            return -1

    def obtienePares(self,operando):
        aux=operando.getLista()
        for i in aux:
            if(aux[i].esPar()==True):
                self.setEntero(aux[i])

    def obtieneImpares(self,operando):
        aux=operando.getLista()
        for i in aux:
            if(aux[i].esPar()==False):
                self.setEntero(aux[i])

    def obtienePrimos(self,operando):
        aux=operando.getLista()
        for i in aux:
            if(len(aux[i].devuelveDivisores())==2):
                self.setEntero(aux[i])

    def obtieneCompuesto(self,operando):
        aux=operando.getLista()
        for i in aux:
            if(len(aux[i].devuelveDivisores())>2):
                self.setEntero(aux[i])

    def toString(self):
        cadena="["

        for i in range(len(self.__lista)):
            cadena+=str(self.__lista[i].getNumero())+ " , "

        cadena+="]"

        return cadena