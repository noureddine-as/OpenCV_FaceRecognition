import xlsxwriter

# [[id  , last_name, first_name], [.. , .. , ..] ... []]
def writeExcel(list, course, branch, date, d1, d2, excel_name):
    workbook = xlsxwriter.Workbook(course + excel_name + '.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write('C1', date)
    worksheet.write('B3', course)
    worksheet.write('B4', branch)
    worksheet.write('B5', d1)
    worksheet.write('B6', d2)
    for i in range(len(list)):
        worksheet.write('A' + str(i + 10), list[i][0])
        worksheet.write('B' + str(i + 10), list[i][1])
        worksheet.write('C' + str(i + 10), list[i][2])

    worksheet.set_column('A1:B1', 50)
    bold = workbook.add_format({'bold': True})
    worksheet.write('B1', 'absence situation:', bold)
    worksheet.write('A3', 'Course:', bold)
    worksheet.write('A4', 'branch:', bold)
    worksheet.write('A5', 'from:', bold)
    worksheet.write('A6', 'to:', bold)
    worksheet.write('A9', 'Id', bold)
    worksheet.write('B9', 'LastName', bold)
    worksheet.write('C9', 'FirstName', bold)

    worksheet.set_column('A2:C2', 20)
    workbook.close()

