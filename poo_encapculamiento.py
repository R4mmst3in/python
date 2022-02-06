
class A:
	def __init__(self):
		self.__contador = 0

	def incrementa(self):
		self.__contador += 1

	def cuenta(self):
		return self.__contador

class B(object):
	def __init__(self):
		self.__contador = 0

	def incrementa(self):
		self.__contador += 1

	def cuenta(self):
		return self.__contador

if __name__ == "__main__":

	a = A()
	b = B()

	inc_a = int(input("Incremento de A : "))

	inc_b = int(input("Incremento de B : "))

	for i in range(inc_a):
		a.incrementa()

	for i in range(inc_b):
		b.incrementa()


	print(a.cuenta())
	print(b.cuenta())
