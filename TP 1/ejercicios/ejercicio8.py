import random

def determinaFrecuencia(img):
    
    frecuencia={}

    for i in range(len(img)):
        for j in range(len(img[0])):
            num=img[i][j]
            if num in frecuencia:
                frecuencia[num]=frecuencia[num]+1
            else:
                frecuencia[num]=1

    return frecuencia



def matrizRandom(m,n):
    matriz=[]
    for i in range(m):
        matriz.append([])
        for j in range(n):
            matriz[i].append(random.randint(0,255))

    return matriz


def muestraMatriz(matriz):
    for linea in matriz:
        for elemento in linea:
            print(str(elemento),end=" ")
        print()

m=random.randint(2,10)
n=random.randint(2,10)

img=matrizRandom(m,n)
muestraMatriz(img)

print(determinaFrecuencia(img))