

def main():
	class gato(object):

		especie = "mamifero"

		def __init__(self, nombre, edad):
			self.nombre = nombre
			self.edad = edad
			self.alimentos=["Galletas","Pescado"]

		def verEtapaDeVida(self):
			if self.edad > 1:
				print(self.nombre, "es adulto")
			else:
				print(self.nombre, " es cachorro")

		def esAlimentoFavorito(self, alimento):
			return alimento in self.alimentos


	gatos=[]

	for i in range(10):
		gatos.append(gato("Lacasito", i*2))

	for miau in gatos:
		print(miau.nombre)
		print(miau.edad)
		print(miau.alimentos)
		miau.verEtapaDeVida()
		


if __name__ == '__main__':
	main()
