class Item:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "%s" % self.name

class Weapon(Item):

    def __init__(self, name, level):
        super.__init__(self, name)
        self.level = level

    def __str__(self):
        return "[+%d] %s" % self.level, self.name