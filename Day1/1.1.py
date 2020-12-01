import datetime
timestart = datetime.datetime.now()
targetValue = 2020
solved = False
sourceFile = 'day1.txt'
sourceData = open(sourceFile)
sourceList = []

for row in sourceData:
    sourceList.append(int(row))

secondList = sourceList.copy()

for i in sourceList:
    for n in secondList:
        if i != n:
            if i + n == targetValue:
                print(f'{i} + {n} = {targetValue} - multiplication is {i*n}')
                break
    secondList.pop(0)

timeend = datetime.datetime.now()
print(f'Time to complete: {timeend - timestart}')
#Time to complete: 0:00:00.001966