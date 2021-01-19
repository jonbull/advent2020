import datetime
timestart = datetime.datetime.now()
success = False
instructions = []

ridx = 0
rlist = []

theFile = 'Part1.txt'
rulesText = open(theFile).read().splitlines()
for rules in rulesText:
    temp = rules.split()
    instructions.append([temp[0],int(temp[1])])
    if temp[0] == 'nop' or temp[0] == 'jmp':
        rlist.append(ridx)
    ridx += 1

def flip(value):
    if value == 'nop': return 'jmp'
    else: return 'nop'

print(f'{instructions}')
print(f'{rlist}')

ridx = 0
while not success:
    acc = 0
    i = 0
    history = set()

    instructions[rlist[ridx]][0] = flip(instructions[rlist[ridx]][0])
    if ridx != 0:
        instructions[rlist[ridx-1]][0] = flip(instructions[rlist[ridx-1]][0])
    ridx += 1

    while i not in history:
        if instructions[i][0] == 'nop':
            history.add(i)
            i += 1
        elif instructions[i][0] == 'jmp':
            history.add(i)
            i += instructions[i][1]
        elif instructions[i][0] == 'acc':
            acc += instructions[i][1]
            history.add(i)
            i += 1

        if i >= len(instructions):
            success = True
            break

print(f'#Acc: {acc}')
print(f'#Time to complete: {datetime.datetime.now() - timestart}')

#Acc: 1270
#Time to complete: 0:00:00.018264
