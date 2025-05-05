class Student:
    def init(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.name}, Marks: {self.marks}")
if name == "main":
    s = Student("Ali", 85)
    s.display()
