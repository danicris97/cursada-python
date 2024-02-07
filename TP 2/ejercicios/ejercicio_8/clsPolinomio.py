import clsMonomio as monomio

class Polinomio:
    def __init__(self):
        self.__listaMonomios=[]
        self.__grado=0
    
    def cargaPolinomio(self):
        s=input("ingrese un polinomio: ")
        s=list(s)

        #carga grado
        for i in range(len(s)):
            if(s[i-1]=="*" and s[i]!="*"):
                if(int(s[i])>self.getGrado()):
                    self.setGrado(int(s[i]))

        #prototipo
        # i=0
        # while i<len(s) and s[i]!="*":
        #     i=i+1

        # if(s[i]=="*"):
        #     self.__grado=int(s[i+2])

        # print(self.__grado)
        # aux=""
        # for i in range(len(s)):
        #     if(s[i]!="x" and s[i]!="*" and s[i]!="+"):
        #         if(i==0):
        #             aux+=s[i]
        #         elif(s[i-1]!="*"):
        #             aux+=s[i]
        #     if(s[i]=="x"):
        #         self.__listaMonomios.append(int(aux))
        #         aux=""

        # self.__listaMonomios.append(int(aux))

        #cargar polinomio
        aux=""
        for i in range(len(s)):
            if(s[i]!="x" and s[i]!="*" and s[i]!="+"):
                if(i==0):
                    aux+=s[i]
                elif(s[i-1]!="*"):
                    aux+=s[i]
            if(s[i]=="x"):
                try:
                    self.__listaMonomios.append(monomio.clsMonomio(int(aux),int(s[i+3])))
                    aux=""
                except:
                    None

        self.__listaMonomios.append(monomio.clsMonomio(int(aux),0))       

    def getListaMonomios(self):
        return self.__listaMonomios

    def setListaMonomios(self,lista):
        self.__listaMonomios=lista

    def setMonomio(self,monomio):
        self.__listaMonomios.append(monomio)

    def setGrado(self,grado):
        self.__grado=grado

    def getGrado(self):
        return self.__grado

    def evaluarEnX(self,x):
        acomulador=0
        aux=self.getListaMonomios()
        for i in range(len(aux)):
            acomulador=aux[i].getCoeficiente*pow(x,aux[i].getExponente())

        return acomulador

    def ruffini(self,polinomio,binomio):
        a=binomio.getListaMonomios()[1].getCoeficiente()
        if(binomio.getGrado()==1 and a<0):
            listaCoeficientes=[]
            listaCoeficientes.append(polinomio.getListaMonomios()[0].getCoeficiente())
            aux=polinomio.getGrado()
            for i in range(1,len(polinomio.getListaMonomios())):
                aux=aux-polinomio.getListaMonomios()[i].getExponente()
                if(aux>1):
                    for j in range(aux):
                        listaCoeficientes.append(0)

                listaCoeficientes.append(polinomio.getListaMonomios()[i].getCoeficiente())
                aux=polinomio.getListaMonomios()[i].getExponente()

            self.setMonomio(monomio.clsMonomio(listaCoeficientes[0],polinomio.getGrado()-1))
            a=a*listaCoeficientes[0]
            for i in range(polinomio.getGrado()-1):
                self.setMonomio(monomio.clsMonomio(listaCoeficientes[i]+a),polinomio.getGrado()-i-1)
                a=a*listaCoeficientes[i]

            return listaCoeficientes[i]+a
        else:
            print("Error en el ingreso del binomio")

    def sumaPolimonio(self,a,b):
        aux=[]
        aux=(a.getListaMonomios().extend(b.getListaMonomios()))
        if(a.getGrado()>=b.getGrado()):
            self.setGrado(a.getGrado())
        else:
            self.setGrado(b.getGrado())

        i=0
        while i<=len(aux):
            j=i+1
            while j<=len(aux)-1:
                if(aux[i].getExponente()==aux[j].getExponente()):
                    aux[i].setCoeficiente(aux[i].getCoeficiente()+aux[j].getCoeficiente())
                    aux.pop(j)
            
        self.setListaMonomios(aux)

    def productoPolimonio(self,a,b):
        None