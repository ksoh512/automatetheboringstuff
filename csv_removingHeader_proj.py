#! python3

# removeCSVHeader.py - Removes the header from all CSV files in the current
# Working directory


import csv, os

os.makedirs('headerRemoved')

#TODO: Loop through every file in the current working directory.
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue            # skip non-csv files

    print('Removing header from ' + csvFilename + '...')


    #TODO: Read the CSV file in (skipping first row)
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue                # skip first row
        csvRows.append(row)
    csvFileObj.close()

    #TODO: Write out the CSV file.
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
