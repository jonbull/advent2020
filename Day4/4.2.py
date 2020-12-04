import datetime
import re
timestart = datetime.datetime.now()
targetValue = 0
theFile = 'Part1.txt'

requiredFields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')


#Below we have a function to validate each type of field


def byr(value):
    if value <= 2002 and value >= 1920:
        return True
    else:
        return False

def iyr(value):
    if value <= 2020 and value >= 2010:
        return True
    else:
        return False

def eyr(value):
    if value >= 2020 and value <= 2030:
        return True
    else:
        return False

def hgt(value):
    if value[-2:] == 'cm':
        if int(value[:-2]) >= 150 and int(value[:-2]) <= 193:
            return True
    elif value[-2:] == 'in':
        if int(value[:-2]) >= 59 and int(value[:-2]) <= 76:
            return True
    return False

def hcl(value):
    if value[0] == '#' and re.findall("[0-9,a-f]{6}",value):
        return True
    return False

def ecl(value):
    validColors = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
    for entry in validColors:
        if entry == value:
            return True
    return False

def pid(value):
    if len(value) == 9 and re.findall("\d{9}",value):
        return True
    return False

#Similiar to the record ingestion from part 1, but this time we're going to create a dictionary instead of just a
#list of the keys


sourcefile = open(theFile).readlines()
collection = []
dict = {}
for line in sourcefile:
    if line != "\n":
        breakout = line.split()
        for pair in breakout:
            elements = pair.split(':')
            dict.update({elements[0]:elements[1]})
    else:
        collection.append(dict)
        dict = {}
collection.append(dict)


#Verify the record has the necessary fields


for record in collection:
    fieldsinrecord = record.keys()
    isGood = True
    for field in requiredFields:
        isFound = False
        for entry in fieldsinrecord:
            if entry == field:
                isFound = True
        if not isFound:
            isGood = False


#If all fields are present, validate the contents of the fields

    if isGood:
        if isGood and not byr(int(record['byr'])):
            isGood = False

        if isGood and not iyr(int(record['iyr'])):
            isGood = False

        if isGood and not eyr(int(record['eyr'])):
            isGood = False

        if isGood and not hgt(record['hgt']):
            isGood = False

        if isGood and not hcl(record['hcl']):
            isGood = False

        if isGood and not ecl(record['ecl']):
            isGood = False

        if isGood and not pid(record['pid']):
            isGood = False


#If we have all fields, and the fields are valid, increment our good record counter.

    if isGood: targetValue += 1


print(f'#Tree Count: {targetValue}')
timeend = datetime.datetime.now()
print(f'#Time to complete: {timeend - timestart}')

#Tree Count: 121
#Time to complete: 0:00:00.005010