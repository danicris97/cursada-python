
import clsConexionF 

class clsIrisType:
	def __init__(self):
		self.bd= clsConexionF.clsConexion()

	def getData(self):
		query = "SELECT * FROM EstudianteC;"
		result = self.bd.run_query(query)

		if (len(result)==0):
			return None
		else:
			return result