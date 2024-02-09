#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   print() - display data to std out"""

# below is a function containing our code
def main():

    # Have user input name
    user_input_name = input("Please type in your name:")

    # Have user input day of the week
    user_input_week = input("Please type in the day of the week:")

    # display the input back to the user.
    print("Hello, {0}! Happy {1}! ".format(user_input_name, user_input_week))
    
# this calls main
main()

