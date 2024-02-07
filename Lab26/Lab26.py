#!/usr/bin/env python3

#Dictionary utilized in lab although placed in a non-intuitive oder in the lab 
marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }



#input from user asking for list of characters
char_name = input(" Which character do you want to know about? (Starlord, Mystique, Hulk)")

#input from user asking for statisitc about character
char_stat = input(" What statistic do you want to know about? (real name, powers, archenemy)")

#Pull value from dictionary and print to command line
value = marvelchars[char_name][char_stat]
print(f"{char_name}'s {char_stat} is : {value}")

