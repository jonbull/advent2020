import time
start = time.perf_counter()

if __name__ == '__main__':

    file = 'Input.txt'
    inputlist = []
    filecontents = open(file)
    depthcnt = 0

    for row in filecontents:
            inputlist.append(int(row.rstrip()))

    for row in range(len(inputlist)):
        if row != 0:
            if inputlist[row-1] < inputlist[row]:
                depthcnt += 1

print ('#How many measurements are larger than the previous measurement? '+str(depthcnt))
print ('#Time:'+str((time.perf_counter() - start)))
#How many measurements are larger than the previous measurement? 1548
#Time:0.0019495
