import datetime
timestart = datetime.datetime.now()

theFile = 'Part1.txt'
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
        print(f'#Number: {base[target]}')
        print(f'#Time to complete: {datetime.datetime.now() - timestart}')

#Number: 177777905
#Time to complete: 0:00:00.074830