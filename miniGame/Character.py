class Character:
    def __init__(self, name, description, gender, breed):
        self.name = name
        self.description = description
        self.gender = gender
        self.breed = breed
        self.muscle = 30
        self.intelligence = 20
        self.speed = 35
        self.charm = 64
        self.hp = 100
        self.mp = 100
        self.current_weapon = ""
        self.inventory = []

    def __str__(self):
        return f"""
        Name: {self.name}
        Description: {self.description}
        Gender: {self.gender}
        Breed: {self.breed}
        HP: {self.hp}
        MP: {self.mp}
        CurrentWeapon: {self.show_current_weapon()}
        Inventory: {self.show_inventory()}
        """

    def equip(self, index):
        self.current_weapon = self.inventory[index]

    def add_weapon(self, weapon):
        self.inventory.append(weapon)

    def show_inventory(self):
        weapons = ""
        for weapon in self.inventory:
            weapons = f"{weapons} [{weapon.name}]"

        return weapons

    def doDamage(self, character):
        if(character.hp <= 0):
            message = f"The player {character.name} has died."
            print(message)
            return
        message = ""
        if (not self.current_weapon):
            message = "Please, equip a weapon first"
            print(message)
            return

        if(self.current_weapon.element == "Fire" and character.current_weapon.element == "Grass"):
            damage = (self.current_weapon.damage * 2)
            character.hp -= damage
            message = f"The player {self.name} attacked {character.name}. Bonus of element: {damage} critical hit"
            print(message)
            return

        elif (self.current_weapon.element == "Grass" and character.current_weapon.element == "Fire"):
            damage = (self.current_weapon.damage / 2)
            character.hp -= damage
            message = f"The player {self.name} attacked {character.name}. Reduced damage: {damage}"
            print(message)
            return

        else:
            character.hp -= self.current_weapon.damage
            message = f"The player {self.name} attacked {character.name}. Normal damage: {self.current_weapon.damage}"
            print(message)
            return

    def show_current_weapon(self):
        return self.current_weapon.name
