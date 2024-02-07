def inputString():
    cadena=input("ingrese una cadena: ")
    return cadena

def convertToAscii(cadena):
    for i in cadena:
        print(i + " = " + str(ord(i)))

def convertToList(cadena):
    lista=[]
    tam=len(cadena)

    for i in range(0,tam):
        lista.append(ord(cadena[i]))

    return lista

s=inputString()
print(s[0])
convertToAscii(s)
ascii=convertToList(s)

print(ascii)