# Exercise_20
enter_dinner = float(input("Enter a number in pesos: "))
print("Conversion to dollars, Euro select 1, 2")
conversion = int(input("Conversion: "))


class dinner_conversion:
    def __init__(self, number, enter):
        self.number = number
        self.enter = enter

    def numbers(self):
        if self.number == 1:
            value = 4017.93
            print(f"{(self.enter/value):.2f} dollar")
        elif self.number == 2:
            value = 4376.99
            print(f"{(self.enter/value):.2f} Euro")
        else:
            print("Other money stupid?")


print(dinner_conversion(conversion, enter_dinner).numbers())
