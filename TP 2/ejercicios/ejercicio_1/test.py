import clsPersona as persona
import random

if __name__=='__main__':
    personaA=persona.clsPersona(random.randint(1,1000),"perez","nicolas",True,random.randint(0,100))
    personaB=persona.clsPersona(random.randint(1,1000),"rueda","constanza",False,random.randint(0,100))

    if personaA.esMujer():
        print("Es mujer")
    else:
        print("Es hombre")

    if personaB.esMujer():
        print("Es mujer")
    else:
        print("Es hombre")

    if personaA.esMayor():
        print("Es mayor")
    else:
        print("Es menor")

    if personaB.esMayor():
        print("Es mayor")
    else:
        print("Es menor")

    print(personaA.getApellido())
    print(personaA.getNombre())

    print(personaB.getApellido())
    print(personaB.getNombre())