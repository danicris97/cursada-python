import random

def generaListaPrioridad(lista):
    dic_prioridad={}
    
    for i in range(len(lista)):
        dic_prioridad[lista[i]]=random.randint(1,100)

    return dic_prioridad

def llenaMochilaPrioridad(lista):
    mochila_llena={}
    lista_con_prioridad={}

    lista_con_prioridad=generaListaPrioridad(lista)
    print("orden de prioridades: " + str(lista_con_prioridad))

    capacidad=random.randint(80,200)
    print("mochila de capacidad: " + str(capacidad))
    controlador=0

    for i in lista_con_prioridad:
        if(lista_con_prioridad[i]>=80 and controlador+i<capacidad):
            mochila_llena[i]=lista_con_prioridad[i]
            controlador=controlador+i

    print("peso actual: " + str(controlador))
    print("mochila actual: " + str(mochila_llena))

    for i in lista_con_prioridad:
        if(lista_con_prioridad[i]<80 and (controlador+i)<capacidad):
            mochila_llena[i]=lista_con_prioridad[i]
            controlador=controlador+i

    print("peso final: " + str(controlador))

    return mochila_llena

listaPeso=[]

tam=random.randint(2,30)
for i in range(tam):
    listaPeso.append(random.randint(5,50))

print("lista de libros: " + str(listaPeso))

mochila={}
mochila=llenaMochilaPrioridad(listaPeso)

print("mochila final: ")
print(mochila)