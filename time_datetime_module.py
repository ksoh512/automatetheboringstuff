import datetime


print(datetime.datetime.now())

dt = datetime.datetime(2015, 10, 21, 16, 29, 0)
print(dt.year, dt.month, dt.day)
print(dt.hour, dt.minute, dt.second)


halloween2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
newyear2016 = datetime.datetime(2016, 1, 1, 0, 0, 0)
oct31_2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)

print(halloween2015 == oct31_2015)

print(halloween2015 > newyear2016)

print(newyear2016 > halloween2015)

print(newyear2016 != oct31_2015)


# timedelta represents a duration of time rather than a moment in time.
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)

print(delta.total_seconds())


# To calculate the date 1,000 days from now.
dt = datetime.datetime.now()
print(dt)
thousandDays = datetime.timedelta(days=1000)
print(dt + thousandDays)


# multiply and divide timedelta
oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
aboutThirtyYears = datetime.timedelta(days=365 * 30)

print(oct21st)
print(oct21st - aboutThirtyYears)           # 30 years before
print(oct21st - (2 * aboutThirtyYears))     # 60 years before
