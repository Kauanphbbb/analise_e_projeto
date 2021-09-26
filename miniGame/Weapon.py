from Item import Item


class Weapon (Item):
    def __init__(self, element, name, price, rarity, damage, speed):
        Item.__init__(self, price, rarity, damage, speed)
        self.element = element
        self.name = name
