import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
print(tuple(sheet['A1':'C3']))

for rowOfCellObjects in sheet['A1':'C3']:
    for cellObj in rowOfCellObjects:
        print(cellObj.coordinate, cellObj.value)
    print('--- END OF ROW ---')





wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.active
print(sheet.columns[1])

for cellObj in sheet.columns[1]:
    print(cellObj.value)
