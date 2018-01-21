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
"""shard = Object("A red, glass-like shard", True, door, 8)
key1 =
key2 =
letter = Object("It says: ''", True)
matches = Object("Regular coated matches", True, desk, 1)
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
examine <object> : provides description of object / goes closer to object (from wall view)
back : returns you to wall view
turn <left> or turn <right>: turns your character either left or right
inventory : prints inventory
help : shows instructions and commands
"""

title = """~~~~~~~~~~~~~~~~~~~~
| The Eight Shards |
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

frontwall = """
You are facing the front wall.
There is a sturdy wooden DOOR in the center of the wall. On the door, there is a small opening for the gem.
To the left of the door, there is a SHELF with a few things on it.
To the right of the door, there is a CABINET with three shelves inside.
On those shelves, there are various containers.
"""

leftwall ="""
You are facing the left wall.
In the left corner, there is a large DESK, scattered with paper. By the desk, there is a really creepy skeleton sitting on a chair.
(Yeah, I was serious when I told you the guy who got cursed didn't get out.)
To the right of the desk, there is a tall BOOKSHELF that takes up the rest of the space on this wall. It is full of books.
"""

backwall ="""
You are facing the back wall.
There is a BED in the left corner, with the foot of the bed closer to you.
Next to the bed, there is a small NIGHTSTAND, which has two drawers. On top of the nightstand, there is a candle, matches, and a weird box.
On the right, you can still see the desk and that unsettling skeleton.
"""

rightwall ="""
You are facing the right wall.
On the right, you can still see the BED. In front of the foot of the bed, there is a wooden CHEST. It looks pretty old.
On the left, there is a big window. Outside the window, you only see endless black.
Remember? This room is in a separate universe, with nothing else in it.
"""

#location is used if the player uses examine on any objects from wall view, which brings them closer to the object
location = "none"

shelf = """You approach the shelf.
"""

door = """You approach the door. In the center of the door, there is a small carving in the wood.
The carving is faceted, meant to hold the gem, once the shards are all collected.
"""

cabinet = """You approach the cabinet.
"""

chest = """You approach the chest.
"""

bed = """You approach the bed.
"""

nightstand = """You approach the nightstand.
"""

desk = """You approach the desk.
"""

bookshelf = """You approach the bookshelf.
"""

end = """You take all eight shards and hold them in your hand.
They shake slightly before gathering together like magnets. They push closer together until they form one, faceted gem.
You hear a 'clink' as you place the gem in the carved opening. It fits perfectly.
The door rumbles, and it slowly begins to fade into thin air.

YOU ESCAPED!
"""


#functions
def type_slow(str):
    """prints words slowly"""
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.025)

def invalid():
    """used to respond to invalid commands"""
    type_slow(random.choice(responses))
    print("\n")

def invalid2():
    """used to respond to invalid commands"""
    type_slow(random.choice(responses2))
    print("\n")

def front():
    """provides description of the front wall"""
    type_slow(frontwall)

def back():
    """provides description of the back wall"""
    type_slow(backwall)

def left():
    """provides description of the left wall"""
    type_slow(leftwall)

def right():
    """provides description of the right wall"""
    type_slow(rightwall)

#wall value indicates direction (in reference to front wall): front = 1, left = 2, back = 3, right = 4
def turn(direction, start):
    """turns to the next wall"""
    wall = start
    if direction == "left":
        wall += 1
    elif direction == "right":
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
        wall = 1
        front()
    else:
        wall = 4
        right()
    return wall


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
    type_slow(obj.desc)

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
    #wall = 1
    #location = "none"
    res = (input("\n> ")).lower()
    if ' ' in res:
        resp = res.split(" ")
        respo = resp[0]
        if respo == "turn" :
            wall_int = turn(resp[1], wall)
            return wall_int
        elif respo == "take" :
            take(resp[1])
        elif respo == "use" :
            use(resp[1])
        elif respo == "examine" :
            examine(resp[1])
        else:
            invalid()
    else:
        if res == "inventory":
            inventory()
        elif res == "help":
            hlp()
        elif res == "back":
            wall_int = turn("none", wall)
            return wall_int
        else:
            invalid()

    #command()


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
type_slow("...\n.....\nThis is weird. Really weird. This place was supposed to be sealed off from your world.\n...Is something wrong with the curse?\nHow did you get here?\n")
type_slow("\nUmm...WHO ARE YOU?\n")
new_name = input("> ")
if new_name.lower == "who are you":
    type_slow("\nI am...Actually, I'm not sure. I appeared when the curse did. Just pretend I'm some random narrator or something. \nNow, answer my question, you trespasser!\nWho are you?\n")
    new_name = input("> ")
type_slow(f"\nWell, {new_name}, get out. Or at least try to. I mean, it really shouldn't be that hard...\nThis whole place was designed by an amateur anyways. Compared to people with real experience, her code- \nI mean her curse skills are...subpar...\nBasically at the level of a high school junior. It gets the job done, though. Easy to escape, if you're not the cursed one.\nAbout that guy...Yeah...He didn't get out.\n")
type_slow("\nYeah... you're probably confused. That didn't explain anything...Basically, this place was some scientist's home. \nHe got way too close to discovering the secret for immortality, so someone had to step in. \nTo protect the universe, a curse was cast to put the room in a different dimension. \nThe curse is anchored by 8 gem shards, one of which is actually next to where you're standing. \nI'll add that to your inventory right now.\nThe only way back home is through the front door.\nThe key for the door is the full gem, which means you need all 8 shards.\n\nOkay, it's time for you to get out. I'll help where I can, but if you type <help>, you can get more information.")
type_slow("\nLet's get started:\n")
#end of super long exposition

#start with player facing front of room
front()

wall = 1
game = command()

while True:
    if type(game) == int:
        wall = game
        game = command()
    else:
        game = command()