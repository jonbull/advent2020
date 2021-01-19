import datetime
timestart = datetime.datetime.now()
targetValue = 'shiny gold bag'
answer = 0
theFile = 'Part1.txt'
rulesText = open(theFile).read().splitlines()
rules = {}

for line in rulesText:
    prefix = line.split(' contain ')
    prefix[0] = prefix[0].rstrip('s')
    rules[prefix[0]] = {}
    if prefix[1] != 'no other bags.':
        prefix[1] = prefix[1].rstrip('.')
        suffix = prefix[1].split(', ')
        for entry in suffix:
            entry = entry.rstrip('s')
            item = entry.split(' ',1)
            rules[prefix[0]].update({item[1]:item[0]})

def hunt(i,workingSet):
    workingSet = [i]
    if len(rules[i].keys()) > 0:
        for x in rules[i].keys():
            workingSet+=(hunt(x,workingSet))
    return(workingSet)

for line in rules.keys():
    res = []
    if line != targetValue:
        if targetValue in hunt(line,res):
            answer += 1

print(f'#Bag: {targetValue} appears in {answer} nested bags')
print(f'#Time to complete: {datetime.datetime.now() - timestart}')

#Bag: shiny gold bag appears in 246 nested bags
#Time to complete: 0:00:00.191043