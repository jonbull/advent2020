import datetime
timestart = datetime.datetime.now()

results = [10,16,6,0,1,17]
i = len(results)
target = 2020-1
guess = int()
debug = False
while i <= target:
    if debug: print(f'Turn {i} Last Guess {results[-1]} ',end='')
    if results[-1] not in results[:(len(results)-1)]:
        if debug: print(f' ...Result not in list... ',end='')
        guess = 0
        if debug: print(f'makes this guess {guess}')
    else:
        if debug: print(f' ...Result IN list... ', end='')
        h = int()
        for z in range(0,len(results)-1):
            if (results[-1] == results[z]): h = z+1
        guess = i-h
        if debug: print(f'was in position {h} makes this guess ({i}-{h} = {guess})')
    results.append(guess)
    i += 1

print(f'#Solution = {results[-1]}')
print(f'#Time to complete: {datetime.datetime.now() - timestart}')

#Solution = 412
#Time to complete: 0:00:00.154963