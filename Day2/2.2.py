import datetime
timestart = datetime.datetime.now()
solved = False
debug = False
targetValue = 0

theFile = 'Day1.txt'
sourceList = []
sourceData = open(theFile)


def keybuilder(row):

    components = row.split()

    mykey = {
        'minVal':int(components[0].split('-')[0]),
        'maxVal':int(components[0].split('-')[1]),
        'letter':components[1][0],
        'password':components[2]
    }

    return mykey


def keyeval(mykey, targetvalue):
    correctish = 0
    if mykey['password'][mykey['minVal'] - 1] == mykey['letter']: correctish += 1
    if mykey['password'][mykey['maxVal'] - 1] == mykey['letter']: correctish += 1
    if correctish == 1:
        targetvalue += 1
    return targetvalue


for row in sourceData:
    targetValue = keyeval(keybuilder(row),targetValue)

print(f'#Valid Passwords: {targetValue}')
timeend = datetime.datetime.now()
print(f'#Time to complete: {timeend - timestart}')

#Valid Passwords: 705
#Time to complete: 0:00:00.001999