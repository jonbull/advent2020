import datetime

timestart = datetime.datetime.now()
finalAnswer = 1
theFile = 'Part1.txt'
sourceMap = open(theFile).read().splitlines()

movelist = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

for currentrules in movelist:
    targetValue = 0
    x = 0
    y = 0
    while y < (len(sourceMap) - 1):
        if x+currentrules[0] > (len(sourceMap[0]) - 1):
            x = x + currentrules[0] - (len(sourceMap[0]) - 1) - 1
        else:
            x += currentrules[0]
        y += currentrules[1]
        if sourceMap[y][x] == '#': targetValue += 1
    finalAnswer *= targetValue


print(f'#Product is {finalAnswer}')
print(f'#Time to complete: {datetime.datetime.now() - timestart}')

#Product is 3316272960
#Time to complete: 0:00:00.000998