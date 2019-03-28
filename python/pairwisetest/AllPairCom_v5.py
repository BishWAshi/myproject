import xlrd
from allpairspy import AllPairs
path ="X:\\KhairulBasar\\AllPairTesting\\AllPairwiseTesting_v5.xlsx"
loc = (path)
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(3)
sheetname = wb.sheet_by_name("Ports")


print("#=====================Para Arrays=======================")
#Ports
sheetname = wb.sheet_by_name("Ports")
#SlotCount=[]
#Ports=[]
#IOType=[]
#Pins=[]
Slot1=[]
Slot2=[]
Slot3=[]
'''
print("#=====================ports=======================")
#Ports
#ports
cells = sheetname.row_slice(rowx=2,start_colx=2,end_colx=6)
for cell in cells:
    Ports.append(cell.value)
print (Ports)

print("#=====================IOType=======================")
#IOType
cells = sheetname.row_slice(rowx=3,start_colx=2,end_colx=6)
for cell in cells:
    IOType.append(cell.value)
print (IOType)
print("#=====================Pins=======================")
#Pins
cells = sheetname.row_slice(rowx=4,start_colx=2,end_colx=4)
for cell in cells:
    Pins.append(cell.value)
print (Pins)
'''
print("#=====================Slot1=======================")
#Slot1
cells = sheetname.row_slice(rowx=5,start_colx=2,end_colx=4)
for cell in cells:
    Slot1.append(cell.value)
print (Slot1)

print("#=====================Slot2=======================")
#Slot2
cells = sheetname.row_slice(rowx=6,start_colx=2,end_colx=6)
for cell in cells:
    Slot2.append(cell.value)
print (Slot2)

print("#=====================Slot3=======================")
#Slot2
cells = sheetname.row_slice(rowx=7,start_colx=2,end_colx=3)
for cell in cells:
    Slot3.append(cell.value)
print (Slot3)
'''
print("#=====================SlotCount=======================")
#SlotCount
#SlotCount
cells = sheetname.row_slice(rowx=8,start_colx=2,end_colx=4)
for cell in cells:
    SlotCount.append(cell.value)
print (SlotCount)
'''
#==========================Ports End===================


#-----------------------------------------------------------------------------------------------------

def is_valid_combination(row):
    """
    This is a filtering function. Filtering functions should return True
    if combination is valid and False otherwise.

    Test row that is passed here can be incomplete.
    To prevent search for unnecessary items filtering function
    is executed with found subset of data to validate it.
    """

    n = len(row)
    if True:
        pass
    ''''
    if n > 1:
        # Brand Y does not support Windows 98
        if "98" == row[1] and "Brand Y" == row[0]:
            return False

        # Brand X does not work with XP
        if "XP" == row[1] and "Brand X" == row[0]:
            return False

    if n > 4:
        # Contractors are billed in 30 min increments
        if "Contr." == row[3] and row[4] < 30:
            return False
'''
    return True

'''
Ports=[]
IOType=[]
Pins=[]
Slot1=[]
Slot2=[]
Slot3=[]

'''
parameters = [
    #SlotCount,
    #Ports,
    #IOType,
    #Pins,
    Slot1,
    Slot2,
    Slot3
    ]

print("PAIRWISE:")
for i, pairs in enumerate(AllPairs(parameters, filter_func=is_valid_combination)):
    print("{:2d}: {}".format(i, pairs))
