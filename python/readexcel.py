from xlrd import open_workbook
import xlwt


wb = open_workbook("C:\\Users\\Khairul Basar\\Documents\\A004_CWDProjects\\GitHub\\myproject\\python\\testpairs.xlsx")
values = []
for s in wb.sheets():
    #print 'Sheet:',s.name
    for row in range(1, s.nrows):
        col_names = s.row(0)
        col_value = []
        for name, col in zip(col_names, range(s.ncols)):
            value  = (s.cell(row,col).value)
            try : value = str(int(value))
            except : pass
            col_value.append((name.value, value))
        values.append(col_value)
print (values)


book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")

