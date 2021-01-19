import datetime
import copy

timestart = datetime.datetime.now()
map = []

theFile = 'Part1.txt'
for row in open(theFile).read().splitlines():
    newrow = []
    for char in row:
        newrow.append(char)
    map.append(newrow)

def getsurroundingseats(x,y,map):

    seats = []
    seatsleft = False
    seatsright = False
    rowbehind = False
    rowahead = False

    if y - 1 >= 0: seatsleft = True
    if y + 1 < len(map[x]): seatsright = True
    if x - 1 >= 0: rowbehind = True
    if x + 1 < len(map): rowahead = True

    if seatsleft:
        seats.append(map[x][y-1])
        if rowbehind: seats.append(map[x-1][y-1])
        if rowahead: seats.append(map[x+1][y-1])

    if seatsright:
        seats.append(map[x][y+1])
        if rowbehind: seats.append(map[x-1][y+1])
        if rowahead: seats.append(map[x+1][y+1])

    if rowahead: seats.append(map[x+1][y])
    if rowbehind: seats.append(map[x-1][y])

    #print(f'Evaluating {x},{y} sl = {seatsleft} sr = {seatsright} rb = {rowbehind} and ra = {rowahead} and found {seats}')
    if map[x][y] == 'L':
        if '#' in seats: return False
        else: return True

    if map[x][y] == '#':
        if seats.count('#') < 4: return False
        else: return True


def flipseat(value):
    if value == '#': return 'L'
    if value == 'L': return '#'

ischanged = True
while ischanged:
    ischanged = False
    map2 = copy.deepcopy(map)
    for x in range(0,len(map)):
        for y in range(0,len(map[x])):
            if getsurroundingseats(x,y,map):
                ischanged = True
                map2[x][y]=flipseat(map[x][y])
    map = copy.deepcopy(map2)

solution = 0
for row in map:
    for seat in row:
        if seat == '#': solution += 1

print(f"#solution: {solution}")
print(f'#Time to complete: {datetime.datetime.now() - timestart}')

#Number: 177777905
#Time to complete: 0:00:00.074830