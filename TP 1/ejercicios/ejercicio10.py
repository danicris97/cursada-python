import random

def cargarMochila(lista):
    mochila_cargada=[]
    capacidad=random.randint(80,150)
    print("capacidad: " + str(capacidad))
    peso_actual=0

    tam=len(lista)
    i=0
    while(i<tam):
        if(peso_actual+lista[i]<capacidad):
            men=51
            c=0
            for j in range(i,len(lista)):
                if(lista[j]<men):
                    men=lista[j]
                    c=j

            mochila_cargada.append(men)
            peso_actual=peso_actual+men
            del(lista[c])
            tam=tam-1
        i=i+1

    return mochila_cargada,peso_actual

listaPeso=[]

tam=random.randint(2,30)
for i in range(tam):
    listaPeso.append(random.randint(5,50))

print("lista de libros: " + str(listaPeso))

mochila,peso=cargarMochila(listaPeso)
print("mochila cargada: ")
print(mochila)
print("peso final: " + str(peso))