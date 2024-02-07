mi_agenda = {"alicia":2222,"roberto":1111,"lucia":3333,"andres":5555}

for clave in mi_agenda:
    print(clave)

for clave in mi_agenda:
    print(clave, ":", mi_agenda[clave])

vista_claves = mi_agenda.keys()
print(vista_claves)#no es una lista

vista_claves = list(mi_agenda.keys())
print(vista_claves)

for clave in vista_claves:
    print(clave)

print(mi_agenda.values())# no es lista

if 1111 in mi_agenda.values():
    print("ese valor esta en el diccionario")
    print(mi_agenda.get("roberto"))

print(mi_agenda.items())#devuelve tuplas

for elemento in mi_agenda.items():
    print(elemento)

for clave,valor in mi_agenda.items():
    print(clave,valor)