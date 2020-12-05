"""
This one we cheesed and did the barest of minimums.

The requirement was that we  records have the required fields...

Which is to say we only care about the field labels and not the contents.
"""

import datetime
timestart = datetime.datetime.now()
targetValue = 0
theFile = 'Part1.txt'
requiredFields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

"""
Open the file, read lines until we come up to a blank line.
Split the line into elements based on " " (blank space.)
Split that element based on the ":"
Add the key to a list for that record.
When we hit a blank line "\n" write that list to a list of lists
"""

sourcefile = open(theFile).readlines()
collection = []
record = []
for line in sourcefile:
    if line != "\n":
        breakout = line.split()
        for pair in breakout:
            elements = pair.split(':')
            record.append(elements[0])
    else:
        collection.append(record)
        record = []

"""
For each of the lists we created
...compare the requiredFields variable to the content of the list.  
If a member of requiredFields isn't present, the record is invalid.
Otherwise increment our valid list.    
"""

for record in collection:
    isGood = True
    for rule in requiredFields:
        if rule not in record:
            isGood = False
    if isGood: targetValue += 1

print(f'#Valid Records: {targetValue}')
timeend = datetime.datetime.now()
print(f'#Time to complete: {timeend - timestart}')

#Valid Records: 190
#Time to complete: 0:00:00.002994