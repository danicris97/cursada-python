import random
minimo=1
maximo=7

lista=[22,27,12,90,5]
print(lista)

#agregar un elemento a la lista
x=3242
lista.append(x)
print(lista)

#cantidad de elementos de la lista
print("cantidad de elementos: " + str(len(lista)))

#elimina uno
pos=1
del(lista[pos])
print(lista)

#suma dos elementos
aux=lista[0]+lista[1]
print(aux)

#asigna elemento en posicion
pos=2
ele=4
lista[pos]=ele
print(lista)

#comprueba si existe y agrega a la lista un elemento 
ele=4
if ele in lista:
    print("el elemento " + str(ele) + ", esta en la lista")
else:
    print("el elemento " + str(ele) + ", no esta en la lista")
    lista.append(ele)
print(lista)

#mostrar lista
print(lista)