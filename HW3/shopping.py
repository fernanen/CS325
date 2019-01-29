import os
import re

def shopping(itemList,capacity,itemToView,keyPairCap):
    result = []
    price = total = 0
    weight = items = 1
    print("capacity: {} itemtoview: {}").format(capacity,itemToView)
    if keyPairCap[itemToView][capacity] is not None:
        print("capacity is not NONE")
        return keyPairCap[itemToView][capacity]

    if capacity == 0 or itemToView == 0:
        result = [0,""]
        return result
    
    elif itemList[itemToView][weight] > capacity:
        result = shopping(itemList,capacity,(itemToView-1),keyPairCap)
    else:
        print ("itemToview: {} : price {} : itemList {}").format(itemToView,price,itemList)
        tmp1 = shopping(itemList,capacity,(itemToView-1),keyPairCap)
        tmp2 =  shopping(itemList,(capacity - itemList[itemToView][weight]),(itemToView-1),keyPairCap)
        tmp2[total] = tmp2[total] + itemList[itemToView][price]
        print ("itemToview: {} : price {} : itemList {} ---tmp2:{}").format(itemToView,price,itemList,tmp2)
        print ("tmp2 price: {} tmp2item {}").format(tmp2[price],tmp2[items])
        tmp2[items] = tmp2[items].join(str(itemToView))
        print ("itemToview: {} : price {} : itemList {} ---tmp2:{}").format(itemToView,price,itemList,tmp2)
        print("tmp1 price: {} , tmp2 price {}").format(tmp1[price],tmp2[price]) 
        if tmp1[total] < tmp2[total]:
            print ("returing tmp1")
            return tmp1
        else:
            print("returning tmp2")
            return tmp2
    

price = 0
weight = 1


fileLocation = os.getcwd() + "/shopping.txt"
print fileLocation
myfile = open(fileLocation,"r")
#read number of test cases
numcases = myfile.readline()
numcases = int(numcases)
print("number of cases: {}").format(numcases)

for cases in range(numcases):
    # Get number of items in each case
    numItems = myfile.readline()
    numItems = int(numItems)
    print("number of items: {}").format(numItems)

    #store item information
    itemList = [0] * (numItems+1)
    for item in range(1,(numItems+1)):
        itemList[item] = [0] * 2
        itemLine = myfile.readline()
        itemInfo = list(map(int, itemLine.split()))
        itemList[item][price] = itemInfo[price]
        itemList[item][weight] = itemInfo[weight]
        print("item price: {} item weight: {}").format( itemList[item][price], itemList[item][weight])
    
    # get family size 
    familySize = myfile.readline()
    familySize = int(familySize)
    print("family Size: {}").format(familySize)

    #store family member capacity
    family = [0] * familySize
    


    for familyMember in range(familySize):
        family[familyMember] = myfile.readline()
        family[familyMember] = int(family[familyMember])
        print("weight capacity: {}").format(family[familyMember])

    #let each member shop -- calling shopping method
    cap = max(family) + 1
    print ("max Size : {}").format(cap)
    itemCount = len(itemList)
    #store cases for dynamic programming application
    keyPairCap = [None] * itemCount  
    for result in range(len(keyPairCap)):
        keyPairCap[result] = [None] * cap
    print ("{} x {}").format(len(keyPairCap),len(keyPairCap[0]))
    for shopper in range(len(family)):
        finalShop = shopping(itemList,family[familyMember],numItems,keyPairCap)
        print("{}: --{}--").format(shopper,finalShop)
    #
    #with open('results.txt',"a+") as resultFile:
    #    for item in sortedList:
    #        resultFile.write("%s " % item)
    #    resultFile.write("\n")