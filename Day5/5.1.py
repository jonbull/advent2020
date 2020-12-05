import datetime
import re
import math

timestart = datetime.datetime.now()
targetValue = 0
theFile = 'Part1.txt'

sourcefile = open(theFile).readlines()


def getSeatId(row,seat):
    return (row * 8) + seat

for record in sourcefile:
    row = 0
    seat = 0
    curr_row = [0, 127]
    curr_seat = [0, 7]

    for prefix in record[0:7]:
        if prefix == 'F':
            curr_row[1] -= math.ceil((curr_row[1] - curr_row[0]) / 2)
        else:
            curr_row[0] += math.ceil((curr_row[1] - curr_row[0]) / 2)

    if record[:7] == 'F':
        row = curr_row[0]
    else:
        row = curr_row[1]

    for suffix in record[7:10]:
        if suffix == 'L':
            curr_seat[1] -= math.ceil((curr_seat[1] - curr_seat[0]) / 2)
        else:
            curr_seat[0] += math.ceil((curr_seat[1] - curr_seat[0]) / 2)

    if record[:10] == 'L':
        seat = curr_seat[0]
    else:
        seat = curr_seat[1]

    if targetValue < getSeatId(row, seat): targetValue = getSeatId(row, seat)

print(f'#Highest Seat Value: {targetValue}')
print(f'#Time to complete: {datetime.datetime.now() - timestart}')

#Highest Seat Value: 832
#Time to complete: 0:00:00.009973
