#Setting color to default value at 'black'
spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')

#Setting color to default value at 'white'.
#This does NOT changing the default value for color because color key already exists.
spam.setdefault('color', 'white')
