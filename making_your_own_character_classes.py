import re


vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats bab food. BABY FOOD.'))


letters_numbers_Regex = re.compile(r'[a-zA-Z0-9]')
print(letters_numbers_Regex.findall('There are total of 6 zeBRAs '))

consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('Robocop eats baby food. BABY FOOD.'))
