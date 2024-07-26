# Exercise_7
enter_Date = int(input("convert date in a Clock: "))


class convert:
    def __init__(self, enter_Date):
        self.enter_Date = enter_Date

    def operation(self):
        if self.enter_Date < 0:
            print("No is value you date")
            return

        hours = self.enter_Date // 3600
        minutes = (self.enter_Date % 3600)//60
        seconds = self.enter_Date % 60
        print(hours, ': ', minutes, ': ', seconds)


result = convert(enter_Date)
result.operation()
