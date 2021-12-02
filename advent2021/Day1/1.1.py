
if __name__ == '__main__':
    debug = 1
    if debug > 0:
        file = 'TestInput.txt.'
        file = 'Input.txt'
    else:
        file = 'Input.txt'

    inputlist = []
    filecontents = open(file)
    depthcnt = 0

#Not ten minutes in, and the IDE has saved my bacon :)

    for row in filecontents:
            inputlist.append(row.rstrip())

    idx = 0
    for row in inputlist:
        if idx != 0:
            if debug > 0:
                print (str(row),end='')
            if inputlist[idx-1] < inputlist[idx]:
                depthcnt += 1
                if debug > 0:
                    print(' (increased) depthcnt now '+str(depthcnt))
            else:
                if debug > 0:
                    print(' (decreased)')
        else:
            if debug > 0:
                print (str(row)+' (N/A - no previous measurement)')
        idx += 1
###Off by 1, but how?  to ve investigated later
print ('How many measurements are larger than the previous measurement? '+str(depthcnt))

