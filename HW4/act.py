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
#myfile = open(fileLocation,"r")
#
# variable declarations
#
taskNumber = 0
startTime= 1
finishTime= 2
case = 1
with open(fileLocation) as myfile:
    numberOfTasks = myfile.readline()
    while numberOfTasks != '':
        #get number of tasks
        numberOfTasks = int(numberOfTasks)
        #
        # initialize information array
        #
        info = [None] * (numberOfTasks)
        #print ("Number of tasks: {}").format(numberOfTasks)
        for row in range(len(info)):
            info[row] = [-1] * 3 # 3 being number of pieces of information given. 

        #
        #getInfo
        #
        for task in range(len(info)):
            line = myfile.readline()
            line_array = list(map(int, line.split()))
            info[task][taskNumber] = line_array[taskNumber]
            info[task][startTime] = line_array[startTime]
            info[task][finishTime] = line_array[finishTime]

        #print "Before sorting info {}".format(info)
        #
        #sort task information based on finishtime in decending order 
        #
        selection_sort(info)
        #print "after sorting Info {}".format(info)

        # create schedule 
        taskList = []

        #
        # Add first task to schedule
        #
        taskList.insert(0,info[0][taskNumber])
        nextLatest = info[0][startTime]
        counter = 1 
        while nextLatest > 0 and counter < numberOfTasks:
            #print ("couter: {}").format(counter)
            if info[counter][finishTime] <= nextLatest:
                nextLatest = info[counter][startTime]
                taskList.insert(0,info[counter][taskNumber])
            counter = counter + 1 

        print ("case {}").format(case)
        print ("Number of activities selected = {}").format(len(taskList))
        print ("Activities: {}").format(taskList)
        case = case + 1
        numberOfTasks = myfile.readline()
