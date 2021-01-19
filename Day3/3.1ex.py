import datetime

timestart = datetime.datetime.now()
theFile = 'Part1.txt'
sourceMap = open(theFile).read().splitlines()
targetValue = 0
x = 0
y = 0

while y < len(sourceMap) - 1:
    if x+3 > (len(sourceMap[0]) - 1):
        x = x + 2 - (len(sourceMap[0]) - 1)
    else:
        x += 3
    y += 1
    if sourceMap[y][x] == '#': targetValue += 1

print(f'#Tree Count: {targetValue}')
print(f'#Time to complete: {datetime.datetime.now() - timestart}')

#Tree Count: 203
#Time to complete: 0:00:00.000971