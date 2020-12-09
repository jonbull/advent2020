import datetime
timestart = datetime.datetime.now()

theFile = 'part1.txt'
base = []
i = open(theFile).read().splitlines()
for line in i: base.append(int(line))
preamble = 25
idx = preamble
success = False

while not success:
    success = True
    target = idx+1
    for a in base[(idx-preamble):target]:
        for b in base[(idx-preamble):target]:
            if a != b:
                if a+b == base[target]:
                    success = False
                    break
    idx+=1
    if success:
        targetnumber = base[target]

#print(f'{base}')
success = False
idx = 0
bottom = 0
while not success:
    target = 0
    idx = bottom
    #print(f'{targetnumber}... ',end='')
    while target < targetnumber:
        target += base[idx]
        #print(f'{base[idx]} ({target}) + ', end='')
        idx += 1

    if target == targetnumber:
        answer = min(base[bottom:idx]) + max(base[bottom:idx])
        success = True
    else:
        bottom += 1
        print()

print(f'#Number: {answer}')
print(f'#Time to complete: {datetime.datetime.now() - timestart}')

#Number: 23463012
#Time to complete: 0:00:00.114695