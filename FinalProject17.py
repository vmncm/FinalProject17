#import modules
import random, sys, time

#classes
class Object():
    def __init__(self, description, take, place, number):
        """new object"""
        self.desc = description
        self.keep = take
        self.place = place
        self.usenum = number


#objects
"""shard = Object("a red glass-like shard", True, door)
shard2 = Object("a red glass-like shard", True)
shard3 = Object("a red glass-like shard", True)
shard4 = Object("a red glass-like shard", True)
shard5 = Object("a red glass-like shard", True)
shard6 = Object("a red glass-like shard", True)
shard7 = Object("a red glass-like shard", True)
shard8 = Object("a red glass-like shard", True)
key1
letter = Object("It says: ''", True)
"""


#lists and dictionaries
#for when the command input is completely invalid
responses = ["Sorry, I don't understand that.", "That just so happens to be outside of my skill set.", "Excuse me?", "Do something else.", "Huh?", "Dude, that's not an option.", "Can't do that, sorry.", "Yeah, I'll go right ahead and do that for you! Just kidding.", "No.", "You're not the boss of me. Ugh.", "Can you...just maybe...make some sense?", "Oops! Sorry, I don't know how to do that!", "Maybe I can do that in the next curse update."]
inventory = {"shard" : 1}
#for when the command is valid, but it is not the intended use/not allowed (such as taking the skeleton or taking the door)
responses2 = ["You really think you can do that?" , "Sorry, you can't do that." , "No." , "Do something else." , "You better not.", "I really don't think that'll work."]


#long strings & other variables
commands = """take <object> : takes object and puts it in the inventory, if possible
use <object>: uses object
examine <object> : provides description of object
turn <left> or turn <right>: turns your character either left or right
inventory : prints inventory
help : shows instructions and commands
"""

title = """~~~~~~~~~~~~~~~~~~~~
|   Eight Shards   |
|     > PLAY <     |
|  > HOW TO PLAY < |
~~~~~~~~~~~~~~~~~~~~
"""

instructions = """You can interact with objects using various preset commands. You can interact with anything that is in all caps.
To use commands with objects, type the command followed by the name of the object as it is shown in caps.
You do not need to type in all caps. Don't use punctuation either.
Shown below are the various commands you can use throughout the game.
"""
#wall value indicates direction (in reference to front wall): front = 1, left = 2, back = 3, right = 4
wall = 1

frontwall = """There is a sturdy wooden DOOR in the center of the wall. On the door, there is a small opening for the gem.
To the left of the door, there is a SHELF with a few things on it. To the right of the door, there is a CABINET with three shelves inside.
On those shelves, there are various containers.
"""

leftwall ="""In the left corner, there is a large DESK, scattered with paper. By the desk, there is a really creepy skeleton sitting on a chair.
(Yeah, I was serious when I told you the guy who got cursed didn't get out.)
To the right of the desk, there is a tall BOOKSHELF that takes up the rest of the space on this wall. It is full of books.
"""

backwall ="""There is a BED in the left corner, with the foot of the bed closer to you.
Next to the bed, there is a small NIGHTSTAND, which has two drawers. On top of the nightstand, there is a candle, matches, and a weird box.
On the right, you can still see the desk and that unsettling skeleton.
"""

rightwall ="""On the right, you can still see the BED. In front of the foot of the bed, there is a wooden CHEST. It looks pretty old.
On the left, there is a big window. Outside the window, you only see endless black.
Remember? This room is in a separate universe, with nothing else in it.
"""

#location is used if the player uses examine on any objects from wall view, which brings them closer to the object
location = "none"

#functions
def type(str):
    """prints words slowly"""
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.025)

def invalid():
    """used to respond to invalid commands"""
    type(random.choice(responses))
    print("\n")

def invalid2():
    """used to respond to invalid commands"""
    type(random.choice(responses2))
    print("\n")

def front():
    """provides description of the front wall"""
    type(frontwall)

def back():
    """provides description of the back wall"""
    type(backwall)

def left():
    """provides description of the left wall"""
    type(leftwall)

def right():
    """provides description of the right wall"""
    type(rightwall)

def turn(direction):
    """turns to the next wall"""
    if direction == "left":
        global wall
        wall += 1
    elif direction == "right":
        global wall
        wall -= 1
    else:
        invalid()
    if wall == 1:
        front()
    elif wall == 2:
        left()
    elif wall == 3:
        back()
    elif wall == 4:
        right()
    elif wall == 5:
        global wall
        wall= 1
        front()
    else:
        global wall
        wall = 4
        right()

def take(obj):
    """take object, if possible"""
    if obj.keep == True:
        if obj in inventory:
            inventory[obj] += 1
        else:
            inventory[obj] = 1
    else:
        invalid2()

def use(obj):
    """uses object"""
    if obj.place == location:
        inventory[obj] -= obj.usenum
    else:
        invalid2()

def examine(obj):
    """provides description of object"""
    type(obj.desc)

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
        elif respo == "use" :
            use(resp[1])
        elif respo == "examine" :
            examine(resp[1])
        else:
            invalid()
    elif ' ' not in res:
        if res == "inventory":
            inventory()
        elif res == "help":
            hlp()
        elif res == "back":
            turn("none")
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
type("...\n.....\nThis is weird. Really weird. This place was supposed to be sealed off from your world.\n...Is something wrong with the curse?\nHow did you get here?\n")
type("\nUmm...WHO ARE YOU?\n")
new_name = input("> ")
#player = Character(new_name)
if new_name.lower == "who are you":
    type("\nI am... You don't need to know. Now, answer my question, you trespasser!\nWho are you?\n")
    new_name = input("> ")
type(f"\nWell, {new_name}, get out. Or at least try to. I mean, it really shouldn't be that hard...\nThis whole place was designed by an amateur anyways. Compared to people with real experience, her code- \nI mean her curse skills are...subpar...\nBasically at the level of a high school junior. It gets the job done, though. Easy to escape, if you're not the cursed one.\nAbout that guy...Yeah...He didn't get out.\n")
type("\nYeah... you're probably confused. That didn't explain anything...Basically, this place was some scientist's home. \nHe got way too close to discovering the secret for immortality, so someone had to step in. \nTo protect the universe, a curse was cast to put the room in a different dimension. \nThe curse is anchored by 8 gem shards, one of which is actually next to where you're standing. I'll add that to your inventory right now.\nThe only way back home is through the front door.\nThe key for the door is the full gem, which means you need all 8 shards.\nOkay, it's time for you to get out. I'll help where I can, but if you type <help>, you can get more information.")
type("\nLet's get started:\n")
#end of super long exposition

#start with player facing front of room
front()
command()
