import datetime
timestart = datetime.datetime.now()

results = [1,3,6]
target = 4
debug = True

def buildrd(results):
    rd = {}
    t = 1
    for r in results:
        rd[r] = t
        t += 1

    return rd

rd = buildrd(results)

if debug: print(f'Starting rd {rd}')

guess = results[0]

for n in results:
    print(n)

i = 4
while i <= target:
    if debug: print(f'iteration {i}, guess {guess} ',end='')
    if guess in rd.keys():
        if debug: print(f' last at {rd.get(guess)} ', end='')
        rd[i - rd.get(guess)] = i
        if debug: print(f'number spoken iteration - last at {i - rd.get(guess)}')
    if guess not in rd.keys():
        rd[guess] = i

    i += 1

#Expected resuts 0,3,6,0,3,1,0,4,0
print(f'#Solution = {guess}')
print(f'#Time to complete: {datetime.datetime.now() - timestart}')

#Solution = 412
#Time to complete: 0:00:00.154963