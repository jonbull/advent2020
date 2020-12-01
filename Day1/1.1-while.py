import datetime
timestart = datetime.datetime.now()
targetValue = 2020
solved = False
sourceFile = 'day1.txt'
sourceData = open(sourceFile)
sourceList = []

for row in sourceData:
    sourceList.append(int(row))

while len(sourceList) > 0 and not(solved):
    secondList = sourceList
    for i in secondList:
        if sourceList[0] + i == targetValue:
            print(f'{sourceList[0]} + {i} = {targetValue}, product is {sourceList[0]*i}')
            solved = True
            break
    sourceList.pop(0)

timeend = datetime.datetime.now()
print(f'Time to complete: {timeend - timestart}')
#Time to complete: 0:00:00.001000