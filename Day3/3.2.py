import datetime

timestart = datetime.datetime.now()
targetValue = 0
finalAnswer = 1
theFile = 'Part1.txt'
sourceMap = open(theFile).read().splitlines()

movelist = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
answerList = []
column_bound = len(sourceMap[0]) - 1
row_bound = len(sourceMap) - 1
x = 0
y = 0

def istree(currentpos):
    if currentpos == '#':
        return 1
    else:
        return 0

for currentrules in movelist:
    while y < row_bound:
        if x+currentrules[0] > column_bound:
            x = x + currentrules[0] - column_bound - 1
        else:
            x += currentrules[0]
        y += currentrules[1]
        targetValue += istree(sourceMap[y][x])
    answerList.append(targetValue)
    finalAnswer *= targetValue
    targetValue = 0
    x = 0
    y = 0

print(f'#Answer List: {answerList}, product is {finalAnswer}')
timeend = datetime.datetime.now()
print(f'#Time to complete: {timeend - timestart}')

#Answer List: [68, 203, 78, 77, 40], product is 3316272960
#Time to complete: 0:00:00.001027