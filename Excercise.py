import math

# Exercise_1
name = input("Enter your name: ")
print("Hello " + name)

# Exercise_2
print(f"remember {name}, That the formula of perimeter is p =(a+b+c)")
perimeter = input("Enter your areas rectangle,  So (1,2,3,4): ")
elements = perimeter.split(',')
list_number = [int(element) for element in elements]

suma_number = sum(list_number)
print(f"Perimeter is : {suma_number}")

# Exercise_3
print("New, but calculate the Hypotenuse, we need C^2 = Ca + Cb ")
dates = input("Enter your date one Ca+Cb example (1,2): ")

separate_dates = dates.split(',')

list_dates = [int(date) for date in separate_dates]

operation_one = math.sqrt(list_dates[0] ** 2 + list_dates[1] ** 2)

print(f"you hypotenuse is {operation_one:.2f}")


# Exercise_4
class operation:
    def __init__(self, numbers):
        self.numbers = numbers

    def sum(self):
        return sum(self.numbers)

    def rest(self):
        return self.numbers[0] - self.numbers[1]

    def division(self):
        return self.numbers[0] // self.numbers[1]

    def multi(self):
        return self.numbers[0] * self.numbers[1]


two_number = input("Enter two numbers separate from ´,´ for addition and subtraction, division, multiplication :  ")

list_operation = [int(operator) for operator in two_number.split(',')]

op = operation(list_operation)

print(f"La suma es {op.sum()}, la resta es {op.rest()}, la division es {op.division()}, la multiplication es {op.multi()}")


