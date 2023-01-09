from datetime import datetime
tday = datetime.now()
m_day = datetime.time(tday)
print(m_day,m_day.strftime("%p"))
#p help it shows either pm or am
import datetime
import time
print( f"Today date and time is: \n{datetime.datetime.today()}")
print ("The current year is",datetime.date.today().strftime("%Y"))
print("The current month is:",datetime.date.today().strftime("%B"))
print("week number of the year is:",datetime.date.today().strftime("%W"))
print("weekday of the week is: ",datetime.date.today().strftime("%w"))
print("Day of the year is :", datetime.date.today().strftime("%j")," days")
print("Day in of the month is;",datetime.date.today().strftime("%D"))
print("Day in of the month is;",datetime.date.today().strftime("%d"))
print("Day in the week",datetime.date.today().strftime("%A"))
from datetime import datetime
Christmas = datetime(month = 12,day = 25,year = 1)
today = datetime.today()
Christmas= Christmas.replace(year = datetime.today().year)
count = Christmas- today
print("There are ",count.days,"remaining till Christmas!")
import datetime
b_day = datetime.date(year= 2000,month = 3,day = 24)
b_day2 = datetime.date(year = 1988,month= 5,day = 27)

if b_day < b_day2:
  print("Person one is older")
elif b_day > b_day2:
  print("Person two is older")
else:
  print("The ae both the same age")
from datetime import datetime
t = datetime.now()
m = datetime.time(t)
print(m)
print (m.hour)
print (m.minute)
print (m.second)
bday = datetime.date(2022,5,14)
till_bday = (bday-tday)
print(till_bday)
print(till_bday.days)
print(till_bday.total_seconds())
import datetime
tday = datetime.date.today()
tdelta = datetime.timedelta(days = 7)
print(tdelta + tday)


now = datetime.now()

# Returns a tuple year, week, and weekday
string = datetime.replace(now,2017,3,25)
print(string.weekday())
print(string.ctime())
print (string)

now = datetime.now()

string = datetime.astimezone(now)
# Returns the DateTime object containing
# timezone information.
print (string)