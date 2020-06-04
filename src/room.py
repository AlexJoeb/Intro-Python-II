# Implement a class to hold room information. This should have name and
# description attributes.

from items import Item

class Chest:
    def __init__(self, items):
        self.items = items

    def __str__(self):
        contents = ', '.join([item.name for item in self.items])
        return f"You open the chest and find: {contents}"

    def contains(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower(): return item
            else: continue
        return None

    def open(self, player):
        if len(self.items) <= 0:
            print('This chest is empty.');
            while(1):
                command = input('Type "close" to close the chest.')
                if command == 'close':
                    break
                else: continue
            return None
        else:
            printed = 0
            while(1):
                # What does the player find, remove it from the chest and add it to the player backpack.

                # Print contents of the chest.

                if(len(self.items)):
                    print(self)
                else:
                    print('The chest is now empty.')

                command = None
                if printed == 0:
                    command = input('Type "close" to close the chest or "get [item name]" to pick something up.\n>> ')
                else: command = input('>> ')

                if command.split(' ')[0] == 'close':
                    break
                elif command.split(' ')[0] == 'get':
                    # get an item
                    item_name = " ".join(command.split(' ')[1:])
                    item_to_get = self.contains(item_name)
                    if item_to_get == None:
                        # ! Item does not exist.
                        print("You've rummaged through the chest but can not find that item.")
                        continue
                    else:
                        player.pickup_item(item_to_get)
                        print(f"You picked up the {item_to_get.name}")
                        continue
            return None

        if len(self.items) <= 0: 
            print(f"The chest is empty.")
            return None
        else:
            item_names = []

            for item in self.items:
                item_names.append(item.name)

            print(f'You open the chest and find:\n{", ".join(item_names).strip(", ")}')

class Room:
    def __init__(self, name, desc, chest):
        self.name = name
        self.desc = desc
        self.chest = chest

    def __str__(self):
        return f'{self.name}\n({self.desc})'

    def get_room(self, direction):
        if direction == 'n': return self.n
        elif direction == 'e': return self.e
        elif direction == 's': return self.s
        elif direction == 'w': return self.w
        else: return None

    def add_item(self, item):
        self.chest.items.append(Item(item.name))

    def remove_item(self, item):
        self.chest.items.remove(item)