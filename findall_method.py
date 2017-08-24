import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())


phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #has no groups
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))


phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') #has groups
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 222-555-0000'))
