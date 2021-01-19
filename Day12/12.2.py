import datetime
import copy

timestart = datetime.datetime.now()
direction = []

theFile = 'Part1.txt'
for row in open(theFile).read().splitlines():
    direction.append(row)

class boat():

    def __init__(self):
        self.ns = 0
        self.ew = 0
        self.orientation = 'E'

    def __repr__(self):
        print(f'Location NS={self.ns} EW={self.ew}')

    def rotate(self,direction,degrees):
        factor = int(degrees/90)
        for r in range(0,factor):

            tempns = self.ns
            tempew = self.ew

            if direction == 'R':
                self.ew = tempns
                self.ns = tempew*-1
            if direction == 'L':
                self.ew = tempns*-1
                self.ns = tempew

    def move(self,arbor,units):

        if arbor == 'N':
            self.ns += units
            return self.ns
        elif arbor == 'S':
            self.ns -= units
            return self.ns
        elif arbor == 'W':
            self.ew -= units
            return self.ew
        elif arbor == 'E':
            self.ew += units
            return self.ew

titanic = boat();
waypoint = boat();

waypoint.ns = titanic.ns + 1
waypoint.ew = titanic.ew + 10

for instruction in direction:

    if instruction[0] in ['N','S','E','W']:
        waypoint.move(instruction[0],int(instruction[1:]))

    if instruction[0] in ['F']:
        for i in range(0,int(instruction[1:])):
            titanic.ns += waypoint.ns
            titanic.ew += waypoint.ew

    if instruction[0] in ['L','R']:
        waypoint.rotate(instruction[0],int(instruction[1:]))

solution = abs(titanic.ew) + abs(titanic.ns)

print(f"#solution: {solution}")
print(f'#Time to complete: {datetime.datetime.now() - timestart}')

#solution: 52866
#Time to complete: 0:00:00.006964