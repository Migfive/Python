# Exercise_10
student = input("Enter your note of  three partial: ")
exam_end = float(input("Enter your exam end note: "))
work_end = float(input("Enter your work end note: "))

list_student = [float(notes) for notes in student.split(",")]


class Value:
    def __init__(self, list_student, exam_end, work_end):
        self.list_student = list_student
        self.exam_end = exam_end
        self.work_end = work_end
        
    def average_one(self):
        notes = sum(self.list_student) / len(self.list_student)
        total_notes = notes * 0.55
        return total_notes

    def average_two(self, total_notes):
        exam_notes = self.exam_end * 0.33
        work_notes = self.work_end * 0.15
        enter_notes = total_notes+exam_notes+work_notes
        return enter_notes


total = Value(list_student, exam_end, work_end)

partial = total.average_one()

final = total.average_two(partial)
print(f"your note end is {final}")
        
    
