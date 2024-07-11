add = lambda a,b: a+b
print(add(10,4))

multiply = lambda a,b : a*b
print(multiply(80,5))

#cuadrado de cada numero
numbers = range(11)
numbers_squared = list(map(lambda x: x**2, numbers))
print("cuadrados", numbers_squared)

numeros_pares = list(filter(lambda x: x % 2 == 0, numbers))
print("Pares:", numeros_pares)