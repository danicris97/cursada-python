
class clsPersona:
    def __init__(self,id,apellido,nombre,mujer,edad):
        self.__id=id
        self.__apellido=apellido
        self.__nombre=nombre
        self.__mujer=mujer
        self.__edad=edad

    def getId(self):
        return self.__id
    
    def setId(self,id):
        self.__id=id

    def getApellido(self):
        return self.__apellido
    
    def setApellido(self,apellido):
        self.__apellido=apellido
    
    def getNombre(self):
        return self.__nombre

    def setNombre(self,nombre):
        self.__nombre=nombre

    def esMujer(self):
        return self.__mujer

    def setMujer(self,mujer):
        self.__mujer=mujer

    def getEdad(self):
        return self.__edad

    def setEdad(self,edad):
        self.__edad=edad

    def esMayor(self):
        if self.getEdad()>=18:
            return True
        else:
            return False

    def esMayorQue(self,otro):
        if self.getEdad()>otro.getEdad():
            return True
        else:
            return False