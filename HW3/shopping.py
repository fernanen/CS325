import os
import re

def shopping(capacity,itemToView):
    result = []
    price = total = 0
    weight = items = 1
    difference = -1
    global itemList
    global keyPairCap
    
    #print("capacity: {} itemtoview: {}").format(capacity,itemToView)
    if keyPairCap[itemToView][capacity] is not None:
        #print("capacity is not NONE")
        return keyPairCap[itemToView][capacity]

    if capacity <= 0 or itemToView <= 0 or itemToView >= (len(itemList)):
        result = [0,""]
        #print("RETURNING BASE CASE")
        return result
    
    elif itemList[itemToView][weight] > capacity:
        #print("capacity is less than weight")
        result = shopping(capacity,(itemToView + difference))
        return result
    
    else:
        tmp2=[]
        #print ("itemToview: {} : price {} : itemList {}").format(itemToView,price,itemList)
        #print("#############calling tmp1#############")
        tmp1 = shopping(capacity,(itemToView + difference))
        #print("tmp1: {}").format(tmp1)
        #print("##############calling tmp2############")
        tmp2 = shopping((capacity - itemList[itemToView][weight]),(itemToView + difference))
        #print("TMP2 : {}").format(tmp2)
        tmp2[total] = tmp2[total] + itemList[itemToView][price]
        #print ("itemToview: {} : price {} : itemList {} ---tmp2:{}").format(itemToView,price,itemList,tmp2)
        #print ("tmp2 price: {} tmp2item {}").format(tmp2[price],tmp2[items])
        tmp2[items] += (str(itemToView))
        tmp2[items] += " "
        #print ("itemToview: {} : price {} : itemList {} ---tmp2:{}").format(itemToView,price,itemList,tmp2)
        #print("tmp1 price: {} , tmp2 price {}").format(tmp1[price],tmp2[price]) 
        if tmp1[total] > tmp2[total]:
            #print ("returing tmp1 {}").format(tmp1)
            return tmp1
        else:
            #print("returning tmp2 {}").format(tmp2)
            return tmp2
    

price = 0
weight = 1


fileLocation = os.getcwd() + "/shopping.txt"
print fileLocation
myfile = open(fileLocation,"r")
#read number of test cases
numcases = myfile.readline()
numcases = int(numcases)
#print("number of cases: {}").format(numcases)

resultFile = open('results.txt',"a+")

for cases in range(numcases):
    resultFile.write("Test Case %s " % (cases+1))
    resultFile.write("\n")

    # Get number of items in each case
    numItems = myfile.readline()
    numItems = int(numItems)
    #print("number of items: {}").format(numItems)

    #store item information
    itemList = [0] * (numItems+1)
    for item in range(1,(numItems+1)):
        itemList[item] = [0] * 2
        itemLine = myfile.readline()
        itemInfo = list(map(int, itemLine.split()))
        itemList[item][price] = itemInfo[price]
        itemList[item][weight] = itemInfo[weight]
        #print("item price: {} item weight: {}").format( itemList[item][price], itemList[item][weight])
    
    # get family size 
    familySize = myfile.readline()
    familySize = int(familySize)
    #print("family Size: {}").format(familySize)

    #store family member capacity
    family = [0] * familySize  

    for familyMember in range(familySize):
        family[familyMember] = myfile.readline()
        family[familyMember] = int(family[familyMember])
        #print("weight capacity: {}").format(family[familyMember])

    #let each member shop -- calling shopping method
    cap = max(family) + 1
    
    #print ("max Size : {}").format(cap)
    itemCount = len(itemList)
    
    #store cases for dynamic programming application
    keyPairCap = [None] * itemCount  
    for result in range(len(keyPairCap)):
        keyPairCap[result] = [None] * cap
    
    #print ("{} x {}").format(len(keyPairCap),len(keyPairCap[0]))
    result = [None] * familySize
    totalFam = 0
    for shopper in range(len(family)):
        result[shopper] = shopping(family[shopper],numItems)
        totalFam += result[shopper][price]
        #print("SHOPPER {}").format(family[familyMember])
        #print("{}: --{}--").format(shopper,result[shopper])
    resultFile.write("Total Price %s" % totalFam)
    resultFile.write("\nMember Items \n")
    for shopper in range(len(family)):
        resultFile.write("%s:    " % shopper)
        resultFile.write("%s\n" % result[shopper][weight])