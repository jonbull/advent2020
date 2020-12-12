import datetime
import copy

debug = False
showmap = False
timestart = datetime.datetime.now()
map = []

if debug:
    theFile = 'testcase.txt'
else:
    theFile = 'Part1.txt'

for row in open(theFile).read().splitlines():
    newrow = []
    for char in row:
        newrow.append(char)
    map.append(newrow)

def togglechair(value):
    #If seat is empty (L), return occupied (#).
    #If seat is occupied (#), return empty (L).
    if value == 'L': return '#'
    elif value == '#': return 'L'

def observedseat(ox,oy,dx,dy,value):
    #Recursively determine if the space being observed contains a seat.  If seat, return value of seat.
    if debug: print(f' *1* - {dx},{dy} contains {value}')
    if value != '.':
        if debug: print(f' Done!')
        return value  # If the destination is a seat, return the value of the seat
    # Given the observers position and the destination of gaze, find the next space
    if ox > dx: newx = dx - 1#looking up
    elif ox < dx: newx = dx + 1#looking down
    else: newx = dx #no x change

    if oy > dy: newy = dy - 1#looking left
    elif oy < dy: newy = dy + 1 #looking right
    else: newy = dy #No y change

    if newx < 0 or newx > len(map)-1:
        if debug: print('Returning Z')
        return('Z') #New coordinate out of bounds, return invalid space
    if newy < 0 or newy > len(map[x])-1:
        if debug:print('Returning Z')
        return ('Z') #New coordinate out of bounds, return invalid space
    else:
        if debug: print(f' *2* - {dx},{dy} contains {value}\n     -> moving on to {newx},{newy} \n')
        value = observedseat(dx,dy,newx,newy,map[newx][newy])
    return value

def getsurroundingseats(ox,oy,map):
    #Return a list of surrounding seats for investigation
    solution = []
    for h in range(-1,2): #Builds an array of the 8 coordinates around the seat and the seat
        for v in range(-1,2):
            newx = ox+h
            newy = oy+v
            if (newx >= 0) and (newy >= 0) and (newx < len(map)) and (newy < len(map[ox])) and \
                    not(newy == oy and newx == ox):
                solution.append([newx,newy])
    return solution

hasChanged = True

while hasChanged:

    if showmap:
        print('\n\nStart Map\n')
        for row in map:
            for character in row:
                print(f'{character}', end='')
            print('')
        print('')

    hasChanged = False
    map2 = copy.deepcopy(map)                                       #make map2 that we can record to
    for x in range (0,len(map)):
        for y in range (0,len(map[x])):                             #Iterate through each seat in the map
            if map[x][y] != '.':                                    #If empty space take no action
                allseats = []
                if debug: print(f'Working on {x},{y}:')
                viablechairs = getsurroundingseats(x, y, map)           # For each surrounding seat
                for dx,dy in viablechairs:
                    if debug: print(f'Investigating destination {dx},{dy}')
                    allseats.append(observedseat(x,y,dx,dy,map[dx][dy])) #record the observed seat
                if debug: print(f'Investigation complete,\n{x},{y}-{map[x][y]} - Observes {allseats}\n\n')

                if map[x][y] == 'L' and allseats.count('#') == 0:       #ruleset for Sitting in an empty seat
                    if debug: print(f' - Sitting')
                    map2[x][y] = togglechair(map[x][y])  # toggle the chair
                    hasChanged = True

                if map[x][y] == '#' and allseats.count('#') > 4:       #if there are 5 or more occupied seats
                    if debug: print(f' - Standing')
                    map2[x][y] = togglechair(map[x][y])                 #toggle the chair
                    hasChanged = True                                   #note that a change has been made

    map = copy.deepcopy(map2)                                       #copy the working map into the source map
    if debug: hasChanged=False

if showmap:
    print('\n\nEnd Map\n')
    for row in map:
        for character in row:
            print(f'{character}', end='')
        print('')
    print('')

solution = 0
for row in map:
    for seat in row:
        if seat == '#': solution += 1

print(f"#solution: {solution}")
print(f'#Time to complete: {datetime.datetime.now() - timestart}')

#solution: 2199
#Time to complete: 0:00:09.809198
