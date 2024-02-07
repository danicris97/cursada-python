import math

class clsFigura:
    def __init__(self):
        pass

    def calculaPerimetro(self):
        return 0

    def calculaArea(self):
        return 0


class clsRectangulo(clsFigura):
    def __init__(self,ladoA,ladoB):
        super().__init__()
        self.__ladoA=ladoA
        self.__ladoB=ladoB

    def getLadoA(self):
        return self.__ladoA

    def getLadoB(self):
        return self.__ladoB

    def calculaPerimetro(self):
        return 2*(self.getLadoA()+self.getLadoB())

    def calculaArea(self):
        return (self.getLadoA()*self.getLadoB())


class clsCuadrado(clsRectangulo):
    def __init__(self, ladoA):
        super().__init__(ladoA,ladoA)


class clsTriagulo(clsFigura):
    def __init__(self,ladoA,ladoB,ladoC):
        super().__init__()
        self.__ladoA=ladoA
        self.__ladoB=ladoB
        self.__ladoC=ladoC

    def getLadoA(self):
        return self.__ladoA

    def getLadoB(self):
        return self.__ladoB

    def getLadoC(self):
        return self.__ladoC

    def calculaPerimetro(self):
        return (self.getLadoA()+self.getLadoB()+self.getLadoC())

    def calculaArea(self):
        s=(self.getLadoA()+self.getLadoB()+self.getLadoC())/2
        return (math.sqrt((s*(s-self.getLadoA())*(s-self.getLadoB())*(s-self.getLadoC()))))


class clsCirculo(clsFigura):
    def __init__(self,radio):
        super().__init__()
        self.__radio=radio

    def getRadio(self):
        return self.__radio

    def calculaPerimetro(self):
        return (2*math.pi*self.getRadio())

    def calculaArea(self):
        return (math.pi*pow(self.getRadio(),2))
