minimo=10
maximo=25

for x in range(minimo,maximo+1):
    print(x)

for x in range(minimo,maximo+1):
    if x%2==0:
        print("par " + str(x))
    else:
        print("impar " + str(x))