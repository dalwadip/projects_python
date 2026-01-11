from Employee import Employee

class Doctor(Employee):

    def __init__(self, name, age, emp_id, intern):
        super().__init__(name, age, emp_id)
        self.is_intern = intern

    def md(self):
        print("This doctor has an MD")