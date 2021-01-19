import datetime

timestart = datetime.datetime.now()
targetValue = 0
theFile = 'part1.txt'

records = []
answers = set()

for templine in open(theFile).readlines():
    record = templine.rstrip()
    if len(record) > 0:
        for letter in record: answers.add(letter)
    else:
        targetValue += len(answers)
        answers.clear()
targetValue += len(answers)

print(f'#Total Unique Trues: {targetValue}')
print(f'#Time to complete: {datetime.datetime.now() - timestart}')

#Total Unique Trues: 7120
#Time to complete: 0:00:00.003989
