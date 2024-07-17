tupla = ("hola", "mundo")
print(type(tupla))
#Devuelve al valor absoluto de un número.
control = 4.95
print(abs(control))
#Toma como parámetro dos números, y devuelve una tubla con dos valores, la división entera, y el módulo o resto de la división.
dismod = 4.67
print(divmod(dismod, control))

#Devuelve una cadena con la representación hexadecimal del número que recibe como parámetro
number = 5
print(hex(number))

#Devuelve una cadena con la representación binaria del número que recibe como parámetro.
print(bin(number))

#Devuelve la potencia de la base x elevado al exponente y. Es similar al operador **`.
print(pow(number, 5, 4))

#Devuelve un número real (float) que es el redondeo del número recibido como parámetro, podemos indicar un parámetro opcional que indica el número de decimales en el redondeo.
print(round(7.65,number))