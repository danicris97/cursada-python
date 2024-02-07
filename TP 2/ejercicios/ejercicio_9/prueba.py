#from io import open

#abrir para escribir
archivo_texto=open("archivo.txt","w")
texto="hola mundo en archivo txt desde python \n tambien en html"
archivo_texto.write(texto)
archivo_texto.close()

#abrir para leer
archivo_texto=open("archivo.txt","r")
#contenido=archivo_texto.read()
lista=archivo_texto.readlines()
archivo_texto.close()
#print(contenido)
print(lista)