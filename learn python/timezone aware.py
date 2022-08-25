# timezone aware time using pytz and utc
import datetime
import pytz

dt = datetime.datetime(2022, 3, 23, 2, 29, 45, tzinfo=pytz.UTC)
print(dt)
# to get the current time zone using now
dt_now = datetime.datetime.now(tz=pytz.utc)
print(dt_now)
# another way is using utcnow but this doesn't allow us to pass a timezone
dt_utc = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utc)
# both utcnow and now gives the same result
# converting our time to our timszone
dt_zone = dt_now.astimezone(pytz.timezone('us/mountain'))
print(dt_zone)
# to get nigeria utc time zone
cur_zone = dt_now.astimezone(pytz.timezone('Etc/GMT-1'))
print(cur_zone)
# to print out different timezones
# for tz in pytz.all_timezones:
#  print(tz)
# making a naive datetime timezone aware
dt_mtn = datetime.datetime.now()
# naive time
mtn = pytz.timezone('Etc/GMT-1')
# to make our local naive datetime aware
# first we call our local timezone which is
mtn_tz = mtn.localize(dt_mtn)
print(mtn_tz)
# converting our local time to eastern time
dt_east = mtn_tz.astimezone(pytz.timezone('us/mountain'))
print(dt_east)
print(dt_east.isoformat())
# converting a num date time to a string datetime
print(dt_east.strftime('%B %d,%Y'))
# converting a string datetime
dt_string = 'August 25,2022'
dt = datetime.datetime.strptime(dt_string, '%B %d,%Y')
print(dt)
# strptime converts a string to a datetime
# strftime datetime to string
