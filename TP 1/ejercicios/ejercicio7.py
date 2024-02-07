import random

def sumaMatrices(matrizA,matrizB):
    if((len(matrizA)==(len(matrizB[0])))):
        resultado=[]
        for i in range(len(matrizA[0])):
            resultado.append([])
            for j in range(len(matrizA)):
                resultado[i].append((matrizA[i][j]+matrizB[i][j]))

        return resultado
    else:
        print("las matrices son de distinto orden")

n=random.randint(1,5)

def matrizRandom(m,n):
    matriz=[]
    for i in range(m):
        matriz.append([])
        for j in range(n):
            matriz[i].append(random.randint(1,10))

    return matriz

def muestraMatriz(matriz):
    for linea in matriz:
        for elemento in linea:
            print(str(elemento),end=" ")
        print()

a=matrizRandom(n,n)
b=matrizRandom(n,n)

print("matriz a: ")
muestraMatriz(a)
print("matriz b: ")
muestraMatriz(b)

suma=sumaMatrices(a,b)
print("suma a+b: ")
muestraMatriz(suma)