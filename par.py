even = input("Enter tow number: ")
list_even = [int(evens) for evens in str(even).split(',')]


class Even:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def operation(self):
        number_list = list(range(self.number1, self.number2+1))
        return number_list


call = Even(list_even[0], list_even[1])
print(call.operation())


