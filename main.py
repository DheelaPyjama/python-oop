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
    
    
emp_1 = Employee("Rohit", "Chakraborty", 100000)
print(emp_1.fullname())

emp_2_str = 'Rhea-Mantri-5000000'
emp_2 = Employee.from_string(emp_2_str)

emp_1.apply_raise()
print(emp_1.pay)
print(emp_2.fullname())

import datetime
print(Employee.is_workday(datetime.date(2025, 1, 5)))

