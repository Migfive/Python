# Exercise_9
store = input("Enter your shopping store Example ($3000, $4000): ")
list_shopping = [int(buy) for buy in store.split(",")]


class Descent:
    def __init__(self, shopping):
        self.shopping = shopping

    def total_cost(self):
        if self.shopping == "":
            print("Please enter your shopping list")

        list_total = sum(self.shopping)
        percentage = (list_total / 100) * 15
        return print(f"value total of the shopping is $ {int(list_total - percentage)}")


subtotal = Descent(list_shopping)
subtotal.total_cost()

