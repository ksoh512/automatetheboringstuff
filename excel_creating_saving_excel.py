import openpyxl

wb = openpyxl.Workbook()
print(wb.get_sheet_names())

sheet = wb.active
print(sheet.title)

sheet.title = 'Spam Bacon Eggs Sheet'
print(wb.get_sheet_names())
wb.save('excel_creating_sample.xlsx')
