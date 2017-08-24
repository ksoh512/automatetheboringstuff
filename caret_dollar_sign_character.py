import re

beginWithHello = re.compile(r'^Hello')
print(beginWithHello.search('Hello world!'))


print(beginWithHello.search('He said Hello.')) == None


endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('Your number is 42'))

print(endsWithNumber.search('Your number is forty two') == None)


wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('1234567890'))

print(wholeStringIsNum.search('12345xyz67890')) == None
print(wholeStringIsNum.search('12 34567890')) == None
