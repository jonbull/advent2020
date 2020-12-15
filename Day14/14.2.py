import datetime
timestart = datetime.datetime.now()

def buildbin(): #Builds an empty array of binday values
    bin = []
    for loop in range(0,36):
        bin.append(0)
    return bin

def decimaltobin(value): #Given a decimal value, creates a binary array of equal value
    bin = buildbin()
    for l in range(len(bin)-1,-1,-1):
        if value >= 2 ** l:
            bin[l] = 1
            value -= 2 ** l
        else:
            bin[l] = 0
    return bin

def bintodecimal(bin):
    v = 0
    for l in range(0,len(bin)):
        if bin[l] == 1:
            v += 2 ** l
    return v

def bintodecimalv2(bin):
    v = 0
    numx = 0
    numx = bin.count('X')
    numx = 2 ** numx
    print(f'bin = {bin} \nnumx = {numx}')
    for l in range(0,len(bin)):
        if bin[l] == 1:
            print(f'Pos {l} is {bin[l]} evals at {2 ** l} ', end='')
            print(f' * {int(numx)} or {(2 ** l) * int(numx)}')
            v += (2 ** l) * int(numx)
        elif bin[l] == 'X':
            print(f'Pos {l} is {bin[l]} evals at {2 ** l} ', end='')
            print(f' * {int(numx/2)} or {(2 ** l) * int((numx/2))}')
            v += (2 ** l) * int((numx/2))
    return v

def applyv2(mask,bin):
    l = 0
    for l in range(0,len(bin)):
        if mask[l] != 'X':
            if int(mask[l]) == 1: bin[l] = 1
        else: bin[l] = 'X'
    return(bin)

theFile = 'simple.txt'
program = open(theFile).read().splitlines()
memory = {}
for entry in program:
    action,value=entry.split(' = ')
    if action == 'mask':
        mask = []
        for imask in value[::-1]:
            mask.append(imask)

    else:
        value = action.split('[')
        value = value[1][:len(value)]
        bin = decimaltobin(int(value))
        memory.update({applyv2(mask,bin):1})

solution = 0

for k in memory.keys():
    solution += k

print(f"#Solution = {solution}")
print(f'#Time to complete: {datetime.datetime.now() - timestart}')

#Solution = 15172047086292
#Time to complete: 0:00:00.016996