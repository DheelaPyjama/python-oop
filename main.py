from dataclasses import dataclass
class Employee:
    raise_amt = 1.08
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = self.first + '.' + self.last + "@company.com"
        self.pay = pay
    
        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt) 
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount        

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang 

class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self, emp):
        for emp in self.employees:
            print('-->', emp)

    def __repr__(self):
        return "{} {}".format(self.first, self.last)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __sub__(self, other):
        return self.pay - other.pay
    
emp_1 = Employee("Rohit", "Chakraborty", 100000)
print(emp_1.fullname())

emp_2_str = 'Rhea-Mantri-5000000'
emp_2 = Employee.from_string(emp_2_str)

emp_1.apply_raise()
print(emp_1.pay)
print(emp_2.fullname())

import datetime
print(Employee.is_workday(datetime.date(2025, 1, 5)))

dev_1 = Developer("test", "1", 200, 'Python')
dev_2 = Developer("test", "2", 300, 'Python')
mgr_1 = Manager("mgr", '1', 123123, [dev_1])
mgr_2 = Manager("mgr", '2', 123123, [dev_2])

mgr_1.add_emp(dev_2)
print(mgr_1.__repr__())
print(mgr_1.__str__())
print(mgr_1 + mgr_2)
print(mgr_1 - mgr_2)



