"""
Lootroll 1.0

A simple game which generates randomised "loot", as if from an action roleplaying game such as Diablo.
Current notes:
1) Only generates one-handed swords
2) The item names do not currently influence the attributes of the item
3) Items currently do not have special effects or abilities
"""
import random

#Words which are placed at random at the start of item names, e.g BARBED Blade of the Tiger (currently 10 prefixes)
SWORD_PREFIXES_1H = [
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
SWORD_SUFFIXES_1H = [
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

#Words which are placed at the start of dragon monster name, e.g ELDER Volcano Dragon (currently 5 ages)
DRAGON_AGE = [
"Hatchling",
"Juvenile",
"Mature",
"Elder",
"Ancient",
]

#Words which are placed after the age in the dragon monster namer, e.g Elder VOLCANO Dragon (currently 8 prefixes)
DRAGON_PREFIXES = [
"Volcano",
"Thunder",
"Frozen",
"Tempest",
"Mountain",
"Arcane",
"Shadow",
"Eldritch",
]


def main():

    while input("Challenge a monster? (y/n)") == "y":

    #Pulls a random prefix from PREFIXES
        random_prefix = random.choice(SWORD_PREFIXES_1H)
    #Pulls a random one-handed sword name from SWORD_NAMES_1H
        random_sword1h = random.choice(SWORD_NAMES_1H)
    #Pulls a random suffix from SUFFIXES
        random_suffix = random.choice(SWORD_SUFFIXES_1H)

    #Pulls a random dragon age from DRAGON_AGE
        random_dragon_age = random.choice(DRAGON_AGE)
    #Pulls a random dragon prefix from DRAGON_PREFIXES
        random_dragon_prefix = random.choice(DRAGON_PREFIXES)

    #Calculates the the level of the monster
        monster_level = random.randint(80, 110)

    #Generates an item level (currently does nothing)
        item_level = random.randint(80, 110)
    #Generates an attack speed (weapons only)
        attack_speed = round(random.uniform (1.50, 1.99), 2)
    #Generates a minumum value for a damage range (weapons only)
        minimum_damage = random.randint(150, 200)
    #Generates a maximum value for a damage range (weapons only)
        maximum_damage = random.randint(250, 300)
    #Calculates the damage per second of a weapon by finding the average of its damage range and diving it by its attack speed (weapons only)
        raw_dps = ((minimum_damage+maximum_damage)/2)/attack_speed
    #Calculates DPS adjusted by a percentage informed by item_level
        total_dps = round(((raw_dps/100)*item_level),2)

    #Randomly rolls an item name, formatted as an f-string
        item_name = (f'{random_prefix} {random_sword1h} of the {random_suffix}')
    #Randomly rolls a dragon name, formatted as an f-string
        dragon_name = (f'{random_dragon_age} {random_dragon_prefix} Dragon')
    #Calculates a random amount of gold dropped by the enemy, scaled by monster_level
        gold_dropped = (random.randint(50, 500)*item_level)

    #Prints the name and level of the monster in the console
        print(end='\n')
        print("You have defeated the Level", monster_level, dragon_name)
        print(end='\n')

    #Prints the generated weapon in the console
        print("Congratulations! You receive:")
        print(end='\n')
        print(item_name)
        print("Item level:", item_level)
        print("Damage:", minimum_damage, "-", maximum_damage)
        print("Attack speed:", attack_speed)
        print("DPS:", total_dps)
        print(end='\n')

    #Prints a rating for the weapon based on DPS value
        if total_dps <= 100:
            print("F tier: Weapons this terrible really have no use.")
        if 100 <= total_dps <= 110:
            print("D tier: This weapon is not very good...")
        if 110 <= total_dps <= 130:
            print("C tier: A fairly average weapon.")
        if 130 <= total_dps <= 140:
            print("B tier: Quite a strong, reliable weapon.")
        if 140 <= total_dps <= 150:
            print("A tier: Exceptional quality and craftmanship.")
        if 150 <= total_dps <= 156:
            print("S tier: Wow! An incredible weapon, and a rare find.")
        if total_dps >= 160:
            print("S+ tier: Legendary weapon! It doesn't get much better than this.")

        # Prints a random amount of gold earned in the console
        print(end='\n')
        print("...you also receive", format(gold_dropped, ","), "gold pieces.")
        print(end='\n')

if __name__ == "__main__":
    main()
