import datetime
import copy

timestart = datetime.datetime.now()
#theFile = 'testcase2.txt'
#theFile = 'testcase1.txt'
#theFile = 'testcase4.txt'
#theFile = 'testcase3.txt'
#theFile = 'testcase5.txt'
theFile = 'Part1.txt'



target,sched = open(theFile).read().splitlines()
target = int(target)
sched = sched.split(',')
vsched = []

for i in range(0,len(sched)):
    if sched[i] != 'x':
        sched[i] = int(sched[i])
        vsched.append(int(sched[i]))

highbus = max(vsched)
highbus_offset = sched.index(highbus)

lowbus = min(vsched)
lowbus_offset = sched.index(lowbus)

highcount = 1
lowcount = 1

while ((((highbus*highcount)-highbus_offset)+lowbus_offset)%lowbus) != 0:
    highcount += 1

i = 0
timestamp = 0
success = False
highcount = 1
while not success:
    i += 1
    timestamp = (i * highbus * highcount) - highbus_offset
    success = True
    for bus in vsched:
        if (timestamp+sched.index(bus)) % bus != 0:
            success = False

    if success:
        print(f'#Iteration = {i}')
        print(f'#Timestamp = {timestamp}')
        print(f'#Time to complete: {datetime.datetime.now() - timestart}')

#Timestamp = 1202161486
#Time to complete: 0:00:21.723110