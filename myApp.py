# Enter your date automatic
class Enter_Date:
    def __init__(self, name, years):
        self.DateN = []
        self.name = name
        self.years = years
        self.available = True

    def list_date(self):
        if self.available:
            self.DateN.append(self.name)
            self.DateN.append(self.years)
            return self.DateN


class start:
    def __init__(self):
        self.var1 = ""
        self.var2 = ""

    def conversation(self):
        print("Hello today we are going to store data ")
        print("1.Enter date ")
        print("2.End ")
        Enter1 = int(input())
        if Enter1 == 1:
            self.var1 = input("Enter your name: ")
            self.var2 = input("Enter your age: ")
            return self.var1, self.var2
        else:
            print("Coming out")


income = int(input("Please income how much data going to Enter "))
all_data = []

user1 = None
for i in range(income):
    person1 = start()
    person1.conversation()

    user1 = Enter_Date(person1.var1, person1.var2)
    all_data.append(user1.list_date())

print(all_data)


class Rol_family:
    def __init__(self, data):
        self.data = data
        self.occupation = []

    def enter_date(self, index):
        adjusted_index = index - 1
        if adjusted_index < len(self.data):
            name, age = self.data[adjusted_index]
            print(f"Hola {name} a question")
            occupation_data = input("What is your occupation in the family? ")
            self.occupation.append(occupation_data)
            return occupation_data
        else:
            return "Index out of range"

    def result_date(self, index):
        if index < len(self.occupation):
            name, age = self.data[index]
            print(f"{name} of {age} ages your occupation in family is {self.occupation[index]}")
        else:
            print("Index out of range")


start_family = Rol_family(all_data)

for i in range(len(all_data)):
    index_to_retrieve = int(input("Enter the index of the data you want to retrieve: "))
    print(start_family.enter_date(index_to_retrieve))

print(start_family.occupation)
one = 0
while one < len(all_data):
    start_family.result_date(one)
    one += 1
