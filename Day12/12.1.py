import datetime
import copy

timestart = datetime.datetime.now()
direction = []

theFile = 'part1.txt'
for row in open(theFile).read().splitlines():
    direction.append(row)

class boat():

    def __init__(self):
        self.ns = 0
        self.ew = 0
        self.orientation = 'E'

    def rotate(self,direction,degrees):
        factor = int(degrees/90)
        for r in range(0,factor):
            if direction == 'L':
                if self.orientation == 'N':self.orientation = 'W'
                elif self.orientation == 'W': self.orientation = 'S'
                elif self.orientation == 'S': self.orientation = 'E'
                elif self.orientation == 'E': self.orientation = 'N'

            if direction == 'R':
                if self.orientation == 'N': self.orientation = 'E'
                elif self.orientation == 'W': self.orientation = 'N'
                elif self.orientation == 'S': self.orientation = 'W'
                elif self.orientation == 'E': self.orientation = 'S'

        return(self.orientation)

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

for instruction in direction:

    #print(f'{instruction[0]} and {instruction[1:]}')
    if instruction[0] in ['N','S','E','W']:
        titanic.move(instruction[0],int(instruction[1:]))

    if instruction[0] in ['F']:
        titanic.move(titanic.orientation,int(instruction[1:]))

    if instruction[0] in ['L','R']:
        titanic.rotate(instruction[0],int(instruction[1:]))

    #print(f'NS = {titanic.ns} EW = {titanic.ew}')

solution = abs(titanic.ew) + abs(titanic.ns)

print(f"#solution: {solution}")
print(f'#Time to complete: {datetime.datetime.now() - timestart}')

#solution: 1603
#Time to complete: 0:00:00.002024