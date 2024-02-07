import random

def union(listaA,listaB):
    resultado=[]
    for x in listaA:
        resultado.append(x)
    
    for x in listaB:
        if not x in resultado:
            resultado.append(x)
    
    return resultado

m=random.randint(1,15)
n=random.randint(1,15)

a=[]
b=[]

for i in range(m):
    a.append(random.randint(-100,100))

for i in range(n):
    b.append(random.randint(-100,100))

print("lista a: " + str(a))
print("lista b: " + str(b))
print("union a y b: " + str(union(a,b)))