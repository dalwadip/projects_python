from sys import intern

from Doctor import Doctor

class Vet(Doctor):

    def __init__(self, name, age, emp_id, intern, on_vacation, is_kind):
        super().__init__(name, age, emp_id, intern)
        self.is_kind = is_kind

    def dvm(self):
        print("This vet has an DVM")

    def is_licensed(self):
        print("Vets must be licensed to practice in the state they work")