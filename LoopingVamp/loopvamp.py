#!/usr/bin/env python3

## create file object in "r"ead mode
with open("dracula.txt", "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    novel = configfile.readlines() #store lines into file object

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
#print(novel)

for line in novel: #for every line in object do something
    # if this 'fail pattern' appears in the line...
    print(line)

count = 0

for line in novel: #

    lowerLine = line.lower()

    if "vampire" in lowerLine:
        print(line)
        count = count + 1

print(count)

