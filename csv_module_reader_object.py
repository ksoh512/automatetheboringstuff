import csv

exampleFile = open('csv_module_example.csv')        # open csv file
exampleReader = csv.reader(exampleFile)             # read opened csv file
exampleData = list(exampleReader)                   # create a list of the content in csv file after reading
print(exampleData)                                  # print the list of content


print(exampleData[0][0])
print(exampleData[0][1])
print(exampleData[0][2])
