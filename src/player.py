# Write a class to hold player information, e.g. what room they are in
# currently.

class Backpack:
    def __init__(self, items):
        self.items = items

    def __str__(self):
        if len(self.items) <= 0: return f"Your backpack is empty."
        else:
            contents = ', '.join([item.name for item in self.items])
            return f'You open your backpack and find: {contents}'

    def contains(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower(): return item
            else: continue
        return None

    def add_item(self, item):
        self.items.append(item);

    def remove_item(self, item):
        self.items.remove(item);

    def open(self, player):
        if len(self.items) <= 0:
            print('Your backpack is empty.');
            while(1):
                command = input('Type "close" to close your backpack.\n')
                if command == 'close':
                    break
                else: continue
            return None
        else:
            printed = 0

            while(1):

                if(len(self.items)):
                    print(self)
                else:
                    print('You backpack is now empty.')

                command = None

                if printed == 0:
                    command = input('Type "close" to close your backpack or "drop [item name]" to drop an item.\n>> ')
                else: command = input('>> ')

                if command.split(' ')[0] == 'close':
                    break
                elif command.split(' ')[0] == 'drop':
                    # get an item
                    item_name = " ".join(command.split(' ')[1:])
                    item_to_get = self.contains(item_name)
                    if item_to_get == None:
                        # ! Item does not exist.
                        print("That item must have fallen out, because it's not in your backpack.")
                        continue
                    else:
                        self.remove_item(item_to_get)
                        print(f"You dropped the {item_to_get.name}")
                        continue
            return None
class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.backpack = Backpack([])

    def __str__(self):
        return f'{self.name}, in room: {self.room}'

    def pickup_item(self, item):
        self.room.remove_item(item)
        self.backpack.add_item(item)

    def drop_item(self, item):
        self.backpack.remove_item(item)
        self.room.add_item(item)