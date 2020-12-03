import datetime

timestart = datetime.datetime.now()
targetValue = 0
theFile = 'Part1.txt'
sourceMap = open(theFile).read().splitlines()

column_bound = len(sourceMap[0]) - 1
row_bound = len(sourceMap) - 1
x = 0
y = 0


def istree(currentpos):
    if currentpos == '#':
        return 1
    else:
        return 0


while y < row_bound:
    if x+3 > column_bound:
        x = x + 2 - column_bound
    else:
        x += 3
    y += 1
    targetValue += istree(sourceMap[y][x])

print(f'#Tree Count: {targetValue}')
timeend = datetime.datetime.now()
print(f'#Time to complete: {timeend - timestart}')

#Tree Count: 203
#Time to complete: 0:00:00.000996