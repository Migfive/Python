import random

dictionary = {}

for i in range(10):
    dictionary[i] = i * 2

print(dictionary)

# version 2
dict_2 = {i: i * 2 for i in range(10)}

print(dict_2)

# fast
countries = ['Col', 'Mex', 'Bol', 'Pe']
people_country = {i: random.randint(1, 100) for i in countries}

print(people_country)

names = ['John', 'Doe', 'Jane']
ages = [12, 56, 98]

new_dict = dict(zip(names, ages))
print(new_dict)
