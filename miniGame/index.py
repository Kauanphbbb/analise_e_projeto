from Weapon import Weapon
from Character import Character

sword = Weapon("Fire", "Hell Sword", 100, 3, 12, 21)
wand = Weapon("Grass", "Green Wand", 100, 2, 8, 16)

kauan = Character("Kauan", "A swordmaster", "M", "Human")
rannyson = Character("Rannyson", "A magician", "M", "Elf")

kauan.add_weapon(sword)
rannyson.add_weapon(wand)
rannyson.add_weapon(sword)

kauan.equip(0)
rannyson.equip(0)
kauan.doDamage(rannyson)
rannyson.doDamage(kauan)
rannyson.equip(1)
rannyson.doDamage(kauan)
rannyson.equip(0)
kauan.doDamage(rannyson)
kauan.doDamage(rannyson)
kauan.doDamage(rannyson)
kauan.doDamage(rannyson)
kauan.doDamage(rannyson)
kauan.doDamage(rannyson)

print(rannyson)
