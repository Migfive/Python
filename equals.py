import random


class Equals:
    def __init__(self, number):
        self.number = number

    def enter_date(self):
        self.number = int(input("Enter all numbers "))
        dates = []
        for lol in range(self.number):
            random_number = random.randint(1, 10)
            dates.append(random_number)

        print("Generate ", dates)
        for i in dates:
            if i == 0:
                print("Found zeros ", i)


start = Equals(0)
start.enter_date()

