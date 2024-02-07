class clsDocumento:
    def __init__(self,direccion,tipo):
        self.__direccion=direccion
        self.__tipo=tipo
        self.__archivo=None
    
    def setDireccion(self,direccion):
        self.__direccion=direccion

    def getDireccion(self):
        return self.__direccion

    def setTipo(self,tipo):
        self.__tipo=tipo

    def getTipo(self):
        return self.__tipo

    def abreArchivo(self):
        self.__archivo=open(self.getDireccion()+self.getTipo(),"r")

    def cierraArchivo(self):
        self.__archivo.close()

    def getCantPalabras(self):
        aux=self.__archivo.read()
        palabras=aux.split()
        return len(palabras)

    def getCantDeLineas(self):
        aux=self.__archivo.readlines()

        return len(aux)

    def getTamArchivo(self):
        aux=self.__archivo.read()

        return len(aux)

    def getCantNumeros(self):
        aux=self.__archivo.read()
        palabras=aux.split()
        numeros=0

        for i in range(len(palabras)):
            aux=list(palabras[i])
            for j in range(len(aux)):
                if(ord(aux[j])>46 and ord(aux[j])<58):
                    numeros+=1

        return numeros

    def getCantDeCaracteres(self):
        aux=self.__archivo.read()
        palabras=aux.split()
        caracteres=0

        for i in range(len(palabras)):
            caracteres+=len(list(palabras[i]))

        return caracteres

    def getFrecuenciaPalabras(self):
        frecuencia={}
        aux=self.__archivo.read()
        palabras=aux.split()

        for i in range(len(palabras)):
            p=palabras[i]
            if p in frecuencia:
                frecuencia[p]=frecuencia[p]+1
            else:
                frecuencia[p]=1

        return frecuencia