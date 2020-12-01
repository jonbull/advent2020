import datetime
timestart = datetime.datetime.now()
solved = False
debug = False
targetValue = 2020

theFile = 'day1.txt'
sourceList = []
sourceData = open(theFile)

for row in sourceData:
    sourceList.append(int(row))

secondList = sourceList.copy()
thirdList = sourceList.copy()
if debug: print(f'{sourceList}')
for i in sourceList:
    for n in secondList:
        for x in thirdList:
            if i != n and i != x and n != x:
                if debug: print(f'{i} + {n} + {x}')
                if i + n + x == targetValue:
                    print(f'\n\n{i} + {n} + {x} = {targetValue} - multiplication is {i*n*x}\n\n')

timeend = datetime.datetime.now()
print(f'Time to complete: {timeend - timestart}')
#Time to complete: 0:00:02.133014