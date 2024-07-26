# Exercise_19
qualification = input("Enter your notes first correct second incorrect third in white Example (5,4,2): ")
list_note = [int(note) for note in qualification.split(',')]


class All_qualification:
    def __init__(self, correct, incorrect, white):
        self.correct = correct
        self.incorrect = incorrect
        self.white = white

    def operation(self):
        total_point = (self.correct * 5) + (self.incorrect * -1) + (self.white * 0)
        total_responses = self.correct + self.incorrect + self.white
        if total_responses > 0:
            average = total_point/total_responses
        else:
            average = 0

        print(f"average {average:.2f}")


print(All_qualification(list_note[0], list_note[1], list_note[2]).operation())
