# Exercise_8
Seller = int(input("Enter your salary: "))
commission = input("Enter your sales Example 3000, 4000: ")

list_Commission = [int(commits) for commits in commission.split(",")]


class Record:
    def __init__(self, record):
        self.record = record

    def recording(self):
        total_sales= sum(self.record)
        return total_sales


class Percent:
    def __init__(self, salary, total_sales):
        self.salary = salary
        self.total_sales = total_sales

    def operation(self):
        commits = int((self.total_sales / 100) * 10)
        self.salary = int(self.salary + commits)
        print(f"you salary with commission apply is $ {self.salary}, the commission is $ {commits}")


date = Record(list_Commission)
total_sales = date.recording()
Consult = Percent(Seller, total_sales)
Consult.operation()


