#import modules
import random, sys, time

#create Character class
"""class Character(object):

    def __init__(self):
        ""new character""

    def use_skill():
"""

#lists and dictionaries
responses = ["Sorry, I don't understand that.", "Excuse me?", "Huh?", "Dude, that's not an option.", "Can't do that, sorry.", "Yeah, I'll go right ahead and do that for you! Just kidding.", "No.", "You're not the boss of me. Ugh.", "Can you...just maybe...make some sense?", "Oops! Sorry, I don't know how to do that!", "Maybe I can do that in the next update."]
#inventory = {}

#variables
commands = """check <object> : prompts character to look at object
use <object>: uses object
examine <object> : provides description of object
inventory : prints inventory
commands : displays command list
how to play : shows instructions
"""


#functions
def type(str):
    """prints words slowly"""
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

def start():
    """ """
    print("")

def invalid():
    """used to respond to invalid commands"""
    type(random.choice(responses))
    print("\n")

def che(object):
    """checks object """

def use(object):
    """uses object"""

def exa(object):
    """provides description of object"""

def inv():
    """prints inventory"""

def com():
    """displays command list"""

def htp():
    """shows instructions"""
    print(commands)

title = """~~~~~~~~~~~~~~~~~~~~
|   (game title)   |
|     > PLAY <     |
|  > HOW TO PLAY < |
~~~~~~~~~~~~~~~~~~~~
"""

print(title)




choice1 = input("> ")

#Not working
if choice1.lower() == "play":
    start()
else:
    while choice1.lower != "play":
        if choice1.lower() == "how to play":
            htp()
            choice1 = input("> ")
        else:
            invalid()
            choice1 = input("> ")
    start()




#Room 1



#Room 2



#Room 3



#Room 4



#Room 5



#Room 6


