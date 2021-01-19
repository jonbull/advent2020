import datetime
timestart = datetime.datetime.now()
acc = 0
i = 0
history = set()
instructions = []
temp =[]
theFile = 'Part1.txt'
rulesText = open(theFile).read().splitlines()
for rules in rulesText:
    temp = rules.split()
    instructions.append([temp[0],int(temp[1])])

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

print(f'#Acc: {acc}')
print(f'#Time to complete: {datetime.datetime.now() - timestart}')

#Acc: 1475
#Time to complete: 0:00:00.002000