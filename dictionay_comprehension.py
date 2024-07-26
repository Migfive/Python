import random

countries = ['Col', 'Mex', 'Bol', 'Pe']

people = {country: random.randint(1, 100) for country in countries}

print(people)

result_maxive = {country: people_2 for (country, people_2) in people.items() if people_2 > 20}
print(result_maxive)


cadena_str = 'Hola, soy Miguel'
unique = {c: c.upper() for c in cadena_str if c in 'aeiou'}
print(unique)