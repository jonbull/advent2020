import datetime

timestart = datetime.datetime.now()
targetValue = 0
theFile = 'Part1.txt'

group = []
groupmember = set()

for record in open(theFile).readlines():
    record = record.rstrip()
    if len(record) > 0:
        for char in record: groupmember.add(char)
        group.append(groupmember.copy())
        groupmember.clear()
    else:
        targetValue += len(set.intersection(*group))
        group.clear()

targetValue += len(set.intersection(*group))
group.clear()

print(f'#Total Unique Trues: {targetValue}')
print(f'#Time to complete: {datetime.datetime.now() - timestart}')

#Total Unique Trues: 3570
#Time to complete: 0:00:00.005983
