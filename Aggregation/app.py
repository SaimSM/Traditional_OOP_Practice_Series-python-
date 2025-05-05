class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee  

if __name__ == "__main__":
    e = Employee("Zara")
    dept = Department("HR", e)
    print(f"{dept.name} department has employee {dept.employee.name}")
