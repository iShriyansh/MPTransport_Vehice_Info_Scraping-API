
data = [['Sr No.', 'Class Name.', 'Issued On', 'Valid Till', 'Badge No', 'Badge No Old', 'Badge Valid From', 'Badge Valid To'], ['1', 'M/C with Gear', '03-10-2019', '02-10-2039', '', '', '', ''], ['2', 'Light Motor Vehicle-NT', '03-10-2019', '02-10-2039', '', '', '', '']]
dictx = {}

for i in range(1,len(data)):

    dictx[str(i)] = dict(zip(data[0],data[i]))


print(dictx)