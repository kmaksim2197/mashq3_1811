class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def calculate_bonus(self):
        raise NotImplementedError


class Manager(Employee):
    def calculate_bonus(self):
        return self.get_salary() * 0.20


class Developer(Employee):
    def calculate_bonus(self):
        return self.get_salary() * 0.15


class Designer(Employee):
    def calculate_bonus(self):
        return self.get_salary() * 0.10


employees = [
    Manager("Ali", 5000),
    Developer("Vali", 4000),
    Designer("Soli", 3500)
]

for e in employees:
    print(e.name, "bonus:", e.calculate_bonus())
