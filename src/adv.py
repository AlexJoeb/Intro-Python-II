from room import Room, Chest
from player import Player
from items import Item
from os import system, name

brone_coin = Item("Bronze Coin")
silver_coin = Item("Silver Coin")
gold_coin = Item("Gold Coin")

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", Chest([])),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", Chest([brone_coin])),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", Chest([])),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", Chest([silver_coin])),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", Chest([silver_coin, gold_coin])),
}


# Link rooms together

room['outside'].n = room['foyer']
room['foyer'].s = room['outside']
room['foyer'].n = room['overlook']
room['foyer'].e = room['narrow']
room['overlook'].s = room['foyer']
room['narrow'].w = room['foyer']
room['narrow'].n = room['treasure']
room['treasure'].s = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

name = input("What is your name?\n")
if name == 'exit' or name == 'q': done = 1

player = Player(name, room['outside'])

print(f'You\'ve started outside.')

# -> Gets the short nick-name of the room.
def get_room_short_name(room_name):
    if room_name == 'Outside Cave Entrance': return 'outside'
    elif room_name == 'Grand Overlook': return 'overlook'
    elif room_name == 'Foyer': return 'foyer'
    elif room_name == 'Narrow Passage': return 'narrow'
    elif room_name == 'Treasure Chamber': return 'treasure'
    else: return 'outside'

# -> Returns the full name of a direction given a singluar abv.
def full_dir(direction):
    if len(direction) > 1: return direction
    else:
        if direction == 'n': return 'north'
        elif direction == 'e': return 'east'
        elif direction == 's': return 'south'
        elif direction == 'w': return 'west'
        else: return 'no direction found.'

# -> Get the next room given a current room and direction.
def get_next_room(current, direction):
    current = current.lower()
    direction = direction.lower()
    short_dir = direction[0]
    next_room = None
    try:
        next_room = room[current].get_room(short_dir)
        return next_room
    except AttributeError:
        return None

def item_in_room_chest(item_name):
    for item in player.room.chest.items:
        print(item.name, item_name)
        if item.name.lower() == item_name.lower(): return item
        else: continue
    return None
    
def item_in_backpack(item_name):
    for item in player.backpack.items:
        if item.name.lower() == item_name.lower(): return item
        else: continue
    return None

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

done = 0

# ! Game Logic Below
while(done == 0):
    clear()
    print(f'You are now in: {player.room}')
    print('=-=')
    current_room = get_room_short_name(player.room.name)
    room_obj = room[current_room]

    if len(room_obj.chest.items) > 0: 
        print('This room has a chest with items, type "open chest" to open the chest.')

    command = input("What would you like to do next?\n")
    
    if command == 'exit' or command == 'q':
        done = 1
        continue
    elif current_room == 'overlook' and command[0] == 'n':
        print("You've stepped into the dark abyss to your death.\n\nGame Over.")
        done = 1
    elif command.split(' ')[0].lower() == 'open':
        second_arg = command.split(' ')[1].lower()
        if second_arg == 'chest':
            room_obj.chest.open(player)
        elif second_arg == 'backpack':
            player.backpack.open(player)
        continue

    next_room = get_next_room(current_room, command);
    
    if next_room == None:
        print(f'Theres nothing to the {full_dir(command)}.')
        continue
    else:
        player.room = next_room
    