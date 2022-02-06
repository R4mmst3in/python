class Carrera:

	def __init__(self, nombre):
		self.nombre=nombre
		self.materias=[]

class Materia:
	def __init__(self, nombre, profesor):
		self.nombre=nombre
		self.profesor=profesor

def main():
	ing=Carrera("Ingenieria")
	programacion=Materia("Programacion","Luisa Menendez")
	fisica=Materia("Fisica","Roberto Perlado")
	quimica=Materia("Quimica","Lorena Rios")

	ing.materias.append((134,programacion))
	ing.materias.append((243,fisica))
	ing.materias.append((432,quimica))

	print(ing.materias)


if __name__ == '__main__':
	main()
