import datetime
timestart = datetime.datetime.now()

theFile = 'Part1.txt'
adapter = []
i = open(theFile).read().splitlines()
for line in i: adapter.append(int(line))

joltfactor = 0
cjoltfactor = 0
answer = {'single':0,
          'triple':1}

for l in range (0,len(adapter)):
    for jf in range(1,4):
        joltfactor += 1
        if joltfactor in adapter:
            if jf == 1: answer['single'] += 1
            if jf == 3: answer['triple'] += 1
            adapter.remove(joltfactor)
            break


print(f"#Number: {answer['single']*answer['triple']}")
print(f'#Time to complete: {datetime.datetime.now() - timestart}')

#Number: 177777905
#Time to complete: 0:00:00.074830