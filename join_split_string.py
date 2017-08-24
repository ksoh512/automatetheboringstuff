x = ['cats', 'rats', 'bats']
print (', '.join(x))

y = ['My', 'name', 'is', 'Simon']
print(' '.join(y))

print('ABC'.join(y))


z = 'My name is Simon'.split()
print(z)

xx= 'MyABCnameABCisABCSimon'.split('ABC')
print(xx)

yy= 'My name is Simon'.split('m')
print(yy)


spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".

Please do not drink it.
Sincerely,
Bob'''
print(spam.split('\n'))
