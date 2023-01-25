import datetime
timestart = datetime.datetime.now()
debug = 0

if debug == 1:
    inputFile = 'TestData.txt'
else:
    inputFile = 'Data.txt'

def buildList(inputFile):
    theFile = open(inputFile).read().splitlines()
    sum = 0
    elves = []
    for line in theFile:
        if line:
            sum += int(line)
        else:
            elves.append(sum)
            sum = 0
    return elves

def findMax(elves):
    print(max(elves))

def findTop3(elves):
    elves.sort(reverse=True)
    sum = 0
    for this in range(0,3):
        sum += elves[this]
    print(sum)

findTop3(buildList(inputFile))
print(f'#Time to complete: {datetime.datetime.now() - timestart}')