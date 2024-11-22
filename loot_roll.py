"""
Lootroll 1.0

A simple game which generates randomised "loot", as if from an action roleplaying game such as Diablo.
Current notes:
1) Only generates one-handed swords
2) The item names do not currently influence the attributes of the item
3) Item level currently has no effect on the attributes of the item
4) Items currently do not have special effects or abilities
"""
import random

#Words which are placed at random at the start of item names, e.g BARBED Blade of the Tiger (currently 10 prefixes)
PREFIXES = [
"Barbed",
"Vorpal",
"Keen",
"Serrated",
"Sharp",
"Dull",
"Tarnished",
"Glowing",
"Rusted",
"Broken"
]

#Words which are placed at random at the start of one-handed sword item names, e.g Barbed BLADE of the Tiger (currently 10 swords)
SWORD_NAMES_1H = [
"Blade",
"Edge",
"Scimitar",
"Cutlass",
"Katana",
"Sabre",
"Rapier",
"Gladius",
"Falchion",
"Dao"
]

#Words which are placed at random at the end of item names, e.g Barbed Blade of the TIGER (currently 10 suffixes)
SUFFIXES = [
"Tiger",
"Wolf",
"Eagle",
"Mongoose",
"Lion",
"Dragon",
"Hound",
"Mouse",
"Cockroach",
"Viper"
]

def main():

#Pulls a random prefix from PREFIXES
    random_prefix = random.choice(PREFIXES)
#Pulls a random one-handed sword name from SWORD_NAMES_1H
    random_sword1h = random.choice(SWORD_NAMES_1H)
#Pulls a random suffix from SUFFIXES
    random_suffix = random.choice(SUFFIXES)

#Generates an item level (currently does nothing)
    item_lvl = random.randint(80, 99)
#Generates an attack speed (weapons only)
    attack_speed = round(random.uniform (1.50, 1.99), 2)
#Generates a minumum value for a damage range (weapons only)
    minimum_damage = random.randint(150, 200)
#Generates a maximum value for a damage range (weapons only)
    maximum_damage = random.randint(250, 300)
#Calculates the damage per second of a weapon by finding the average of its damage range and diving it by its attack speed (weapons only)
    total_dps = round(((minimum_damage+maximum_damage)/2)/attack_speed, 2)
#Randomly rolls an item name, formatted as an f-string
    item_name = (f'{random_prefix} {random_sword1h} of the {random_suffix}')

#Prints the generated weapon in the console
    print("Congratulations! You receive:")
    print(end='\n')
    print(item_name)
    print("Item level:", item_lvl)
    print(end='\n')
    print("Damage:", minimum_damage, "-", maximum_damage)
    print("Attack speed:", attack_speed)
    print("DPS:", total_dps)
    print(end='\n')

#Prints a rating for the weapon based on DPS value
    if total_dps <= 100:
        print("Weapons this terrible really shouldn't exist...")
    if 100 <= total_dps <= 110:
        print("This weapon is not very good...")
    if 110 <= total_dps <= 130:
        print("A fairly average weapon.")
    if 130 <= total_dps <= 140:
        print("Quite a strong weapon.")
    if 140 <= total_dps <= 150:
        print("Exceptional quality.")
    if total_dps >= 150:
        print("Wow! An incredible weapon.")

if __name__ == "__main__":
    main()
