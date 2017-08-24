import subprocess

subprocess.Popen('C:\\Windows\\System32\\calc.exe')

# Popen object has two methods: poll() and wait()

calcProc = subprocess.Popen('C:\\Windows\\System32\\calc.exe')
print(calcProc.poll() == None)

print(calcProc.wait())          # wait() call will block until you quit the launched calculator program.

print(calcProc.poll())
