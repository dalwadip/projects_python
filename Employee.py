from Person import Person

class Employee(Person):

    def __init__(self, name, age, emp_id):
        super().__init__(name, age)
        self.em_id = emp_id

    def insurance(self):
        print("This employee has insurance")
