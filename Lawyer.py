from Employee import Employee

class Lawyer(Employee):

    def __init__(self, name, age, emp_id, is_confident):
        super().__init__(name, age, emp_id)
        self.is_confident = is_confident

    def communication(self):
        print("This lawyer has good communication skills")

    def problem_solving(self):
        print("This lawyer has great problem solving skills")
