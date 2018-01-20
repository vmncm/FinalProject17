#import modules
import random, sys, time

#lists and dictionaries
responses = ["Sorry, I don't understand that.", "That just so happens to be outside of my skill set.", "Excuse me?", "Huh?", "Dude, that's not an option.", "Can't do that, sorry.", "Yeah, I'll go right ahead and do that for you! Just kidding.", "No.", "You're not the boss of me. Ugh.", "Can you...just maybe...make some sense?", "Oops! Sorry, I don't know how to do that!", "Maybe I can do that in the next curse update."]
#inventory = { : , : , : , : , : , : }

#variables
commands = """take <object> : takes object and puts it in the inventory, if possible
check <object> : prompts character to look at object
use <object>: uses object
examine <object> : provides description of object
turn <left> or turn <right>: turns your character either left or right
inventory : prints inventory
help : shows instructions and commands
"""

title = """~~~~~~~~~~~~~~~~~~~~
|      Escape      |
|     > PLAY <     |
|  > HOW TO PLAY < |
~~~~~~~~~~~~~~~~~~~~
"""

instructions = """You can interact with objects using various preset commands. You can interact with anything that is in all caps.
To use commands with objects, type the command followed by the name of the object as it is shown in caps.
You do not need to type in all caps. Don't use punctuation either.
Shown below are the various commands you can use throughout the game.
"""

#classes
"""class Character(object):

    def __init__(self, name):
        ""new character""
        self.name = name

    def use_skill():
        ""use special skill""
"""

class Object():
    def __init__(self, description):
        """new object"""
        self.desc = str(description)

#objects


#functions
def type(str):
    """prints words slowly"""
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

def invalid():
    """used to respond to invalid commands"""
    type(random.choice(responses))
    print("\n")

def take():
    """take object, if possible"""

def turn(direction):
    """turns to the next quadrant"""

def check(object):
    """checks object"""

def use(object):
    """uses object"""

def examine(object):
    """provides description of object"""
    type(object.desc)
    command()

def inventory():
    """prints inventory"""
    for k, v in inventory:
        print(f"{k} : {v}")

def hlp():
    """shows instructions and commands"""
    print(instructions)
    print(commands)

def command():
    """prompts user for response"""
    res = (input("\n> ")).lower()
    if ' ' in res:
        resp = res.split(" ")
        respo = resp[0]
        if respo == "turn" :
            turn(resp[1])
        elif respo == "take" :
            take(resp[1])
        elif respo == "check" :
            check(resp[1])
        elif respo == "use" :
            use(resp[1])
        elif respo == "examine" :
            examine(resp[1])
        else:
            invalid()
            command()
    elif ' ' not in res:
        if res == "inventory":
            inventory()
        elif res == "help":
            hlp()
    else:
        invalid()
        command()



#title screen
print(title)

#setup for title page loop
choice1 = input("> ")

#title page loop
while True:
    if choice1.lower() == "how to play":
        hlp()
        choice1 = input("> ")
    elif choice1.lower() == "play":
        break
    else:
        invalid()
        choice1 = input("> ")

#game start/situation
type("...\n.....\nThis is weird. Really weird. This place was supposed to be sealed off from your world.\nNo one's been here in centuries! ...Is something wrong with the curse?\nHow did you get here?\n")
type("\nUmm...WHO ARE YOU?\n")
new_name = input("> ")
#player = Character(new_name)
if new_name.lower == "who are you":
    type("\nI am... You don't need to know. Now, answer my question, you trespasser!\nWho are you?\n")
    new_name = input("> ")
type(f"\nWell, {new_name}, get out. Or at least try to. I mean, it really shouldn't be that hard...\nThis whole place was designed by an amateur anyways. Compared to real experienced deities, her curse skills are...\n...subpar...\nBasically at the level of a high school junior. It gets the job done, though. Easy to escape, if you're not the cursed one.\nThen again, the last guy didn't think so. I think he hit his head pretty hard when he got here, so his brain was a bit frazzled. \nYeah...He didn't get out.\nOn a completely unrelated note, don't look in the back left corner.\n")

