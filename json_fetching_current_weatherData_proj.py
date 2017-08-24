#! python 2.7
# Prints the weather for a location from the command line

import json, requests, sys

#TODO: compute location from command line arguments
if len(sys.argv) < 2:
    print('Usage: json_fetching_current_weatherData_proj.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])



#TODO: Download the JSON data from OpenWeatherMap.org's API
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
response = requests.get(url)
print(response.raise_for_status())
print(response.text)


#TODO: Loads JSON data into a Python variable
weatherData = json.loads(response.text)
w = weatherData['list']         # print weather descriptions

print('Current WEather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
