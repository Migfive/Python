class Vocal:
    def __init__(self, vocal):
        self.vocal = vocal
        self.date = ['a', 'e', 'i', 'o', 'u']

    def vocal_into(self):
        self.vocal = input("Enter a alphabeta: ").lower()

        while self.vocal.isalpha():
            if self.vocal not in self.date:
                return "not is Vocal"
            else:
                return "is Vocal"


vocal = Vocal(" ")
print(vocal.vocal_into())
