import os
fileLocation = os.getcwd() + "\data.txt"
print fileLocation
myfile = open(fileLocation,"r")
counter = 1 
for line in file: 
    print "Line " + counter:
    for word in line: 
        print word
    print "Line " + counter + "over"
print"done"