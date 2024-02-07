lista = ['a','b','c','d']

for x in lista:
    print(x)

x='z'
lista.append(x)

print(lista)
print(str(lista))

pos=3
del(lista[pos])

print(lista)

print(str(len(lista)))

elemento='u'
if elemento in lista:
    print("si esta en la lista")
else:
    print("el numero no esta en la lista")
    lista.append(elemento)