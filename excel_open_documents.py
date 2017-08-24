import openpyxl

wb = openpyxl.load_workbook('example.xlsx')

print(type(wb)) # Print type of wb

print(wb.get_sheet_names()) #print(sheet names in a list)

sheet = wb.get_sheet_by_name('Sheet3')
print(sheet)
print(type(sheet))
print(sheet.title)


anotherSheet = wb.active
print(anotherSheet)
