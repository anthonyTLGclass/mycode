#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

def main():
   """ Run-time code"""
   # create a small string
   lilstring = input("Type in a string with multiple words:")
   newlist = lilstring.split(" ") # this returns a list
   print(newlist)

   # create a list of strings
   myiplist = input("Type in a list of ip Octet strings")
   # set singleip as the result of joining the list myiplist around the "."
   singleip = ".".join(myiplist)
   # display singleip
   print(singleip)

# call our main function
main()
