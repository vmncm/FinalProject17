#import modules
import random, sys, time


#classes
#this class is for all types of objects that the player can interact with throughout the game
class Object():
    def __init__(self, description, take, place, number):
        """new object"""
        self.desc = description
        self.keep = take
        self.place = place
        self.usenum = number


#objects
shard = Object("A red, glass-like shard\n", True, "door", 8)
gold = Object("A small gold key\n", True, "chest", 1)
silver = Object("A small silver key\n", True, "shelf", 1)
matches = Object("Regular coated matches\n", True, "candle", 1)
meterstick = Object("Wooden meterstick\n", True, "bed", 0)
cup = Object("A ceramic cup. When you pick it up, you see a SHARD inside.\n", False, "N/A", 0)
bowl = Object("A ceramic bowl. When you pick it up, you see it is empty.\n", False, "N/A", 0)
vase = Object("A ceramic vase. When you pick it up, you see a GOLD KEY inside.\n", False, "N/A", 0)
mug = Object("A ceramic mug. When you pick it up, you see it is empty.\n", False, "N/A", 0)
book = Object("A bright red book. You open it and see that a hole has been cut into the pages. In the hole is a SHARD.\n", False, "N/A", 0)
#letters no longer necessary because I got rid of the suitcase that would require the code to save time
#letters = Object("The first letter says: Jan. 2, 1902\nNathan,\nThe research is complete! I am beginning the testing phase tomorrow. \nIf it works, it will be the greatest possible birthday present.\nThe second letter (it's more of a memo) says: Don't forget your password is your birthday.\n", False, "N/A", 0)


#lists and dictionaries
#for when the command input is completely invalid
responses = ["Sorry, I don't understand that.", "That just so happens to be outside of my skill set.", "Excuse me?", "Do something else.", "Huh?", "Dude, that's not an option.", "Can't do that, sorry.", "Yeah, I'll go right ahead and do that for you! Just kidding.", "No.", "You're not the boss of me. Ugh.", "Can you...just maybe...make some sense?", "Oops! Sorry, I don't know how to do that!", "Maybe I can do that in the next curse update."]
#for when the command is valid, but it is not the intended use/not allowed (such as taking the skeleton or taking the door)
responses2 = ["You really think you can do that?" , "Sorry, you can't do that." , "No." , "Do something else." , "You better not.", "I really don't think that'll work."]

inventory = {"shard" : 1}
#objects in each location
inv_bed = {"decoy": 1}
inv_nightstand = {"matches": 30, "silver" : 1}
inv_shelf = {"decoy": 1}
inv_bookshelf = {"meterstick": 1}
inv_desk = {"shard": 1}
inv_cabinet = {"shard": 1, "gold" : 1}
inv_chest = {"shard": 1}



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

#descriptions of each of the four walls
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
Next to the bed, there is a small NIGHTSTAND, which has two drawers. You see a few items on top of it.
On the right, you can still see the DESK and that unsettling skeleton.
"""

rightwall ="""
You are facing the right wall.
On the right, you can still see the BED. In front of the foot of the bed, there is a wooden CHEST. It looks pretty old.
On the left, there is a big window. Outside the window, you only see endless black.
Remember? This room is in a separate universe, with nothing else in it.
"""

#location is used if the player uses examine on any objects from wall view, which brings them closer to the object
location = "none"

#writing descriptions for examine function
#MCMII code no longer necessary because the box it was to be used for was taken out to save time
shelf_p1 = """You approach the shelf. There is a jar that has a label reading 'MCMII'.
Next to the jar is a silver box.
"""

shelf_p2 = """The box is locked.
"""

shelf_p3 = """The box is unlocked. You see a SHARD inside.
"""

door = """You approach the door. In the center of the door, there is a small carving in the wood.
The carving is faceted, meant to hold the gem, once the shards are all collected.
"""

cabinet = """You approach the cabinet, which is full of ceramics. On the top shelf, there is a CUP.
On the middle shelf, there is a MUG and a BOWL. On the bottom shelf, there is a VASE.
"""

chest_p1 = """You approach the chest.
"""

chest_p2 = "There is a golden lock holding it shut."

#may or may not recode in order to make the suitcase happen, but it is cutting close on time
#chest_p3 = """It is open. Inside, you see piles of clothes. Digging through the piles, you find a suitCASE.
#It has a 4-digit number lock.
#"""

chest_p3 = """It is open. Inside, you see piles of clothes. Digging through the piles, you find a SHARD.
"""

bed_p1 = """You approach the bed.
"""

bed_p2 = """Under the bed, you see a red glimmer. It is a SHARD, but you can't reach it."""

nightstand_p1 = """You approach the nightstand. On top, there is an unlit candle, a box of MATCHES, and a BOX.
"""

nightstand_p2 = """There is a SILVER KEY on the stand.
"""

desk_p1 = """You approach the desk. There are various papers documenting the scientist's experiments.
The skeleton of the scientist is sitting on the chair, as if he is reviewing his work.
On top of the desk, there are LETTERS.
"""

desk_p2 = """In the skeleton's eye, there is a red glimmer. You see that it is a SHARD.
"""


bookshelf_p1 = """You approach the bookshelf. It is packed with books, almost all of which are brown or black.
One BOOK in the center catches your eye. It is a vibrant red color.
"""

bookshelf_p2 = """Leaning on the side of the bookshelf is a METERSTICK.
"""

end = """You take all eight shards and hold them in your hand.
They shake slightly before gathering together like magnets. They push closer together until they form one, faceted gem.
You hear a 'clink' as you place the gem in the carved opening. It fits perfectly.
The door rumbles, and it slowly begins to fade into thin air.

YOU ESCAPED!
"""


#functions
#"types" out words so it seems like the narrator is actually talking to the player in real time
def type_slow(str):
    """prints words slowly"""
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.015)

#used for commands or inputs that don't exist
def invalid():
    """used to respond to invalid commands"""
    type_slow(random.choice(responses))
    print("\n")

#used when the command makes sense, but it is not allowed in game, such as taking the bookshelf or using something in the wrong place
def invalid2():
    """used to respond to invalid commands"""
    type_slow(random.choice(responses2))
    print("\n")

#wall value indicates direction (in reference to front wall): front = 1, left = 2, back = 3, right = 4
#returns the value of the wall the player should be facing; this value will later be assigned to a variable outside the turn function, but in the main code
#direction = left or right, start = the wall that the player is currently facing
def turn(direction, start):
    """turns to the next wall"""
    wall = start
    if location == "none" or direction == "back":
        if direction == "left":
            wall += 1
        elif direction == "right":
            wall -= 1
        elif direction == "back":
            wall += 0
        else:
            invalid()
        if wall == 1:
            type_slow(frontwall)
        elif wall == 2:
            type_slow(leftwall)
        elif wall == 3:
            type_slow(backwall)
        elif wall == 4:
            type_slow(rightwall)
        elif wall == 5:
            wall = 1
            type_slow(frontwall)
        else:
            wall = 4
            type_slow(rightwall)
        return wall
    else:
        type_slow("You need to go BACK to wall view to turn.")

#checks if object is available to be taken, based on the current location of the player and whether or not the object is allowed to be taken
#modifies inventory, as well
def take(obj):
    """take object, if possible"""
    y = {"bookshelf" : inv_bookshelf , "bed" : inv_bed , "shelf" : inv_shelf , "cabinet" : inv_cabinet , "nightstand" : inv_nightstand , "desk" : inv_desk, "chest" : inv_chest}
    z = {"shard" : shard , "matches" : matches , "gold" : gold , "silver" : silver , "meterstick" : meterstick}
    #global location
    if location in y:
        if z[obj].keep == True and obj in y[location] and y[location][obj] >= 1:
            if obj in inventory:
                inventory[obj] += 1
            elif obj == "gold" :
                inventory["gold key"] = 1
            elif obj == "silver" :
                inventory["silver key"] = 1
            else:
                inventory[obj] = 1
            x = y[location]
            x[obj] -= 1
            return f"{obj}2"
        #else:
        #    invalid2()
    else:
        invalid2()
#uses object only if it is in the inventory, if the current location is the right place to use it, and if the player has enough of the object to use
#modifies inventory
#after using the 8 shards, it should return "end", which will be recognized by final gameplay loop in order to end the game
#dictionary x makes it easier to call aspects under __init__
def use(obj):
    """uses object"""
    z = {"shard" : shard , "matches" : matches , "gold key" : gold , "silver key" : silver , "meterstick" : meterstick}
    if obj in inventory :
        if inventory[obj] < z[obj].usenum and z[obj].place == location :
            type_slow("You don't have enough.")
        elif inventory[obj] >= z[obj].usenum and [obj].place == location :
            if obj == "meterstick" :
                type_slow("You slide the meterstick under the bed, reaching for the SHARD.\nYou manage to pull it into arm's reach.")
            elif obj == "matches" :
                type_slow("You light the candle. As it melts, you see a SHARD inside the melted wax.\n(You can grab it without hurting yourself, don't worry.)")
            elif obj == "gold" :
                type_slow("You unlock the chest. Inside, you see a SHARD.")
            elif obj == "silver" :
                type_slow("You unlock the box. Inside, you see a SHARD.")
            else:
                type_slow("...")
            inventory[obj] -= z[obj].usenum
        else:
            invalid2()
    else:
        type_slow(f"You don't have a(n) {obj}.")
    if inventory["shard"] == 0 :
        x = "end"
        return x
    else:
        x = obj
        return x

#function used to approach location or look closely at objects
def examine(obj):
    """provides description of object or brings character closer to object"""
    z = {"shard" : shard , "matches" : matches , "gold key" : gold , "silver key" : silver , "meterstick" : meterstick, "cup" : cup , "bowl" : bowl , "vase" : vase , "mug" : mug , "book" : book}
    if obj in z:
        type_slow(z[obj].desc)
        obj2 = f"{obj}1"
        return obj2
    elif obj == "door" :
        type_slow(door)
    elif obj == "shelf" :
        type_slow(shelf)
    elif obj == "cabinet" :
        type_slow(cabinet)
    elif obj == "chest" :
        type_slow(chest)
    elif obj == "bed" :
        type_slow(bed)
    elif obj == "nightstand" :
        type_slow(nightstand)
    elif obj == "desk" :
        type_slow(desk)
    elif obj == "bookshelf" :
        type_slow(bookshelf)
    else:
        invalid2()

#prints inventory in a neat format
def inv():
    """prints inventory"""
    for k, v in inventory.items():
        print(f"{k} : {v}")

#used to help player out if s/he forgets the commands or instructions
def hlp():
    """shows instructions and commands"""
    print(instructions)
    print(commands)

#master command loop, this is what runs to take input commands from the player
#it splits the input if there is a space and uses the different words from the input to call a function and fill in its arguments
#it only returns a number for the back and turn functions; this tells the final gameplay loop to display the description of the wall that matches the number returned
def command():
    """prompts user for response and activates necessary function"""
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
            inv()
        elif res == "help":
            hlp()
        elif res == "back":
            wall_int = turn("back", wall)
            return wall_int
        else:
            invalid()


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
if new_name.lower() == "who are you":
    type_slow("\nI am...Actually, I'm not sure. I appeared when the curse did. Just pretend I'm some random narrator or something. \nNow, answer my question, you trespasser!\nWho are you?\n")
    new_name = input("> ")
type_slow(f"\nWell, {new_name}, get out. Or at least try to. I mean, it really shouldn't be that hard...\nThis whole place was designed by an amateur anyways. Compared to people with real experience, her code- \nI mean her curse skills are...subpar...\nBasically at the level of a high school junior. It gets the job done, though. Easy to escape, if you're not the cursed one.\nAbout that guy...Yeah...He didn't get out.\n")
type_slow("\nYeah... you're probably confused. That didn't explain anything...Basically, this place was some scientist's home. \nHe got way too close to discovering the secret for immortality, so someone had to step in. \nTo protect the universe, a curse was cast to put the room in a different dimension. \nThe curse is anchored by 8 gem shards, one of which is actually next to where you're standing. \nI'll add that to your inventory right now.\nThe only way back home is through the front door.\nThe key for the door is the full gem, which means you need all 8 shards.\n\nOkay, it's time for you to get out. I'll help where I can, but if you type <help>, you can get more information.")
type_slow("\nLet's get started:\n")
#end of super long exposition

#starts with player facing front of room
type_slow(frontwall)

#setup for the following while loop
wall = 1
game = command()
chest = chest_p1 + chest_p2
bed = bed_p1 + bed_p2
shelf = shelf_p1 + shelf_p2
desk = desk_p1 + desk_p2
nightstand = nightstand_p1 + nightstand_p2
bookshelf = bookshelf_p1 + bookshelf_p2

#final gameplay loop
#keeps asking user for input, allows variable, wall, to be used in and out of functions, avoids global variable issue
#uses return value to determine what wall the player is facing, what location the player is in, and when to end the game
#if the return value is not one of the key values (that requires reassigning variables or ending game), the command function will run again
while True:
    if type(game) == int:
        wall = game
        location = "none"
        game = command()
    elif game == "nightstand" or "bed" or "chest" or "door" or "bookshelf" or "shelf" or "desk" or "cabinet":
        location = game
        game = command()
    elif game == "meterstick" :
        inv_bed["shard"] = 1
        bed = bed_p1
    elif game == "gold" :
        chest = chest_p1 + chest_p3
        inv_chest["shard"] = 1
    elif game == "silver" :
        inv_shelf["shard"] = 1
        shelf = shelf_p1 + shelf_p3
    elif game == "matches" :
        inv_nightstand["shard"] = 1
    elif game == "cup1" :
        inv_cabinet["shard"] = 1
    elif game == "book1" :
        inv_bookshelf["shard"] = 1
    elif game == "cup1" :
        inventory["shard"] += 1
    elif game == "vase1" :
        inv_cabinet["gold"] = 1
    elif game == "meterstick2" :
        bookshelf = bookshelf_p1
    elif game =="silver2" :
        shelf = nightstand_p1
    elif game == "end" :
        break
    else:
        game = command()

#previous loop only breaks when the "end" is returned by the command function, so it only reaches this line at the end of the game
#"types" out the ending sequence (found at the top in "long strings and variables" section)
type_slow(end)

responses3 = ["Bye." , "Can you leave?" , "I can't go home until you leave, so can you do me a favor and close this tab?" , "There's a skeleton in this room. A real skeleton. Normal people would leave the first chance they get. Why aren't you one of them?" , "Why are you still here?" , "Game's over, get out." , "Go away." , "Just leave already!" , "Why aren't you leaving? Did I drop you off in the wrong spot or something?" , "Just close the tab, you won already." , "You know you can leave, right?" , "If you want to leave already, you should stop talking to me."]

endv = input(">>> ")

while True:
    type_slow(random.choice(responses3))
    print("\n")
    endv = input(">>> ")