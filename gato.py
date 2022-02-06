

def main():
	class gato:

		especie = "mamifero"

		def __init__(self, nombre, edad):
			self.nombre = nombre
			self.edad = edad
			self.alimentos=[]

		def verEtapaDeVida(self):
			if self.edad > 1:
				print(self.nombre, "es adulto")
			else:
				print(self.nombre, " es cachorro")

		def esAlimentoFavorito(self, alimento):
			return alimento in self.alimentos


	gato1 = gato("Lacasito",7)
	gato1.alimentos.append("pescado")
	gato1.alimentos.append("galletas")

	gato2 = gato("Miau",9)
	gato2.alimentos.append("leche")
	gato2.alimentos.append("arroz")
	gato2.raza="Siames"			#Asigna un nuevo atributo dinamico pero que solo estara disponible para gato2

	print(gato1.nombre)
	print(gato1.edad)
	print(gato1.especie)
	gato1.verEtapaDeVida()
	print(gato1.alimentos)

	print(gato2.nombre)
	print(gato2.edad)
	print(gato2.especie)
	print(gato2.raza)
	gato2.verEtapaDeVida()
	print(gato2.alimentos)

	print
if __name__ == '__main__':
	main()
