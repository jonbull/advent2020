import datetime
timestart = datetime.datetime.now()

theFile = 'sample1.txt'
adapter = []
i = open(theFile).read().splitlines()
for line in i: adapter.append(int(line))

x = [1,3,4,7]
"""
Expected output is
[1,3,4,7]
[1,4,7]
"""
path = [[1],[1]]
def go(path):
    for route in path:
        for i in [1,2,3]:
            if route+i in x:
                print(route+i)

go (path)

#print(f"#Number: {branches}")
#print(f'#Time to complete: {datetime.datetime.now() - timestart}')

#Number: 177777905
#Time to complete: 0:00:00.074830