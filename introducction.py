class Multiply:
    def __init__(self, x):
        self.x = x

    def number_multiply(self):
        for i in range(1, 11):
            total = self.x * i
            print(f"{self.x} x {i} = {total}")


class Rest(Multiply):
    def number_multiply(self):
        print("------------")
        print("------------")
        for i in range(1, 11):
            total = self.x - i
            print(f"{self.x} - {i} = {total}")


enter_number = int(input("Enter a number: "))
# Multiply
multiply = Multiply(enter_number)
multiply.number_multiply()
# Rest
rest = Rest(enter_number)
rest.number_multiply()

