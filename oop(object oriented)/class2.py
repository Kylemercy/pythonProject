class Employee:
    raise_amount = 1.04
    num_emp = 0

    # this is a class variable
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + ',' + self.last + 'company.com'
        Employee.num_emp += 1
        # we increase the num pf Employee within the init method as this runs whenever we create a new Employee

    def fullname(self):
        return self.first + ' ' + self.last

    # to access the class variable we use an instance
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('max', 'smith', 3000)
emp_2 = Employee('john', 'walker', 6000)
print(emp_1.email)
print(emp_2.email)
print(emp_2.fullname())
print(Employee.raise_amount)
print(emp_1.__dict__)
# prints all the attributes of emp1
print(Employee.num_emp)
