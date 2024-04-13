import openpyxl


def update_value_excel(filename,cellname,value):
    wb=openpyxl.load_workbook(filename)
    Sheet1=wb["Sheet1"]
    Sheet1[cellname].value=value
    wb.save(filename)
    wb.close()
def get_value_excel(filename,cellname):
    wb=openpyxl.load_workbook(filename)
    Sheet1=wb["Sheet1"]
    wb.close()
    return Sheet1[cellname].value

filename='input.xlsx'
status='C6'
username='A6'
password='B6'
print(f'username: {get_value_excel(filename,username)}, pass: {get_value_excel(filename,password)}, status: {get_value_excel(filename,status)}')

#update password
update_value_excel(filename,password,'new pass***')
print(f'username: {get_value_excel(filename,username)}, new updated pass: {get_value_excel(filename,password)}, status: {get_value_excel(filename,status)}')
