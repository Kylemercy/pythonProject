import datetime

# this is a naive time as it dosent specify any timezone
t = datetime.time(9, 3, 45, 5000)
# this takes in hour,mins,second, and milliseconds as parameter
print(t)
print(t.hour, 'hours')
print(t.minute, 'minutes')
# to print both time and date
t_time = datetime.datetime(2022, 4, 23, 9, 3, 45, 5000)
# this takes in both the year month day and time
print(t_time)
tdelta = datetime.timedelta(days=7)
thour = datetime.timedelta(hours=7)
tminis = datetime.timedelta(minutes=7)
print(tdelta + t_time)
print(t_time + thour)
print(t_time + tminis)
# methods in datetime
print('\n')
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utnow = datetime.datetime.utcnow()
# difference between today() and noww() today method retuens the local time without an option to pass in a timezone
# but now allows us to pass us tzone so as utcnow
print(dt_today)
print(dt_now)
print(dt_utnow)
# how to ptz for timezone
