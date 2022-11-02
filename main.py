from time import sleep
import sys

class Item:
    def __init__(self, name):
        self.name = name

class Flashlight(Item):
    used = False
    def display(self):
        return "Flashlight - the only light source you currently have"

class Bucket(Item):
    used = False
    def display(self):
        return "Bucket - the plain bucket to carrying water"

class Key(Item):
    used = False
    def display(self):
        return "Key - the little key, maybe some kind of a trunk."

class Dynamite(Item):
    used = False
    def display(self):
        return "Dynamite - it requires some fire..."

class Lighter(Item):
    used = False
    def display(self):
        return "Lighter - some fire"

flashlight = Flashlight("flashlight")
bucket = Bucket("bucket")
key = Key("key")
dynamite = Dynamite("dynamite")
lighter = Lighter("lighter")


class Place:
    def __init__(self, name):
        self.name = name
    
    def entering(place_to_enter):
        place_to_enter.entered = True
        for place in all_places:
            if place.name != place_to_enter.name:
                place.entered = False
        if place_to_enter != first and place_to_enter != main_room:
            print(place_to_enter.display())
            info()

class First(Place):
    def describe(self):
        if flashlight.used == False:
            print("You don't see anything. Try to change it")
        if flashlight.used == True:
            print("You can see the door in front of you. If you want to go to it, type \"go door\"")


class Stone(Place):
    entered = False
    destroyed = False
    def display(self):
        return "A big stone, you can see little sun gaps behind it. "
    def describe(self):
        return print("There should be exit behind it, but it is too heave to move it. Maybe you should destroy it, but how...")

class Trunk(Place):
    entered = False
    open = False
    def display(self):
        return "The closed trunk, it has a hole for key"
    def describe(self):
        if self.open == True:
            return print("Ooo, there is dynamite inside. Take it, it can be useful.")
        else:
            return print("An old trunk, it is locked. Maybe there is any key for that...")

class Puddle(Place):
    entered = False
    empty = False
    def display(self):
        return "In the center of the room, there is a huge puddle, there is something on the bottom but you can't see it"
    def describe(self):
        if self.empty == True:
            return print("You get all the water out of the puddle and you see an old, little key at the bottom. Try to get it")
        else:
            return print("Here is a lot of water, but you can see something on the button.")

first = First("first")
stone = Stone("stone")
trunk = Trunk("trunk")
puddle = Puddle("puddle")

class MainRoom(Place):
    items_to_take = [bucket, lighter]
    places_in_main_room = [stone, trunk, puddle]
    def describe(self):
        if len(self.items_to_take) == 0:
            print("No items to take here.")
        else:
            print("Items to take:")
            for item in self.items_to_take:
                print(f"- {item.name.capitalize()}")
        print("Places to go to:")
        for place in self.places_in_main_room:
            print(f"- {place.name.capitalize()} - {place.display()}")

main_room = MainRoom("main room")

def main_commands(select_action):
    sleep_and_print_empty_line(1)
    if "use" in select_action:
        using(select_action)
    elif "take" in select_action:
        taking(select_action)
    elif "go" in select_action:
        going(select_action)
    elif select_action == "inventory":
        display_inventory()
    elif select_action == "help":
        help()
    elif select_action == "describe":
        describe()
    elif select_action == "back":
        going_back()
    else:
        print("Wrong command")

def info():
    print("Try to do something with that or get back to the main room (type \"back\").")
    

def sleep_and_print_empty_line(seconds):
    sleep(seconds)
    print()

def correct_item(correct_item, using_item):
    if using_item.used == True:
        print("You already used it.")
    elif correct_item is using_item:
        using_item.used = True
    else:
        print("This item doesn't match here. Try something else.")

def append_to_inventory(item):
    inventory.append(item)
    return print(f"You have picked {item.name}.")

def using(select_action):
    if all(item.name not in select_action for item in inventory):
        print("You don't have that item in your inventory.")
    else:
        for item in inventory:
            if item.name in select_action:
                using_item = item       

        if first.entered == True:
            correct_item(flashlight, using_item)
        elif main_room.entered == True:
            print("No item needed here.")
        elif puddle.entered == True:
            correct_item(bucket, using_item)
        elif trunk.entered == True:
            correct_item(key, using_item)
        elif stone.entered == True:
            if dynamite.name in select_action:
                correct_item(dynamite, using_item)
            elif lighter.name in select_action:
                correct_item(lighter, using_item)
            else:
                print("This item doesn't match here. Try something else.")

def taking(select_action):
    if first.entered == True or stone.entered == True:
        print("There aren't any items to take.")
    elif main_room.entered == True and bucket.name in select_action:
        append_to_inventory(bucket)
        main_room.items_to_take.remove(bucket)
    elif main_room.entered == True and lighter.name in select_action:
        append_to_inventory(lighter)
        main_room.items_to_take.remove(lighter)
    elif puddle.entered == True and puddle.empty == True and key.name in select_action:
        append_to_inventory(key)
    elif trunk.entered == True and trunk.open == True and key.used == True and dynamite.name in select_action:
        append_to_inventory(dynamite)
    else:
        print("Invalid name of the item. Please try again.")
            
def going(select_action):
    if "door" in select_action:
        Place.entering(main_room)
    for place in all_places:
        if place.name in select_action:
            Place.entering(place)
            
            

def display_inventory():
    for item in inventory:
        print(item.display())

def help():
    print("\"use {item name} \" - use an item which is in your inventory")
    print("\"take {item name} \" - take the found item")
    print("\"go {place} \" - go to place if it is available")
    print("\"inventory\" - display all items whose you already have")
    print("\"help\" - display all commands")
    print("\"describe\" - it describes a room where you are")

def describe():
    for place in all_places:
        if place.entered == True:
            place.describe()
            break
def going_back():
    if puddle.entered == True or stone.entered == True or trunk.entered == True:
        print("You are going back to main room")
        Place.entering(main_room)
        for item in inventory:
            item.used = False
    else:
        print("You cannot go back from here.")


inventory = [flashlight, ]
all_places = [first, main_room, stone, trunk, puddle]


def chapter2():
    print("You enter a strange room, try to look around. There can be some interesting items. To look around type \"describe\".")
    while True:
        select_action = input("Select an action: ").lower()
        main_commands(select_action)
        while puddle.entered == True:
            if key in inventory:
                print("Nothing more to do here.")
                Place.entering(main_room)
                continue
            select_action = input("Select an action: ").lower()
            main_commands(select_action)
            if bucket.used == True:
                puddle.empty = True
                print("Nice! You get all the water out of the puddle and you see an old, little key at the bottom. Try to get it!")
                select_action = input("Select an action: ").lower()
                main_commands(select_action)
                Place.entering(main_room)
                continue
        while trunk.entered == True:
            if dynamite in inventory:
                print("Nothing more to do here.")
                Place.entering(main_room)
                continue
            select_action = input("Select an action: ").lower()
            main_commands(select_action)
            if key.used == True:
                trunk.open = True
                print("Ooo, there is dynamite inside. Take it, it can be useful.")
                select_action = input("Select an action: ").lower()
                main_commands(select_action)
                Place.entering(main_room)
                continue
        while stone.entered == True:
            select_action = input("Select an action: ").lower()
            main_commands(select_action)
            if lighter.used == True and dynamite.used == True:
                print("Congratulations! The game is over, you are free.")
                sys.exit(0)
            elif lighter.used == True:
                print("Hmm, nice but something is missing...")
            elif dynamite.used == True:
                print("Okey, but you need some fire.")


def main():
    user_name = input('Enter your name: ').capitalize()
    print(f"Hello, {user_name}! Now, you are in the cave. You don't know how and why you are here, but it is not important. Here is so dark and spooky, you can hear some sounds and they aren't nice. You are getting scared and only you can do it is try to escape from here. Let's start.")
    sleep_and_print_empty_line(4)
    print("Okey, first have a look at help. There are all commands whose you can use when you play. You can check help all time typing \"help\" in terminal.")
    sleep_and_print_empty_line(4)
    help()
    sleep_and_print_empty_line(4)
    print("Hmmm..., you already know something but you don't see anything. Look at your inventory and check if you have something that can help you.")
    sleep_and_print_empty_line(4)

    while True:
        Place.entering(first)
        select_action = input("Select an action: ").lower()
        main_commands(select_action)
        if flashlight.used == True:
            print("That's right, there is some light now. You are looking around and see the door. It's only interesting thing here, so you must choose, go through them or stay here forever. Type \"go door\" to continue.")
            break
    while True:
        select_action = input("Select an action: ").lower()
        main_commands(select_action)
        if flashlight.used == True and main_room.entered == True:
            print("You are going to the door, it's open.")
            chapter2() 
            

main()
