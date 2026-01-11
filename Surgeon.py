from Doctor import Doctor

class Surgeon(Doctor):

    def __init__(self, name, age, emp_id, intern, on_vacation):
        super().__init__(name, age, emp_id, intern)
        self.on_vacation = on_vacation

    def md(self):
        print("This doctor has an MD")

    def heart_surgeon(self):
        print("This surgeon will operate on a patient's heart")