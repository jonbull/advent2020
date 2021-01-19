import datetime
timestart = datetime.datetime.now()
targetValue = 'shiny gold bag'
answer = 0
theFile = 'simple.txt'
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
            rules[prefix[0]].update({item[1]:int(item[0])})

def worktheproblem(targetValue,sol):
    if len(rules[targetValue].keys()) > 0:
        for k in rules[targetValue].keys():
            if len(rules[targetValue][k].keys()) = 0:
                sol += worktheproblem(rules[targetValue][k],0)


print(f'{rules}')
print(f'{worktheproblem(targetValue)}')

#print(f'#Bag: {targetValue} appears in {answer} nested bags')
#print(f'#Time to complete: {datetime.datetime.now() - timestart}')

#Bag: shiny gold bag appears in 246 nested bags
#Time to complete: 0:00:00.191043
