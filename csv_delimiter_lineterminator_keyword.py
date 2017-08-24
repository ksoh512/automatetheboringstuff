import csv

csvFile = open('example.tsv', 'w')
csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
csvWriter.writerow(['apples', 'oranges', 'grapes'])
csvWriter.writerrow(['eggs','bacon','ham'])
csvWriter.writerow(['spam','spam','spam','spam','spam','spam'])
csvFile.close()
