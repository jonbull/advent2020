import datetime
timestart = datetime.datetime.now()
success = False
instructions = []

theFile = 'sample.txt'

ridx = 0
rlist = []
rulesText = open(theFile).read().splitlines()
for rules in rulesText:
    temp = rules.split()
    instructions.append([temp[0],int(temp[1])])
    if temp[0] == 'nop' or temp[0] == 'jmp':
        rlist.append(ridx)
    ridx += 1

print(f'{instructions}')
print (f'{rlist}')