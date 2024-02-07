import random

def divisores(entero):
    lista=[]
    entero=abs(entero)
    for i in range(1,entero+1):
        if(entero%i==0):
            lista.append(i)

    return lista

#a=int(input("ingrese un numero entero: "))
a=random.randint(-100,100)
print(a)
print(divisores(a))