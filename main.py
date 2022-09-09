import re

def changeDateCorrectWay(txt):
    d1 = re.search("[0-2][0-9]:[0-5][0-9]",txt[:4])
    d2 = re.search("[0-3][0-9]\/[0-1][0-9]\/\d{4}",txt[5:])
    # print(d1)
    if d1 == None:
        print(txt[11:]+' '+txt[::-1])

    # d = d.group()
    print(txt)

# date1 = '18:11 23/08/2022'

# changeDateCorrectWay(date1)

date2 = '2022/08/18 00:30'



changeDateCorrectWay(date2)
