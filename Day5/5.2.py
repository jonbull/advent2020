import datetime
import re
import math

timestart = datetime.datetime.now()
targetValue = 0
theFile = 'Part1.txt'

sourcefile = open(theFile).readlines()
seat_map = []
flight_map = []
for i in range(0,8): seat_map.append(0)
for i in range(0,128): flight_map.append(seat_map.copy())

def  getSeatId(row,seat):
    return (row * 8) + seat

def  myseat(row,seat):
    print(f'#My Seat ID is {getSeatId(rownum, seatnum)} (Row {rownum} Seat {seatnum})')


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

    flight_map[row][seat] = 1

for rownum in range(0,len(flight_map)):
    for seatnum in range (0,len(flight_map[rownum])):
        if flight_map[rownum][seatnum] == 0: #The seat is empty!  Lets see if it's our seat
            if seatnum > 0 and seatnum < 7: #We know the seats before and after are on the same row
                if flight_map[rownum][seatnum-1] == 1 and flight_map[rownum][seatnum+1] == 1:
                    myseat(rownum,seatnum)
            elif seatnum == 0 and rownum != 0: #Suspect seat is first in the row, and we aren't on the first row
                if flight_map[rownum-1][7] == 1 and flight_map[rownum][seatnum + 1] == 1:
                    myseat(rownum, seatnum)
            elif seatnum == 7 and rownum != 127: #Suspect seat is last in the row, and we aren't on the last row
                if flight_map[rownum+1][0] == 1 and flight_map[rownum][seatnum + 1] == 1:
                    myseat(rownum, seatnum)

print(f'#Time to complete: {datetime.datetime.now() - timestart}')

#My Seat ID is 517 (Row 64 Seat 5)
#Time to complete: 0:00:00.005984