import datetime
timestart = datetime.datetime.now()

ruleorder = []
data = {}
data['near']=[]
data['rule']={}
tickets = {}
sol = 0

theFile = 'Part1.txt'
program = open(theFile).read().splitlines()
state = 1
for entry in program:

    if entry == '':
        state += 1
        ruleset = []

    if state == 1:
        name,rules=entry.split(': ')
        ruleorder.append(name)
        ruleset=rules.split(' or ')
        master = []
        for rs in ruleset:
            min,max=rs.split('-')
            master.append({'min':int(min),'max':int(max)})
        data['rule'][name] = master

    if state == 2:
        if ',' in entry:
            ruleset=entry.split(',')
            data['me']=[ruleset]

    if state == 3:
        master=[]
        if ',' in entry:
            master=entry.split(',')
            data['near'].append(master)

for entry in data['near']:
    for v in entry:
        passed = False
        for crule in data['rule']:
            for rulecondition in data['rule'][crule]:
                if int(v) <= rulecondition['max']:
                    if int(v) >= rulecondition['min']:
                        passed = True
                if passed: break
            if passed: break
        if not passed:
            sol += int(v)



print(f"#Solution = {sol}")
print(f'#Time to complete: {datetime.datetime.now() - timestart}')

#Solution = 19240
#Time to complete: 0:00:00.004999
