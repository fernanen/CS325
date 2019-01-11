import os
import re

def insertionSort(dataArray, numToAdd):
    dataArray.append(numToAdd)
    counter = (len(dataArray)-1)
    if counter <= 0:
        return dataArray
    else:
        while dataArray[counter] < dataArray[counter-1] and counter > 0:
            tempValStore = dataArray[counter]
            dataArray[counter] = dataArray[counter-1]
            dataArray[counter-1] = tempValStore
            counter = counter-1
        return dataArray

fileLocation = os.getcwd() + "/data.txt"
print fileLocation
myfile = open(fileLocation,"r")
counter = 1 
for line in myfile:
    numset = line.split(' ',1)[0]
    dataset = line.split(' ',1)[1]
    sortedList = []
    for number in dataset.split():
        insertionSort(sortedList,number)
    with open('insert.txt', 'w') as f:
    for item in sortedList:
        f.write("%s\n" % item)
    f.write("\n")