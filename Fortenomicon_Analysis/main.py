# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import openpyxl as openpyxl
import pandas as pd

class book:
    def __init__(self,fileloc,mode):
        self.fileloc = fileloc
        self.mode = 1
        print( "File location is " + self.fileloc)
        self.df = pd.DataFrame()
        #self.df = pd.read_excel("C:\\Users\\Jon\\Desktop\\Fortenomicon.xlsx", engine="openpyxl", sheet_name=2)
        self.df = pd.read_excel("C:\\Users\\Jon\\Desktop\\Fortenomicon.xlsx", engine="openpyxl")

    def findrank(self,idx,value):
        explace = 0
        for e in range(0, len(idx)):
            if value == idx[e]:
                return(e+1)


    def volume(self):
        dateidx = set()

        for days in self.df['Day']:
            dateidx.add(days)

        exerciseidx = ['Squat','Bench','Deadlift']

        for exercise in exerciseidx:

            volume = dict()
            volumeidx = list()
            dayidx = list()

            for days in dateidx:
                workingdata = self.df.query('Day == @days and Exercise == @exercise')
                mysum = 0
                for vol in workingdata['Total']:
                    mysum += vol
                if mysum > 0:
                    volume.update({mysum: days})
                    volumeidx.append(int(mysum))
                    dayidx.append(days)

            volumeidx.sort(reverse=True)
            dayidx.sort(reverse=True)

            print('Exercise: '+exercise)
            print('Total Sessions: ' + str(len(dayidx)))
            print('Average Volume: '+ str(sum(volumeidx)/len(volumeidx)))

            for e in volume.keys():
                if volume[e] == dayidx[0]:
                    exvolume = e

            print('Most Recent: ')
            print(str(self.findrank(volumeidx,exvolume))+' '+str(dayidx[0])[0:10]+' '+str(exvolume))
            print()

            if len(volumeidx) >= 3: toplimit = 3
            else: toplimit = len(volumeidx)

            for idx in range(0,toplimit):
                print(idx+1, end=' ')
                print(str(volume.get(volumeidx[idx]))[0:10],end=' ')
                print(volumeidx[idx])
            print()

    def weight(self):
        dateidx = list()
        exerciseidx = list()
        for days in self.df['Day']:
            dateidx.append(days)

        dateidx.sort(reverse=True)
        targetday = dateidx[0]
        targetdatedata = self.df.query('Day == @targetday')

        for exercise in targetdatedata['Exercise']:
            if exercise not in (exerciseidx):
                exerciseidx.append(exercise)

        for targetexercise in exerciseidx:
            workingdata = self.df.query('Day == @targetday and Exercise == @exercise')
            targetreps = 0

            for reps in workingdata['Reps']:
                if targetreps < reps:
                    targetreps = reps

            workingdata = self.df.query('Reps == @targetreps and Exercise == @targetexercise and Day == @targetday')
            targetweight = 0

            for weight in workingdata['Weight']:
                if targetweight < weight:
                    targetweight = weight

            workingdata = self.df.query('Reps == @targetreps and Exercise == @targetexercise')
            masterlist = dict()
            weightidx = list()
            for day in workingdata.index:
                masterlist.update({workingdata['Weight'][day]:workingdata['Day'][day]})
                weightidx.append(workingdata['Weight'][day])

            weightidx.sort(reverse=True)



            print('Exercise: '+targetexercise)
            print('Reps: ' + str(targetreps))
            print('Average Weight: '+ str(sum(weightidx)/len(weightidx)))
            print('Most Recent: \n')
            print(str(self.findrank(weightidx, targetweight))+' '+str(dateidx[0])[0:10]+' '+str(targetweight))
            print()
            if len(weightidx) >= 3: toplimit = 3
            else: toplimit = len(weightidx)

            for idx in range(0,toplimit):
                print(idx+1, end=' ')
                print(str(masterlist.get(weightidx[idx]))[0:10], end=' ')
                print(weightidx[idx])
            print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fileloc = 'C:\\Users\\Jon\\Desktop\\Fortenomicon\.xlsx'
    mybook = book(fileloc, 1)
    mybook.volume()
    mybook.weight()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
