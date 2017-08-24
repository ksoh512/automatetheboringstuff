import threading, time

print('Start of program...')

def takeANap():
    time.sleep(5)
    print('Wake up!')

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('End of program.')



# Passing arguments to the thread's target function
print('Cats', 'Dogs', 'Frogs', sep=' & ')

# Regular arguments can be passed as a list to the args keyword argument in threading.thread()
threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})
print(threadObj.start())
