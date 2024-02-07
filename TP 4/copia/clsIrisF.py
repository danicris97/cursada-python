
import clsConexionF 

class clsIris:
        def __init__(self):
                self.bd= clsConexionF.clsConexion()

        def getData(self):
                #query = "SELECT * FROM iris;"
                query = "SELECT iris.id, iris.sepalLength, iris.sepalWidth, iris.petalLength, iris.petalWidth, iris.idType, iristype.description FROM iris INNER JOIN iristype ON iris.idType=iristype.id;"
                result = self.bd.run_query(query)

                if (len(result)==0):
                        return None
                else:
                        return result


        def insert(self, sepalL, sepalW, petalL, petalW, idT):
                query = "INSERT INTO iris (sepalLength, sepalWidth, petalLength, petalWidth, idType) VALUES ('%s','%s','%s','%s','%d');"%(sepalL, sepalW, petalL, petalW, idT)          
                self.bd.run_query(query)


        def delete(self, ID):
                query = "DELETE FROM iris WHERE id= " + str(ID) + ";"
                self.bd.run_query(query)

        def update(self, ID, sepalL, sepalW, petalL, petalW, idT):
                query = "UPDATE iris SET sepalLength ='%s', sepalWidth='%s', petalLength='%s', petalWidth='%s', idType='%d' WHERE id = '%d';"%(sepalL, sepalW, petalL, petalW, idT, ID)  
                self.bd.run_query(query)


