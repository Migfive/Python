import math

# Exercise_11
two_enter = input("Enter two numbers: ")
list_two = [int(number) for number in two_enter.split(',')]
start = list_two[0]
end = list_two[1]
distance = int(math.fabs(start - end))
print(f"the distance from two numbers is {distance}")
