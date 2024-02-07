import random

def transponer(matriz):

    resultado=[]
    for i in range(len(matriz[0])):
        resultado.append([])
        for j in range(len(matriz)):
            resultado[i].append(matriz[j][i])#lista de lista como en arraylist

    return resultado

m=random.randint(1,5)
n=random.randint(1,5)
print("matriz " + str(m) + " x " + str(n))

a=[]
for i in range(m):
    a.append([])
    for j in range(n):
        a[i].append(random.randint(1,10))

#a=[[1,2,3],[4,5,6],[7,8,9]]
t=transponer(a)

print("matriz original: ")
for linea in a:
    for elemento in linea:
        print(str(elemento),end=" ")#para imprimir en la misma lineal end=""
    print()#salto de linea

print("matriz transpuesta: ")
for linea in t:
    for elemento in linea:
        print(str(elemento),end=" ")
    print()