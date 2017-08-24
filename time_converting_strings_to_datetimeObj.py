import datetime

print(datetime.datetime.strptime('October 21, 2017', '%B %d, %Y'))
print(datetime.datetime.strptime('2017/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))
print(datetime.datetime.strptime("October of '15", "%B of '%y"))
print(datetime.datetime.strptime("November of '63", "%B of '%y"))
