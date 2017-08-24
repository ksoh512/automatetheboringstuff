#! python 2.7
# countdown.py - A simple countdown script.

import time, subprocess

timeLeft = 20
while timeLeft > 0:
    print(timeLeft)
    time.sleep(1)
    timeLeft = timeLeft - 1

#TODO: At the end of the countdown, play a sound file
subprocess.Popen(['start', 'alarm.wav'], shell=True)
