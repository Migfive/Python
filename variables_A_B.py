# Exercise_15
value = input("Enter two numbers: ")
list_Value = [int(number) for number in value.split(',')]

one = list_Value[0]
two = list_Value[1]

one, two = two, one

print(f"the value exchanged {one, two}")
