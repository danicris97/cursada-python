import random

def notas(lista):
    notas={}

    for i in range(len(lista)):
        if not lista[i] in notas:
            notas[lista[i]]=random.randint(1,100)

    return notas

def notasRecuperatorio(notas):
    notasR={}

    for clave in notas:
        if notas[clave]>59:
            notasR[clave]=[notas[clave],0]
        else:
            notasR[clave]=[notas[clave],random.randint(1,100)]

    return notasR

l=[]
n=random.randint(1,60)

for i in range(n):
    l.append(random.randint(150000,300000))

print("lista de libretas universitarias: ")
print(l)

dic_notas={}
dic_notas=notas(l)
print("")
print("diccionario de notas primer parcial: ")
print(dic_notas)

print("")
print("diccionario de notas primer parcial + recuperatorio: ")
dic_notas_rec={}
dic_notas_rec=notasRecuperatorio(dic_notas)
print(dic_notas_rec)

print("")
if 221520 in dic_notas_rec.keys():
    print(dic_notas_rec.get("221520"))
else:
    print("no esta inscripto")
if 219946 in dic_notas_rec.keys():
    print(dic_notas_rec.get("219946"))
else:
    print("no esta inscripto")