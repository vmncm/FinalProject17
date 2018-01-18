#import modules
import random, sys, time

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

title = """~~~~~~~~~~~~~~~~~~~~
|      Escape      |
|     > PLAY <     |
|  > HOW TO PLAY < |
~~~~~~~~~~~~~~~~~~~~
"""

instructions = """You can interact with objects using various preset commands.
Objects that you can interact with are in all caps. To use commands with obects,
type the command followed by the name of the object as it is shown in caps.

Shown below are the various commands you can use throughout the game.

"""

#functions
def type(str):
    """prints words slowly"""
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

def start():
    """starts situation"""
    type("...\n.....\nHow did you get here? No one's been here in centuries!")
    new_name = input("Who are you?\n> ")
    type()

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
    for k, v in inventory:
        print(f"")

def com():
    """displays command list"""
    print(commands)

def htp():
    """shows instructions"""
    print(instructions)
    print(commands)

#create Character class
"""class Character(object):

    def __init__(self, name):
        ""new character""
        self.name = name

    def use_skill():
        ""use special skill""
"""



print(title)


choice1 = input("> ")

while True:
    if choice1.lower() == "how to play":
        htp()
        choice1 = input("> ")
    elif choice1.lower() == "play":
        start()
    else:
        invalid()
        choice1 = input("> ")


#player = Character(new_name)


#Room 1



#Room 2



#Room 3



#Room 4



#Room 5



#Room 6


