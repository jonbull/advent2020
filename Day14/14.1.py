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

def apply(mask,bin):
    l = 0
    for l in range(0,len(bin)):
        if mask[l] != 'X':
            if int(mask[l]) != bin[l]: bin[l] = int(mask[l])
    return(bin)

theFile = 'Part1.txt'
program = open(theFile).read().splitlines()
memory = {}
for entry in program:
    action,value=entry.split(' = ')
    if action == 'mask':
        mask = []
        for imask in value[::-1]:
            mask.append(imask)

    else:
        bin =[]
        bin = decimaltobin(int(value))
        bin = apply(mask,bin)
        memory.update({action:bin})

solution = 0
for k in memory:
    solution += bintodecimal(memory[k])

print(f"#Solution = {solution}")
print(f'#Time to complete: {datetime.datetime.now() - timestart}')

#Solution = 15172047086292
#Time to complete: 0:00:00.016996