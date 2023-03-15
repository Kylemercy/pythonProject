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
        # we increase the num of Employee within the init method as this runs whenever we create a new Employee

    def fullname(self):
        return self.first + ' ' + self.last

    # to access the class variable we use an instance
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10

    # changing the raise amount in the subclass doesn't affect the raise amount in the Employee parent class
    def __init__(self, first, last, pay, pro_lang):
        # to inherit the attributes from the parent class
        # this method also works Employee.__init__(self,first, last, pay)
        super().__init__(first, last, pay)
        self.pro_lang = pro_lang


class manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        # we don't directly pass a list to the Employee as it is not a healthy practice to pass mutable data types
        # like list,dict as default argument
        super().__init__(first, last, pay)
        self.employees = employees
        if self.employees is None:
            self.employees = []
            # if no Employee is given it prints an empty list
        else:
            # this adds an Employee to the list
            self.employees = employees

    def add(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('->>>', emp.fullname())


dev_1 = Developer('max', 'smith', 3000, 'python')
dev_2 = Developer('john', 'walker', 6000, 'java')
print(dev_1.pay)

dev_1.apply_raise()
print(dev_1.pay)
print(dev_1.email)
print(dev_2.pro_lang)
mang_1 = manager('sam', 'daniel', 87000, [dev_1])
print(mang_1.email)
mang_1.print_emp()
mang_1.add(dev_2)
mang_1.remove(dev_1)
mang_1.print_emp()
# using isinstance this tells object is an instance of a class example
print(isinstance(mang_1, manager))
# this checks if mang_1 is an instance of manager

print(isinstance(mang_1, Developer))
# is subclass will tell us if a class is a subclass of another
print(issubclass(Developer, Employee))
print(issubclass(Developer, manager))
