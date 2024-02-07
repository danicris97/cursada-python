import random
minimo=1
maximo=100
contador=-1
lista=[]

for i in range(0,5):
    lista.append(random.randint(minimo,maximo))
print(lista)

min=0
max=10

for i in range(min,max):
    opcion=random.randint(min,max)
    if(opcion==0):
        print("agrega elemento")
        #agregar un elemento a la lista
        x=random.randint(minimo,maximo)
        lista.append(x)
        print(lista)

    if(opcion==1):
        print("cantidad de elementos")
        #cantidad de elementos de la lista
        print("cantidad de elementos: " + str(len(lista)))

    if(opcion==2):
        print("elimina elementos")
        #elimina uno
        pos=random.randint(0,len(lista)-1)
        del(lista[pos])
        print(lista)

    if(opcion==3):
        print("suma dos elementos")
        #suma dos elementos
        aux=lista[random.randint(0,len(lista)-1)]+lista[random.randint(0,len(lista)-1)]
        print(aux)
    if(opcion==4):
        print("asigna elemento en posicion")
        #asigna elemento en posicion
        pos=random.randint(0,len(lista)-1)
        ele=random.randint(minimo,maximo)
        lista[pos]=ele
        print(lista)

    if(opcion==5):
        print("comprueba si existe y agrega")
        #comprueba si existe y agrega a la lista un elemento 
        ele=int(input("ingrese un numero entero: "))
        if ele in lista:
            print("el elemento " + str(ele) + ", esta en la lista")
        else:
            print("el elemento " + str(ele) + ", no esta en la lista")
        lista.append(ele)
        print(lista)

    if(opcion==6):
        print("muestra elemento")
        #mostrar lista
        print(lista)
    
    if(opcion==7):
        print("no pasa nada")