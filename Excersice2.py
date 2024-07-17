# Exercise_5
f = int(input("Enter a number fahrenheit: "))

print(f"the solution in Celsius: {(f - 32) * 5 / 9}")

# Exercise_6
print(f"remember that for find of medium is formula Me= a+b/2")
date = input("Enter two date example (5,6): ")

value = [int(compiler) for compiler in date.split(',')]

start = value[0]
end = value[1]


class Medium:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def conditional(self):
        if self.a > self.b:
            self.a, self.b = self.b, self.a
            print(f"{start} is less than {end}")
        else:
            number_list = list(range(self.a, self.b + 1))
            return number_list

    def formula(self):
        list_number = self.conditional()
        total = sum(list_number)
        count = len(list_number)
        return total / count


medium = Medium(start, end)

# Result
number_list = medium.conditional()
print(f"the number enter {medium.a} and {medium.b} is: {number_list}")

media = int(medium.formula())
print(f"The media enter  {medium.a} and {medium.b} is: {media}")
