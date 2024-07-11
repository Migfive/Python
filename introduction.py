Contact = [
    {'name':'Miguel', 'age':22, 'activity':'programm'},
    {'name':'Arturo', 'age':18, 'activity':'pilot-game'},
    {'name':'Luis', 'age':25, 'activity':'Ingeniery'}
]

name = input('dime tu nombre: ')
found = False

#TODO primera opcion de recorrer una lista en busca de un elemento

# for i in Contact:
#     if name == i['name']:
#         print ('Estas dentro')
#         found=True
#         break

# if not found:
#     print('No eres de aquí')

#TODO segunda opcion para recorrer una lista de diccionario
index = 0
while index < len(Contact):
    if name == Contact[index]['name']:
        print('Estas dentro')
        found=True
        break
    index +=1


if not found:
    print('No eres de aqui')

#Todo Recomendación la primera opción es mas sencilla