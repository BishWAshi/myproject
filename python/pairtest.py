from allpairspy import AllPairs
from xlrd import open_workbook
import xlwt

wb = open_workbook("C:\\Users\\Khairul Basar\\Documents\\A004_CWDProjects\\GitHub\\myproject\\python\\testpairs.xlsx")
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
        for name, col in zip(col_names, range(s.ncols)):
            value  = (s.cell(row,col).value)
            try : value = str(int(value))
            except : pass
            col_value.append((name.value, value))
        values.append(col_value)
        
print (values)

#write to excel save
#sheet1.write(row, co1, values[i,j])





def is_valid_combination(row):
    """
    This is a filtering function. Filtering functions should return True
    if combination is valid and False otherwise.

    Test row that is passed here can be incomplete.
    To prevent search for unnecessary items filtering function
    is executed with found subset of data to validate it.
    """

    n = len(row)

    if n > 1:
        # Brand Y does not support Windows 98
        if "98" == row[1] and "Brand Y" == row[0]:
            j+=1
            return False

        # Brand X does not work with XP
        if "XP" == row[1] and "Brand X" == row[0]:
            j+=1
            return False

    if n > 4:
        # Contractors are billed in 30 min increments
        if "Contr." == row[3] and row[4] < 30:
            j+=1
            return False

    return True

parameters =values

j=0

print("PAIRWISE:")
for i, pairs in enumerate(AllPairs(parameters, filter_func=is_valid_combination)):
    print("{:2d}: {}\n".format(i, pairs))
    #print(str(i)+"==="+str(pairs))
    #str1=str(pairs[i-1])
    #sheet1.write(i, 1, str1)
    #print(pairs[i])
book.save("passfail2.xls")
print("filesaved")
