import string


def divisionE(enteroA,enteroB):
    d=(enteroA//enteroB)
    r=(enteroA%enteroB)

    return d,r

a=int(input("ingrese el valor a: "))
b=int(input("ingrese el valor b b distinto de 0: "))
while(b==0):
    print("ERROR")
    b=int(input("ingrese el valor b b distinto de 0: "))

division,resto = divisionE(a,b) #devuelve una tupla

print(division)
print(resto)