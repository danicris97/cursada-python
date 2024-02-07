import clsDocumento as documento

if __name__=='__main__':
    a=documento.clsDocumento("archivo",".txt")
    a.abreArchivo()
    print("cantidad de palabras: " + str(a.getCantPalabras()))
    a.cierraArchivo()

    a.abreArchivo()
    print("cantidad de lineas: " + str(a.getCantDeLineas()))
    a.cierraArchivo()

    a.abreArchivo()
    print("tamaño del archivo: " + str(a.getTamArchivo()) + " bytes")
    a.cierraArchivo()

    a.abreArchivo()
    print("cantidad de caracteres: " + str(a.getCantDeCaracteres()))
    a.cierraArchivo()

    
    a.abreArchivo()
    print("cantidad de numeros: " + str(a.getCantNumeros()))
    a.cierraArchivo()

    a.abreArchivo()
    print("diccionario: " + str(a.getFrecuenciaPalabras()))
    a.cierraArchivo()

    b=documento.clsDocumento("TP 2/ejercicios/ejercicio_9/objetos",".txt")
    b.abreArchivo()
    print("tamaño de archivo b: " + str(b.getTamArchivo()) + " bytes")
    b.cierraArchivo()

    b.abreArchivo()
    print("cantidad de numeros: " + str(b.getCantNumeros()))
    b.cierraArchivo()

    b.abreArchivo()
    print("diccionario: " + str(b.getFrecuenciaPalabras()))
    b.cierraArchivo()

    c=documento.clsDocumento("TP 2/ejercicios/ejercicio_9/objetos",".html")
    c.abreArchivo()
    print("tamaño de archivo c: " + str(c.getTamArchivo()) + " bytes")
    c.cierraArchivo()

    c.abreArchivo()
    print("cantidad de lineas: " + str(c.getCantDeLineas()))
    c.cierraArchivo()