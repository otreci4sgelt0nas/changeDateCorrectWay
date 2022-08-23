import re

def changeDateCorrectWay(txt):
    d = re.search("[0-2][0-9]:[0-5][0-9] [0-3][0-9]\/[0-1][0-9]\/\d{4}", txt)
    if d == None:
        print('z')
    # d = d.group()
    print(d)
    return d

date1 = '18:11 23/08/2022'

changeDateCorrectWay(date1)

date2 = '2022/08/18 00:30'

changeDateCorrectWay(date2)
