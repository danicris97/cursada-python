import random
##from traceback import print_stack

minimo=int(input("ingrese un minimo: "))
maximo=int(input("ingrese un maximo: "))

x=random.randint(minimo,maximo)

print(x)

while x%2!=0:
    x = random.randint(minimo,maximo)
    print(x)

print ("numero: " + str(x))