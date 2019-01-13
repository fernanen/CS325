import os
import re
import random
import time
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

    size = 10
    sortedList
    start = time.time() 
    for i in size
        insertionSort(sortedList,random.randint(1,10000))
    end = time.time()
    result = end - start
    with open('insert.txt',"a+") as resultFile:
        for item in sortedList:
            resultFile.write("%s " % size)
            resultFile.write("%s " % result)
        resultFile.write("\n")