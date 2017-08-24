while True:
    print('Who are you')
    name = raw_input()
    if name != 'Kyu':
        continue
    print('Hello, Kyu. What is the password? (It is a fish).')
    password = raw_input()
    if password == 'swordfish':
        break
print('Access granted!')
