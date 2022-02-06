class Empleado:
	def __init__(self,nombre,edad,categoria,sueldo):
		self.nombre=nombre
		self.edad=edad
		self.categoria=categoria
		self.sueldo=sueldo

	def calculaSueldo(self, descuentos, bonos):
		return self.sueldo-descuentos+bonos

class agenteVentas(Empleado):
	def __init__(self,nombre,edad,categoria,sueldo,mostrador):
		self.numeroMostrador = mostrador
		super().__init__(nombre, edad, categoria, sueldo)


class tripulante(Empleado):
	def mostrarRenovacionLicencia(self):
		if self.edad < 50:
			print("Renueva su licencia cada año")
		else:
			print("Renueva su licencia cada seis meses") 


def main():
	pedro=AgenteVentas("Luis", 23 ,"Oficial" ,23000 ,3)

	print(pedro)

	print(pedro.calculaSueldo(100,3000))

	luis=tripulante("Jorge", 23, "H454", 60000)
	print(luis)
	luis.mostrarRenovacionLicencia()

if __name__ == "__main__":
	main()
