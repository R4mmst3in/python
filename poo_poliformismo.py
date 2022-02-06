class perro:
	def sonido(self):
		print("Guauu")

class gato:
	def sonido(self):
		print("Miauu")

class vaca:
	def sonido(self):
		print("Muuu")

def a_cantar(animales):
	for animal in animales:
		animal.sonido()


def main():
	perro_1 = perro()
	gato_1 = gato()
	gato_2 = gato()
	vaca_1 = vaca()
	gato_3 = gato()
	vaca_2 = vaca()

	granja = [perro_1,gato_1,gato_2,vaca_2,gato_3,vaca_2]
	a_cantar(granja)

if __name__ == '__main__':
	main()
