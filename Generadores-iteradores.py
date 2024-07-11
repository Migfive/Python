#Lista
lista = [1,2,3,4]

my_iter = iter(lista)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# Cadena Texto
texto = "Hola mundo"

my_texto=iter(texto)

for caracter in my_texto:
    print(caracter)

#Números impares hasta 10
limite = 10

impares=iter(range(1,limite+1,2))

for i in impares:
    print(i)

#Números pares hasta 10
pares=iter(range(0,limite+1,2))

for i in pares:
    print(i)

#TODO generadores 
def mi_generador():
    yield 1
    yield 2
    yield 3

# Usar el generador
for valor in mi_generador():
    print(valor)


#Serie de fibonachi

def fibonachi(limit):
    a,b = 0,1
    while a<limit:
        yield a
        a,b= b, a+b

for num in fibonachi(10):
    print(num)