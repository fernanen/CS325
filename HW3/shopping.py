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
print("number of cases: {}").format(numcases)
caseList = []
for cases in range(numcases):
    numItems = myfile.readline()
    numItems = int(numItems)
    print("number of items: {}").format(numItems)
    itemList = [0] * numItems

    for item in range(numItems):
        itemList[item] = [0] * 2
        itemLine = myfile.readline()
        itemInfo = list(map(int, itemLine.split()))
        itemList[item][price] = itemInfo[price]
        itemList[item][weight] = itemInfo[weight]
        print("item price: {} item weight: {}").format( itemList[item][price], itemList[item][weight])
    familySize = myfile.readline()
    familySize = int(familySize)
    print("family Size: {}").format(familySize)
    family = [0] * familySize
    for familyMember in range(familySize):
        family[familyMember] = myfile.readline()
        family[familyMember] = int(family[familyMember])
        print("number of items: {}").format(family[familyMember])
    #
    ##  
    #
    #with open('results.txt',"a+") as resultFile:
    #    for item in sortedList:
    #        resultFile.write("%s " % item)
    #    resultFile.write("\n")