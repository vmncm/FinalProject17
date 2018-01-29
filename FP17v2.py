

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

inventory = {"shard" : 1}
#objects in each location
inv_bed = {"decoy": 1}
inv_nightstand = {"matches": 30, "silver" : 1}
inv_shelf = {"decoy": 1}
inv_bookshelf = {"meterstick": 1}
inv_desk = {"shard": 1}
inv_cabinet = {"shard": 1, "gold" : 1}
inv_chest = {"shard": 1}

location = "desk"

def take(obj):
    """take object, if possible"""
    y = {"bookshelf" : inv_bookshelf , "bed" : inv_bed , "shelf" : inv_shelf , "cabinet" : inv_cabinet , "nightstand" : inv_nightstand , "desk" : inv_desk, "chest" : inv_chest}
    z = {"shard" : shard}
    global location
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
    else:
        print("invalid")

print(inventory) #should be {"shard" : 1}

take("shard")

print(inventory)
#should be {"shard":2}