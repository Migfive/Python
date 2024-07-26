import random

guess = None


class Guess:
    def __init__(self, gues):
        self.guess = gues
        self.number = True

    def operation(self):
        self.guess = int(input("Guess a number between 1 and 10: "))
        one = random.randint(1, 10)
        if one == self.guess:
            print(f"Correct! {self.guess}")
            self.number = False
        else:
            print(f"Wrong! {one}")
            self.number = True

    def run(self):
        while self.number:
            self.operation()
        print("Game over")


guess = Guess(guess)
print(guess.run())
