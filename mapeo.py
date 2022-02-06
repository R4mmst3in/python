from functools import reduce

numbers = [x+1 for x in range(20)]

def square(n):
	return n**2

def even(n):
	return n % 2 == 0

def multiply(x, y):
	return x * y

squares = list(map(square, numbers))
print(squares)

evens = list(filter(even, numbers))
print(evens)

products = reduce(multiply, numbers)
print(products)

squares = list(map(lambda x: x**2, numbers))
print(squares)

evens = list(filter(lambda x: x%2==0, numbers))
print(evens)

products = reduce(lambda x,y: x*y, numbers)
print(products)
