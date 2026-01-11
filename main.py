from Person import Person
from Employee import Employee
from Doctor import Doctor
from Surgeon import Surgeon
from Vet import Vet
from Lawyer import Lawyer

per = Person("Kim", 29)
print(per.name)
per.birth_date()
print()

doc = Doctor("Jim", 38, 928846, False)
print(doc.age)
doc.md()
print()

sur = Surgeon("Donna", 58, 738469208, False, True)
print(sur.em_id)
sur.heart_surgeon()
print()

vet = Vet("Harry", 42, 778899, False, True, True)
print(vet.is_intern)
vet.is_licensed()
print()

law = Lawyer("Gina", 46, 875635, True)
print(law.em_id)
law.communication()
