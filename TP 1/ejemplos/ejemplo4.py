minimo=int(input("ingrese minimo: "))
maximo=int(input("ingrese maximo: "))


if minimo<=maximo:
    for x in range(minimo,maximo+1):
        if x%2==0:
            print("par " + str(x))
        else:
            print("impar " + str(x))
else:
    print("indeterminado")

