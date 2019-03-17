from allpairspy import AllPairs
from xlrd import open_workbook
import xlwt

wb = open_workbook("C:\\Users\\Khairul Basar\\Documents\\A004_CWDProjects\\GitHub\\myproject\\python\\testpairsSingle1.xlsx")
values = []
#Write to excel file
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet1",cell_overwrite_ok=True)
#==================
for s in wb.sheets():
    #print 'Sheet:',s.name
    for row in range(1, s.nrows):
        col_names = s.row(0)
        col_value = []
        for name, col in zip(col_names, range(0, s.ncols)):
            value  = (s.cell(row,col).value)
            try : value = str(int(value))
            except : pass
            col_value.append((name.value, value))
        values.append(col_value)
        

#print (values)

for i in range(len(values)):
    print (values[i])
    print ("\n")

#write to excel save
#sheet1.write(row, co1, values[i,j])




parameters =values


print("PAIRWISE:")
for i, pairs in enumerate(AllPairs(parameters)):
    print("{:2d}: {}\n".format(i, pairs))
    #print(str(i)+"==="+str(pairs))
    #str1=str(pairs[i-1])
    #sheet1.write(i, 1, str1)
    #print(pairs[i])
book.save("passfail2.xls")
print("filesaved")
