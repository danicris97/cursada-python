class clsAnimal:
    def __init__(self,vive):
        self.__vive=vive

    def estaVivo(self):
        return self.__vive
        
class clsCabra(clsAnimal):
    def __init__(self,vive,cola):
        super().__init__(vive)
        self.__cola=cola

    def ordeniar(self):
        print("ordeniando")

    def saltar(self):
        print("saltando")

class clsCerdo(clsAnimal):
    def __init__(self,vive,hocico):
        super().__init__(vive)
        self.__hocico=hocico

    def comer(self,comida):
        print("comiendo")

    def revolcarse(self):
        print("revolcandose")

class clsCaballo(clsAnimal):

    def __init__(self,vive,altura,color):
        super().__init__(vive)
        self.__altura=altura
        self.__color=color

    def correr(self):
        print("corriendo")

    def saltar(self):
        print("saltando")

class clsCorredor(clsCaballo):
    
    def __init__(self,vive,altura,color):
        super().__init__(vive,altura,color)


    def compertir(self):
        print("compitiendo")

class clsEcuestre(clsCaballo):

    def __init__(self,vive,altura,color,peso):
        super().__init__(vive,altura,color)
        self.__peso=peso

    def trotar(self):
        print("trotando")

    def getPeso(self):
        return self.__peso

    def estaEntrenado(self):
        if(self.getPeso()>380 and self.getPeso()<550):
            return True
        else:
            return False