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


price = 0
weight = 1


fileLocation = os.getcwd() + "/shopping.txt"
print fileLocation
myfile = open(fileLocation,"r")
#read number of test cases
numcases = myfile.readline()
numcases = int(numcases)
caseList = []
for cases in range(numcases):
    numItems = myfile.readline()
    numItems = int(numItems)
    itemList = [0] * numItems

    for item in range(numItems):
        itemList[item] = [0] * 2
        itemLine = myfile.readline()
        itemInfo = list(map(int, itemLine.split()))
        itemList[item][price] = itemInfo[price]
        itemList[item][weight] = itemInfo[weight]
    familySize = myfile.readline()
    family = [0] * familySize
    for familyMember in range(familySize):
        family[familyMember] = myfile.readline()
    #
    ##  
    #
    #with open('results.txt',"a+") as resultFile:
    #    for item in sortedList:
    #        resultFile.write("%s " % item)
    #    resultFile.write("\n")