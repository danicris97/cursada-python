import clsEntero as entero
import clsListaEnteros as listaE
import random

if __name__=='__main__':
    numero=entero.clsEntero(random.randint(-100,100))
    print("primer numero: " + str(numero.getNumero()))
    numero2=entero.clsEntero(random.randint(-100,100))
    print("primer numero: " + str(numero2.getNumero()))
    numero3=entero.clsEntero(random.randint(-100,100))
    print("primer numero: " + str(numero3.getNumero()))

    lista=listaE.clsListaEnteros()
    lista.setEntero(numero)
    lista.setEntero(numero2)
    lista.setEntero(numero3)

    print(len(lista.getLista()))
    print(lista.getLista()[0].getNumero())

    print(lista.toString())

    lista.agregaNumero(random.randint(-5,31))
    print(lista.toString())