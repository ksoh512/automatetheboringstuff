import datetime
import time



halloween2017 = datetime.datetime(2017, 10, 31, 0, 0, 0)
while datetime.datetime.now() < halloween2017:
    time.sleep(1)
