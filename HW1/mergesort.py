import os
import re

def merge_sort(dataset):
    array_size = len(dataset)
    if array_size == 1 or array_size == 0:
        return dataset
    array_split = array_size / 2
    num1 = merge_sort(dataset[:array_split])
    num2 = merge_sort(dataset[array_split:])
    return merge(num1, num2)

def merge(array1, array2):
    new_array = []
    array1_length = len(array1)
    array2_length = len(array2)
    while array1_length != 0 and array2_length != 0:
        if array1[0] < array2[0]:
            new_array.append(array1.pop(0))
        else:
            new_array.append(array2.pop(0))
    if array1_length == 0:
        new_array += array2
    else:
        new_array += array1
    return new_array
        
fileLocation = os.getcwd() + "/data.txt"
print fileLocation
myfile = open(fileLocation,"r")
counter = 1 
for line in myfile:
    numset = line.split(' ',1)[0]
    dataset = line.split(' ',1)[1]
    for number in dataset.split():
        sortedList = merge_sort(sortedList)
    with open('insert.txt',"a+") as resultFile:
        for item in sortedList:
            resultFile.write("%s " % item)
        resultFile.write("\n")