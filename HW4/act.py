import os
import re

def selection_sort(arr):        
    for i in range(len(arr)):
        minimum = i
        
        for j in range(i + 1, len(arr)):
            # Select the smallest value
            if arr[j][finishTime] > arr[minimum][finishTime]:
                minimum = j

        # Place it at the front of the 
        # sorted end of the array
        arr[minimum], arr[i] = arr[i], arr[minimum] # one liner swap
    return arr


fileLocation = os.getcwd() + "/act.txt"
print fileLocation
myfile = open(fileLocation,"r")

#
# wrap this with an EOF condition
#+

#
# variable declarations
#
taskNumber = 0
startTime= 1
finishTime= 2

#get number of tasks
numberOfTasks = int(myfile.readline())

#
# initialize information array
#

info = [None] * (numberOfTasks)
print ("Number of tasks: {}").format(numberOfTasks)
for row in range(len(info)):
    info[row] = [-1] * 3 # 3 being number of pieces of information given. 

for task in range(len(info)):
    line = myfile.readline()
    line_array = list(map(int, line.split()))
    info[task][taskNumber] = line_array[taskNumber]
    info[task][startTime] = line_array[startTime]
    info[task][finishTime] = line_array[finishTime]

print "Before sorting info {}".format(info)
#
#sort task information based on finishtime in decending order 
#
selection_sort(info)
print "after sorting Info {}".format(info)

# create schedule 
taskList = []

#
# Add first task to schedule
#
taskList.insert(0,info[0][taskNumber])
nextLatest = info[0][startTime]
counter = 1 
while nextLatest > 0 or counter < numberOfTasks:
    if info[counter][finishTime] <= nextLatest:
        nextLatest = info[counter][startTime]
        taskList.insert(0,info[counter][taskNumber])
    counter = counter + 1 

print ("Number of activities selected = {}").format(len(taskList))
print ("tasks to run {}").format(taskList)

    #with open('merge.txt',"a+") as resultFile:
    #    for item in sortedList:
    #        resultFile.write("%s " % item)
    #    resultFile.write("\n")
