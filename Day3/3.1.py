import datetime

timestart = datetime.datetime.now()
solved = False
debug = True
targetValue = 0

theFile = 'Part1.txt'
sourceMap = open(theFile).read().splitlines()

column_bound = len(sourceMap[0]) - 1
row_bound = len(sourceMap) - 1

x = 0
y = 0


def istree(currentpos):
    print (currentpos, end = '')
    if currentpos == '#':
        return 1
    else:
        return 0

targetValue += istree(sourceMap[y][x])
while y < row_bound:
    for xmove in [1,2,3]:
        if x+1 > column_bound:
            x = 0
        else:
            x += 1
        targetValue += istree(sourceMap[y][x])
    y += 1
    targetValue += istree(sourceMap[y][x])
    print('')

print(f'Target Value = {targetValue}')
print(f'X in sourceMap = {len(sourceMap[0])}')
print(f'Y in sourceMap = {len(sourceMap)}')
print(f'Right Bound in sourceMap = {column_bound}')
print(f'Bottom Bound in sourceMap = {row_bound}')

# print(f'#Valid Passwords: {targetValue}')
# timeend = datetime.datetime.now()
# print(f'#Time to complete: {timeend - timestart}')
