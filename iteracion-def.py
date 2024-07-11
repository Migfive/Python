frutas = ['Naranja', 'Banana', 'Manzana']
def iteraccion(a,b): 
    for i in b:
        if i == a:
            yield 'Estas dentro'
            return
    yield 'Estas fuera'
        
frutero = input('Dime tu fruta ')

result =iteraccion(frutero, frutas)

for mensaje in result:
    print(mensaje)


