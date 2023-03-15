# class method
# to convert a regular method to a class method we add a class-method decorator
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

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def string_format(cls, emp_name):
        first, last, pay = emp_name.split('-')
        return cls(first, last, pay)

    # creating a static method
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return "its a weekday"

        else:
            return 'Today is a workday'


emp_1 = Employee('max', 'smith', 3000)
emp_2 = Employee('john', 'walker', 6000)
# to change the class variable from 4% to %%
Employee.set_raise_amount(1.05)
print(Employee.raise_amount)
print(emp_1.raise_amount)
emp1_str = 'sam-randy-5500'
emp2_str = 'rew-goth-4600'
new_emp1 = Employee.string_format(emp1_str)
new_emp2 = Employee.string_format(emp2_str)
print(emp_1.fullname())
print(emp_1.first)
import datetime

my_date = datetime.date(2019, 4, 23)
print(Employee.is_workday(my_date))
my_date2 = datetime.date(2023, 3, 18)
print(Employee.is_workday(my_date2))
