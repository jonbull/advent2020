import datetime

timestart = datetime.datetime.now()
targetValue = 0
theFile = 'part1.txt'

records = []
answers = set()
sourcefile = open(theFile).readlines()

for record in sourcefile:
    if record != "\n":
        for letter in record:
            if letter != '\n':
                answers.add(letter)
    else:
        records.append(answers.copy())
        answers.clear()

records.append(answers.copy())

for line in records:
    targetValue += len(line)

print(f'#Total Unique Trues: {targetValue}')
print(f'#Time to complete: {datetime.datetime.now() - timestart}')

#Total Unique Trues: 7120
#Time to complete: 0:00:00.004984
