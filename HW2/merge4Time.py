import os
import re

def four_way_merge_sort(dataset):
    array_size = len(dataset)
    print "dataset length: {}".format(array_size)
    if array_size == 1:
        return dataset
    if array_size == 2:
        if dataset[0] <= dataset[1]:
            return dataset
        else:
            temp=dataset[0]
            dataset[0]=dataset[1]
            dataset[1]=temp
            return temp
    if array_size == 3:
        if dataset[0] > dataset[1]:
            temp=dataset[0]
            dataset[0]=dataset[1]
            dataset[1]=temp
        if dataset[1] > dataset[2]:
            temp=dataset[1]
            dataset[1]=dataset[2]
            dataset[2]=temp
        if dataset[0] > dataset[1]:
            temp=dataset[1]
            dataset[0]=dataset[1]
            dataset[1]=temp
        return dataset          
    if array_size >= 4:
        array_split = array_size / 4
        num1 = four_way_merge_sort(dataset[:array_split])
        num2 = four_way_merge_sort(dataset[array_split:(array_split*2)])
        num3 = four_way_merge_sort(dataset[(array_split*2):(array_split*3)])
        num4 = four_way_merge_sort(dataset[(array_split*3):])
        print "num1: {} num2: {} num3: {} num4: {}".format(num1,num2,num3,num4)
        return merge(num1, num2, num3, num4)
    return 1
 
def as_list(x):
    if type(x) is list: 
        return x
    else: 
        return[x]
    
def merge(arr1, arr2, arr3, arr4):
    sorted_array = []
    array1=as_list(arr1)
    array2=as_list(arr2)
    array3=as_list(arr3)
    array4=as_list(arr4)
    while not len(array1) == len(array2) == len(array3) == len(array4) == 0:
        lowestVal=1000000000;
        lowestPos=-1;
        if array1:
            if array1[0] < lowestVal:
               lowestVal = array1[0]
               lowestPos = array1
        if array2:
            if array2[0] < lowestVal:
                lowestVal = array2[0]
                lowestPos = array2
        if array3:
            if array3[0] < lowestVal:
               lowestVal = array3[0]
               lowestPos = array3
        if array4:
            if array4[0] < lowestVal:
               lowestVal = array4[0]
               lowestPos = array4
        sorted_array.append(lowestPos.pop(0))
    return sorted_array



for x in range(1,21): 
    dataset = []       
    for i in range(1,size):
        dataset.append(random.randint(1,10000))
    #print "Number of values: {} , dataset: {}" .format(len(dataset),dataset)
    start = time.time()
    sortedList = merge_sort(dataset)
    end = time.time()
    result = end-start
    resultFile = open('./mergeTime.txt',"a+")
    resultFile.write("%s " % size)
    resultFile.write("%s " % result)
    resultFile.write("\n")
    resultFile.close()
    size = size + 1000