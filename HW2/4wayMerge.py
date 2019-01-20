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



fileLocation = os.getcwd() + "/data.txt"
print fileLocation
myfile = open(fileLocation,"r")
counter = 1 
for line in myfile:
    line_array = list(map(int, line.split()))
    dataset = line_array[1:]
    print "Number of values: {} , dataset: {}" .format(len(dataset),dataset)
    print "Sorting"
    sortedList = four_way_merge_sort(dataset)
    print "Sorted"
    with open('4merge.txt',"a+") as resultFile:
        for item in sortedList:
            resultFile.write("%s " % item)
        resultFile.write("\n")
