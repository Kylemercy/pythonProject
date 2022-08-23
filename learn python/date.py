import datetime

# naive datetime
d = datetime.date(2018, 3, 25)
print(d)
# remember not to add zero for single digit
tday = datetime.date.today()
print(tday)
# methods of today
# for year
print(tday.year)
print(tday.month)
# to get the day of the week
print(tday.weekday())
# for this monday is 0 and sunday is 6
print(tday.isoweekday())
# for this monday is 1 and sunday is 7
# time delta this is the diff between 2 dates and time
tdelta = datetime.timedelta(days=7)
print('seven days from today is:', tday + tdelta)
print('the date seven days ago is:', tday - tdelta)
# how many days to birthday
bday = datetime.date(2022, 10, 22)
till_bday = bday - tday
print('Days remaining till birthday is:', till_bday)
# to get the number of days only
print('Days remaining till birthday is:', till_bday.days)
# to get the days remaining in seconds
print('Days remaining till birthday is in seconds:', till_bday.total_seconds())
