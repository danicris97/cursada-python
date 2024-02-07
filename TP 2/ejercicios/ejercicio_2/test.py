import clsComplejo as complejo
import random

if __name__=='__main__':
    complejoA=complejo.clsComplejo(random.randint(-100,100),random.randint(-100,100))
    print("A = " + complejoA.toString())
    complejoB=complejo.clsComplejo(random.randint(-100,100),random.randint(-100,100))
    print("B = " + complejoB.toString())
    resultado=complejo.clsComplejo()

    resultado.sumaComplejo(complejoA,complejoB)
    print("suma Resultado = " + resultado.toString())

    resultado.conjugadoComplejo(complejoA)
    print("conjugado Resultado = " + resultado.toString())

    resultado.restaComplejo(complejoA,complejoB)
    print("resta Resultado = " + resultado.toString())

    escalar=random.randint(-10,10)
    print(escalar)
    resultado.productoEscalar(complejoA,escalar)
    print("producto escalar Resultado = " + resultado.toString())

    resultado.productoComplejo(complejoA,complejoB)
    print("producto Resultado = " + resultado.toString())

    resultado.divisionComplejo(complejoA,complejoB)
    print("division Resultado = " + resultado.toString())