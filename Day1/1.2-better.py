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

while len(sourceList) > 0:
    secondList = sourceList.copy()
    while len(secondList) > 0:
        if sourceList[0] + secondList[0] < targetValue:
            thirdList = secondList
            for value in thirdList:
                if sourceList[0] + secondList[0] + value == targetValue:
                    print(f'{sourceList[0]} + {secondList[0]} + {value} = {targetValue} - multiplication is {sourceList[0]*secondList[0]*value}')
                    solved = True
                    break
            secondList.pop(0)
        else:
            secondList.pop(0)
    sourceList.pop(0)

timeend = datetime.datetime.now()
print(f'Time to complete: {timeend - timestart}')
#1144 + 372 + 504 = 2020 - multiplication is 214486272
#Time to complete: 0:00:00.013000

