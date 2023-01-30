import datetime


class user:
    """this describes a username and birthday"""

    def __init__(self, fullname, birthday):
        self.fullname = fullname
        self.birthday = birthday
        name = fullname.split(' ')
        self.f_name = name[0]
        self.l_name = name[-1]

    def age(self):
        """returns the age of the user """
        birthday = datetime.date(2000, 3, 23)
        birth_year = birthday.year
        today = datetime.date.today()
        t_year = today.year
        age_in_days = (today - birthday).days
        age_in_years = t_year - birth_year
        print('Age in days: ',age_in_days)
        print('Age in years: ', age_in_years)


user1 = user('sam dan', '2001-01-09')
print(user1.fullname)
print(user1.f_name)
print(user1.age())

