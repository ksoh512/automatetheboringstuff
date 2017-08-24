spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)


for k in spam.keys():
    print(k)

#If you want a true list from one of
#these methods, pass its list-like return
#value to the list() function. Enter the following into the interactive shell

spam = {'color': 'red', 'age': 42}
print (spam.keys())

print(list(spam.keys()))


#Checking whether a key or value exists in a dictionary

spam = {'name': 'Zophie', 'age': 7}
print('name' in spam.keys())
print('Zophie' in spam.values())
