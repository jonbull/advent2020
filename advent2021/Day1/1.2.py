
if __name__ == '__main__':
    debug = 0
    if debug > 0:
        file = 'TestInput.txt.'
        #file = 'Input.txt'
    else:
        file = 'Input.txt'

    inputlist = []
    filecontents = open(file)
    depthcnt = 0

#Not ten minutes in, and the IDE has saved my bacon :)

    for row in filecontents:
            inputlist.append(int(row.rstrip()))

    for row in range(3,len(inputlist)):
        if debug > 0: print('Row: '+str(row))
        pval = 0
        cval = 0
        for val in range(0,3):
            if debug > 0: print('Val = '+str(val))
            if debug > 0: print('PVAL = ' + str(row-val-1),end='')
            if debug > 0: print(' CVAL = ' + str(row-val))
            pval += inputlist[row-val-1]
            cval += inputlist[row-val]

        if row > 2:
            if debug > 0: print ('\n'+str(cval),end='')
            if cval > pval:
                depthcnt += 1
                if debug > 0: print(' (increased) depthcnt now '+str(depthcnt))
            else:
                if debug > 0: print(' (decreased)')
        else:
            if debug > 0: print (str(row)+' (N/A - no previous measurement)')

print ('How many measurements are larger than the previous measurement? '+str(depthcnt))