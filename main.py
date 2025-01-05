class Employee:
    raise_amt = 1.08

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = self.first + '.' + self.last + "@company.com"
        self.pay = pay

    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt) 
    
emp_1 = Employee("Rohit", "Chakraborty", 100000)
print(emp_1.fullname())

emp_1.apply_raise()
print(emp_1.pay)

