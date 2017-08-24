import csv

exampleFile = open('csv_module_example.csv')                        # open selected csv file
exampleReader = csv.reader(exampleFile)                             # read opened csv file
for row in exampleReader:
    print('#' + str(exampleReader.line_num) + ' ' + str(row))       # print row numbers along with the contents in each rows
