
import clsConexionF 

class clsIris:
        def __init__(self):
                self.bd=clsConexionF.clsConexion()

        def getData(self):
                query = "SELECT idEstudianteC,Estudiante.apellido,Estudiante.nombre,lu,anio,CondEstudiante.descripcion,ConCursado.descripcion,EstadoTPF.descripcion, p1,rp1,p2,rp2 FROM EstudianteC INNER JOIN Estudiante USING(lu) INNER JOIN Cohorte USING (idCohorte) INNER JOIN CondEstudiante USING (idCondE) INNER JOIN ConCursado USING (idCondC)INNER JOIN EstadoTPF USING(idEstadoTPF);"
                result = self.bd.run_query(query)

                if (len(result)==0):
                        return None
                else:
                        return result


        def insert(self, lu, anio, condE, condC, estTPF, p1, rp1, p2, rp2):
                query = "INSERT INTO EstudianteC (lu, idCohorte, idCondC, idCondE, idEstadoTPF, p1, rp1, p2, rp2) VALUES ('%d','%d','%d','%d','%d','%s','%s','%s','%s');"%(lu,anio,condE,condC,estTPF,p1,rp1,p2,rp2)          
                self.bd.run_query(query)

        def delete(self, ID):
                query = "DELETE FROM EstudianteC WHERE id= " + str(ID) + ";"
                self.bd.run_query(query)

        def update(self, ID, sepalL, sepalW, petalL, petalW, idT):
                query = "UPDATE iris SET sepalLength ='%s', sepalWidth='%s', petalLength='%s', petalWidth='%s', idType='%d' WHERE id = '%d';"%(sepalL, sepalW, petalL, petalW, idT, ID)  
                self.bd.run_query(query)

        def getLogin(self):
                query= "SELECT `idUsuario`,`apellido`,`nombre`,`password` FROM Usuario;"
                result = self.bd.run_query(query)

                if(len(result)==0):
                        None
                else:
                        return result