import datetime

timestart = datetime.datetime.now()
targetValue = 0
theFile = 'Part1.txt'

group = []
groupmember = set()
answers = []
records = []
sourcefile = open(theFile).readlines()

for record in sourcefile:
    if record != "\n":
        for character in record:
            if character != '\n':
                groupmember.add(character)
        group.append(groupmember.copy())
        groupmember.clear()
    else:
        records.append(set.intersection(*group))
        group.clear()

records.append(set.intersection(*group))
group.clear()

for line in records:
    targetValue += len(line)

print(f'#Total Unique Trues: {targetValue}')
print(f'#Time to complete: {datetime.datetime.now() - timestart}')

#Total Unique Trues: 3570
#Time to complete: 0:00:00.008002
