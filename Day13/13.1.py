import datetime
import copy

timestart = datetime.datetime.now()
direction = []

theFile = 'Part1.txt'
target,sched = open(theFile).read().splitlines()
target = int(target)
sched = sched.split(',')

bussched=[]

for bus in sched:
    workingbus = {}
    if bus != 'x':
        bus = int(bus)
        busmath = target % bus
        workingbus['name'] = bus
        workingbus['result'] = busmath
        workingbus['nextvisit'] = target - busmath + bus
        bussched.append(workingbus)

bestbus = bussched[0]
for bus in bussched[1:]:
    if bus['nextvisit'] < bestbus['nextvisit']: bestbus = bus

print(f"#BusID = {(bestbus['nextvisit']-target)*bestbus['name']}")
print(f'#Time to complete: {datetime.datetime.now() - timestart}')

#BusID = 2845
#Time to complete: 0:00:00.000997