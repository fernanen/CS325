import os
import re
fileLocation = os.getcwd() + "/data.txt"
print fileLocation
myfile = open(fileLocation,"r")
counter = 1 
for line in myfile:
    numset = line.split(' ',1)[0]
    dataset = line.split(' ',1)[1]
    print "numbers in the set: " + numset + "dataset:" dataset  
    for number in dataset.split()
        print number
    print "line done"
print"done"