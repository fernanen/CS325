import os
import re
import random
import time
def merge_sort(dataset):
    array_size = len(dataset)
    if array_size == 1 or array_size == 0:
        return dataset
    array_split = array_size / 2
    num1 = merge_sort(dataset[:array_split])
    num2 = merge_sort(dataset[array_split:])
    #print "left: {} right: {}".format(num1,num2)
    return merge(num1, num2)

def merge(array1, array2):
    new_array = []
    array1_length = len(array1)
    array2_length = len(array2)
    #print "array1 length: {} content: {} array2 length: {} content {}".format(array1_length,array1,array2_length,array2)
    while array1_length != 0 and array2_length != 0:
        if array1[0] < array2[0]:
            new_array.append(array1.pop(0))
            array1_length = array1_length - 1 
        else:
            new_array.append(array2.pop(0))
            array2_length = array2_length - 1
    if array1_length == 0:
        new_array += array2
    else:
        new_array += array1
    return new_array
size = 10
time = 0.0 
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