import clsEntero as entero
import random

if __name__=='__main__':
    numero=entero.clsEntero(random.randint(-100,100))
    print("primer numero: " + str(numero.getNumero()))
    numero2=entero.clsEntero(random.randint(-100,100))
    print("segundo numero: " + str(numero2.getNumero()))

    print(str(numero.esPar()))
    print(numero.devuelveDivisores())
    print(numero2.devuelveDivisores())
    print(str(numero.mcd(numero2)))
    print(str(numero2.mcd(numero)))
    print(str(numero.mcm(numero2)))
    print(str(numero2.mcm(numero)))