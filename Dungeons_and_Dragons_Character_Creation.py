"""
Created on Tuesday April 30 2019

@author: terreratman
"""

# =============================================================================
# I made this because my group has their noses in the books 24/7 and I want things to go a bit quicker. I'm hoping some random characters will allow them to focus on familiarizing themselves with the game rules by pushing them through different situations
# The code contains every race allowed in the Adventurer's League as well as some extras, every published class and background (I listed some extra classes, but have not finished their code until I test their balance)
# None of my code is very elegant as I have just learned python in the past two weeks.
# Please feel free to leave critisisms and suggestions, it will help me learn. :)
#
# Known Gaps in the character creator:
#
# Does not account for the level 4, 8, 12, and 16 stat increase or feat choice if making a higher level character
# Does not include languages yet because I'm still investigating a method to add a random item to a list only if the addition is not already in the list, and if it was already in the list, pick a new item and try to add
# Does not have a seperate category for currency because I'm not sure how to account for adding from multiple sources
# Does not account for Personality Traits, Ideals or Bonds because I don't want to write a random.choice for things that bulky, trying to find another way
# Not all Skin/Hair/Eye colours may be correct, I just put some in quickly
# It does not print class traits
# =============================================================================

import random
import collections

def normal(min, max): # Not exactly sure how this one is working, but it gives a more realistic result for age, height and weight
    r = round(random.triangular(low = min, high = max))# Round gives us a whole number for a character's age
    return r

def hitpoints(max_dice):
    n = 1
    hitpoints = 0
    if level == 1:
        hitpoints = max_dice + con_mod
        if hitpoints <= max_dice:  # This makes it so that the minimum HP is your HP die but you can start stronger if it "rolls well"
            hitpoints = max_dice
        return(hitpoints)
    else:
        hitpoints = max_dice + level * con_mod
        while n < level:
            hitpoints = hitpoints + random.randint(1, max_dice)
            n = n + 1
    if hitpoints <= max_dice + (level - 1):  # This makes it so the minimum HP increase is 1, I don't like to play with weakening characters
        hitpoints = max_dice + (level - 1)
    return(hitpoints)

def stat_increase(stat, num_increase):
    if stat <= 20 - num_increase:
        stat = stat + num_increase
    else:
        stat = 20
    return(stat)
        
def stat_decrease(stat, num_decrease):
    if stat >= 1 + num_decrease:
        stat = stat - num_decrease
    else:
        stat = 1
    return(stat)
        
def stat_mod(stat):
    return (stat - 10) // 2
    
def remove_duplicates(input):
    return list(set(input))

level = 3  # This is where you change Character Level

# =============================================================================
# # In stead of a d20 for stats you could 4d6 drop the lowest
# def StatRoll():
#     List = []
#     n=0
#     while n < 4:
#         List.append(random.randint(1,6))
#         n = n + 1
#     MIN = (min(List))
#     List.remove(MIN)
#     Stat = sum(List)
#     return Stat
# 
# STR = StatRoll()
# =============================================================================

stats = ["STR", "DEX", "CON", "INT", "WIS", "CHA"] # This list will be used for the variant human later on

attr_str = random.randint (1,20)
attr_dex = random.randint (1,20)
attr_con = random.randint (1,20)
attr_int = random.randint (1,20)
attr_wis = random.randint (1,20)
attr_cha = random.randint (1,20)

armour_profs = []
weapon_profs = []
tool_profs = []
saving_throw_profs = []
skill_profs = []
resistances = []
immunities = []
vulnerabilities = []
traits = []
equipment = []

subrace = "N/A"
subclass = "N/A"
fighting_style = "N/A"
hp = 0
age = 0
size_mod = 0
height = 0
weight = 0
eyes = "N/A"
skin = "N/A"
hair = "N/A"
speed = 0

skills = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival"]
artisan_tools = ["Alchemist's Supplies", "Brewer's Supplies", "Calligrapher's Supplies", "Carpenter's Tools", "Cartographer's Tools", "Cobbler's Tools", "Cook's Utensils", "Glassblower's Tools", "Jeweler's Tools", "Leatherworker's Tools", "Mason's Tools", "Painter's Tools", "Potter's Tools", "Smith's Tools", "Tinker's Tools", "Weaver's Tools", "Woodcarver's Tools"]
gaming_sets = ["Dice Set", "Dragonchess Set", "Playing Card Set", "Three-Dragon Ante Set"]
musical_instruments = ["Bagpipes", "Drum", "Dulcimer", "Flute", "Lute", "Lyre", "Horn", "Pan Flute", "Shawm", "Viol"]
martial_weapons = ["Battleaxe", "Flail", "Glaive", "Greataxe", "Greatsword", "Halberd", "Lance", "Longsword", "Maul", "Morningstar", "Pike", "Rapier", "Scimitar", "Shortsword", "Trident", "War Pick", "Warhammer", "Whip", "Blowgun", "Hand Crossbow", "Heavy Crossbow", "Longbow", "Net"]
martial_melee = ["Battleaxe", "Flail", "Glaive", "Greataxe", "Greatsword", "Halberd", "Lance", "Longsword", "Maul", "Morningstar", "Pike", "Rapier", "Scimitar", "Shortsword", "Trident", "War Pick", "Warhammer", "Whip"]
simple_weapons = ["Club", "Dagger", "Greatclub", "Handaxe", "Javelin", "Light Hammer", "Mace", "Quarterstaff", "Sickle", "Spear", "Light Crossbow", "Dart", "Shortbow", "Sling"]
simple_melee = ["Club", "Dagger", "Greatclub", "Handaxe", "Javelin", "Light Hammer", "Mace", "Quarterstaff", "Sickle", "Spear"]

# Abomination Currently Removed
race = ["Aasimar", "Bugbear", "Dragonborn", "Dryad", "Dwarf", "Elf", "Firbolg", "Genasi", "Gith", "Gnome", "Goblin", "Goliath", "Hobgoblin", "Half-Elf", "Halfling", "Half-Orc", "Human", "Juiblexian", "Kender", "Kenku", "Kobold", "Lizardfolk", "Mousefolk", "Orc", "Succubus", "Tabaxi", "Tiefling", "Tortle", "Triton", "Yuan-Ti Pureblood"]
race = random.choice(race)

if race == "Aasimar":
    subrace = ["Fallen", "Protector", "Scourge"]
    subrace = random.choice(subrace)
    attr_cha = stat_increase(attr_cha, 2)
    if subrace == "Fallen":
        attr_str = stat_increase(attr_str, 1)
    if subrace == "Protector":
        attr_wis = stat_increase(attr_wis, 1)
    if subrace == "Scourge":
        attr_con = stat_increase(attr_con, 1)
    age = normal(20,140)
    size_mod = normal(2,20)
    height = 4 * 12 + 10 + size_mod
    weight = 110 + size_mod * normal(2,8)
    eyes = ["Pupil-less Pale White", "Pupil-less Gold", "Pupil-less Gray", "Pupil-less Topaz"]
    eyes = random.choice(eyes)
    skin = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black", "Emerald", "Gold", "Silver"]
    skin = random.choice(skin)
    hair = ["Red", "Blond", "Brown", "Black", "Silver"]
    hair = random.choice(hair)
    speed = 30
    traits.extend(["Darkvision (60ft)", "Healing Hands", "Light Bearer"])
    resistances.extend(["Necrotic", "Radiant"])
    if level >= 3:
        if subrace == "Fallen":
            traits.extend(["Necrotic Shroud"])
        if subrace == "Protector":
            traits.extend(["Radiant Soul"])
        if subrace == "Scourge":
            traits.extend(["Radiant Consumption"])

# =============================================================================
# if Race == "Abomination": 
# =============================================================================
    
if race == "Bugbear":
    attr_str = stat_increase(attr_str, 2)
    attr_dex = stat_increase(attr_dex, 1)
    age = normal(16,60)
    size_mod = normal(2,16)
    height = 6 * 12 + 4 + size_mod
    weight = 230 + size_mod * normal(2,12)
    eyes = ["Yellow", "Orange", "Red", "Brown", "Greenish White"]
    eyes = random.choice(eyes)
    skin = ["Yellow", "Muddy Yellow", "Reddish Orange", "Reddish Brown"]
    skin = random.choice(skin)
    hair = ["Brown", "Red"]
    hair = random.choice(hair)
    speed = 30
    traits.extend(["Darkvision (60ft)", "Long-Limbed", "Powerful Build", "Surprise Attack"])
    skill_profs.extend(["Stealth"])
    
if race == "Dragonborn":
    subrace = ["Red", "Green", "Blue", "White", "Black", "Gold", "Silver", "Brass", "Copper", "Bronze"]
    subrace = random.choice(subrace)
    attr_str = stat_increase(attr_str, 2)
    attr_cha = stat_increase(attr_cha, 1)
    age = normal(15,60)
    size_mod = normal(2,16)
    height = 5 * 12 + 6 + size_mod
    weight = 175 + size_mod * normal(2,12)
    eyes = ["Red", "Gold"]
    eyes = random.choice(eyes)
    skin = subrace + " Scales"
    speed = 30
    if subrace == "Black":
        resistances.extend(["Acid"])
        traits.extend(["Acid Breath"])
    if subrace == "Blue":
        resistances.extend(["Lightning"])
        traits.extend(["Lightning Breath"])
    if subrace == "Brass":
        resistances.extend(["Fire"])
        traits.extend(["Fire Breath"])
    if subrace == "Bronze":
        resistances.extend(["Lightning"])
        traits.extend(["Lightning Breath"])
    if subrace == "Copper":
        resistances.extend(["Acid"])
        traits.extend(["Acid Breath"])
    if subrace == "Gold":
        resistances.extend(["Fire"])
        traits.extend(["Fire Breath"])
    if subrace == "Green":
        resistances.extend(["Poison"])
        traits.extend(["Poison Breath"])
    if subrace == "Red":
        resistances.extend(["Fire"])
        traits.extend(["Fire Breath"])
    if subrace == "Silver":
        resistances.extend(["Cold"])
        traits.extend(["Cold Breath"])
    if subrace == "White":
        resistances.extend(["Cold"])
        traits.extend(["Cold Breath"])

if race == "Dryad": # Extra Race I found https://www.dandwiki.com/wiki/Dryad_(5e_Race)
    subrace = ["Watcher"]  # Leaving this as a list in case I can find a balanced version of the Guardian subclass
    subrace = random.choice(subrace)
    attr_dex = stat_increase(attr_dex, 1)
    attr_wis = stat_increase(attr_wis, 2)
    age = "N/A"
    size_mod = normal(2,6)
    height = 5 * 12 + 5 + size_mod
    weight = 40 + size_mod * normal(2,6)
    eyes = "Changes with the Seasons"
    skin = ["Orange", "Green", "Yellowish Green"]
    skin = random.choice(skin)
    hair = "Leaves that Change with the Seasons"
    speed = 30
    traits.extend(["Barkskin", "Forest Blend", "Photosynthesis", "Tree Stride", "Nature Whisperer"])
    vulnerabilities.extend(["Fire"])
    
if race == "Dwarf":
    subrace = ["Duergar", "Hill", "Mountain"]
    subrace = random.choice(subrace)
    attr_con = stat_increase(attr_con, 2)
    if subrace == "Hill":
        attr_wis = stat_increase(attr_wis, 1)
    if subrace == "Mountain":
        attr_str = stat_increase(attr_str, 2)
    if subrace == "Duergar":
        attr_str = stat_increase(attr_str, 1)
    age = normal(20,320)
    size_mod = normal(2,8)
    if subrace == "Hill":
        height = 3 * 12 + 8 + size_mod
        weight = 115 + size_mod * normal(2,12)
    if subrace == "Mountain":
        height = 4 * 12 + size_mod
        weight = 130 + size_mod * normal(2,12)
    if subrace == "Duergar":
        height = 3 * 12 + 8 + size_mod
        weight = 115 + size_mod * normal(2,12)
    eyes = ["Brown", "Hazel", "Green"]
    eyes = random.choice(eyes)
    skin = ["White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black"]
    skin = random.choice(skin)
    hair = ["Bald", "Brown", "Black", "Blond", "Red"]
    hair = random.choice(hair)
    speed = 25
    weapon_profs.extend(["Battleaxe", "Handaxe", "Throwing Hammer", "Warhammer"])
    traits.extend(["Dwarven Resilience"])
    if subrace == "Hill":
        hp = hp + level
        traits.extend(["Darkvision (60ft)"])
    if subrace == "Mountain":
        armour_profs.extend(["Light Armour", "Medium Armour"])
        traits.extend(["Darkvision (60ft)"])
    if subrace == "Duergar":
        traits.extend(["Darkvision (120ft)", "Duergar Resilience", "Duergar Magic", "Sunlight Sensitivity"])
    
if race == "Elf":
    subrace = ["Eladrin", "Drow", "High", "Sea", "Shadar-Kai", "Wood"]
    subrace = random.choice(subrace)
    attr_dex = stat_increase(attr_dex, 2)
    if subrace == "Eladrin" or subrace == "Drow":
        attr_cha = stat_increase(attr_cha, 1)
    if subrace == "High":
        attr_int = stat_increase(attr_int, 1)
    if subrace == "Sea" or subrace == "Shadar-Kai":
        attr_con = stat_increase(attr_con, 1)
    if subrace == "Wood":
        attr_wis = stat_increase(attr_wis, 1)
    age = normal(20,700)
    if subrace == "Eladrin":
        size_mod = normal(2,24)
    if subrace == "Drow":
        size_mod = normal(2,12)
    if subrace == "High" or subrace == "Wood":
        size_mod = normal(2,20)
    if subrace == "Sea" or subrace == "Shadar-Kai":
        size_mod = normal(2,16)
    if subrace == "Eladrin":
        height = 4 * 12 + 6 + size_mod
        weight = 90 + size_mod * random.randint(1,4)
    if subrace == "Drow":
        height = 4 * 12 + 5 + size_mod
        weight = 75 + size_mod * random.randint(1,6)
    if subrace == "High":
        height = 4 * 12 + 6 + size_mod
        weight = 90 + size_mod * random.randint(1,4)
    if subrace == "Sea":
        height = 4 * 12 + 6 + size_mod
        weight = 90 + size_mod * random.randint(1,4)
    if subrace == "Shadar-Kai":
        height = 4 * 12 + 8 + size_mod
        weight = 90 + size_mod * random.randint(1,4)
    if subrace == "Wood":
        height = 4 * 12 + 6 + size_mod
        weight = 100 + size_mod * random.randint(1,4)
    eyes = ["Blue", "Violet", "Green"]
    eyes = random.choice(eyes)
    skin = ["Lightly Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown"]
    skin = random.choice(skin)
    hair = ["Dark Brown", "Autumn Orange", "Mossy Green", "Deep Gold"]
    hair = random.choice(hair)
    speed = 30
    traits.extend(["Keen Senses", "Fey Ancestry", "Trance"])
    if subrace == "Eladrin":
        subrace = ["Eladrin of Autumn", "Eladrin of Winter", "Eladrin of Spring", "Eladrin of Summer"]
        subrace = random.choice(subrace)
        traits.extend(["Darkvision (60ft)", "Fey Step"])
    if subrace == "Drow":
        weapon_profs.extend(["Rapiers", "Shortswords", "Hand Crossbows"])
        traits.extend(["Darkvision (120ft)", "Sunlight Sensitivity", "Drow Magic"])
    if subrace == "High":
        weapon_profs.extend(["Longswords", "Shortswords", "Shortbows", "Longbows"])
        traits.extend(["Wizard Cantrip"])
    if subrace == "Sea":
        weapon_profs.extend(["Spears", "Tridents", "Light Crossbows", "Nets"])
        traits.extend(["Swim (30ft)", "Child of the Sea", "Friend of the Sea"])
    if subrace == "Shadar-Kai":
        resistances.extend(["Necrotic"])
        traits.extend(["Blessing of the Raven Queen"])
    if subrace == "Wood":
        speed = 35
        weapon_profs.extend(["Longswords", "Shortswords", "Shortbows", "Longbows"])
        traits.extend(["Mask of the Wild"])

if race == "Firbolg":
    attr_wis = stat_increase(attr_wis, 2)
    attr_str = stat_increase(attr_str, 1)
    age = normal(30,450)
    size_mod = normal(2,24)
    height = 6 * 12 + 4 + size_mod
    weight = 210 + size_mod * normal(1,4)
    eyes = ["Blue", "Violet", "Green"]
    eyes = random.choice(eyes) 
    skin = ["Light Pink", "Grayish Blue"]
    skin = random.choice(skin)
    hair = ["Red", "Blonde", "Dark Brown"]
    hair = random.choice(hair)
    speed = 30
    traits.extend(["Firbolg Magic", "Hidden Step", "Powerful Build", "Speech of Beast and Leaf"])

if race == "Genasi":
    subrace = ["Air", "Earth", "Fire", "Water"]
    subrace = random.choice(subrace)
    attr_con = stat_increase(attr_con, 2)
    if subrace == "Air":
        attr_dex = stat_increase(attr_dex, 1)
    if subrace == "Earth":
        attr_str = stat_increase(attr_str, 1)
    if subrace == "Fire":
        attr_int = stat_increase(attr_int, 1)
    if subrace == "Water":
        attr_wis = stat_increase(attr_wis, 1)
    age = normal(20,100)
    size_mod = normal(2,20)
    height = 4 * 12 + 8 + size_mod
    weight = 110 + size_mod * normal(2,8)
    if subrace == "Air":
        eyes = "Pale Blue"
        skin = "Blueish Silver"
        hair = "Blue and Gray Crystalline Hair"
    if subrace == "Earth":
        eyes = "Golden"
        skin = "Brownish Gray"
        hair = "Black"
    if subrace == "Fire":
        eyes = "Reddish Orange"
        skin = "Bronze"
        hair = "Orange"
    if subrace == "Water":
        eyes = "Deep Blue"
        skin = "Green"
        hair = "Dark Green"
    speed = 30
    if subrace == "Air":
        traits.extend(["Unending Breath", "Mingle with the Wind"])
    if subrace == "Earth":
        traits.extend(["Earth Walk", "Merge with Stone"])
    if subrace == "Fire":
        resistances.extend(["Fire"])
        traits.extend(["Darkvision(60ft)", "Reach to the Blaze"])
    if subrace == "Water":
        resistances.extend(["Acid"])
        traits.extend(["Amphibious", "Swim (30ft)", "Call to the Wave"])

if race == "Gith":
    subrace = ["Githyanki", "Githzerai"]
    subrace = random.choice(subrace)
    attr_int = stat_increase(attr_int, 1)
    if subrace == "Githyanki":
        attr_str = stat_increase(attr_str, 2)
    if subrace == "Githzerai":
        attr_wis = stat_increase(attr_wis, 2)
    age = normal(20,80)
    size_mod = normal(2,24)
    if subrace == "Githyanki":
        height = 5 * 12 + size_mod
        weight = 100 + size_mod * normal(2,8)
    if subrace == "Githzerai":
        height = 4 * 12 + 11 + size_mod
        weight = 90 + size_mod * normal(2,8)
    eyes = "Yellow"
    skin = ["Fair", "Pale Yellow with Green Tones", "Pale Yellow with Brown Tones"]
    skin = random.choice(skin)
    hair = ["Russet", "Black", "Gray"]
    hair = random.choice(hair)
    speed = 30
    if subrace == "Githyanki":
        armour_profs.extend(["Light Armour", "Medium Armour"])
        weapon_profs.extend(["Shortswords", "Longswords", "Greatswords"])
        traits.extend(["Decadent Mastery", "Githyanki Psionics"])
    if subrace == "Githzerai":
        traits.extend(["Mental Discipline", "Githzerai Psionics"])
    
if race == "Gnome":
    subrace = ["Deep", "Forest", "Rock"]
    subrace = random.choice(subrace)
    attr_int = stat_increase(attr_int, 2)
    if subrace == "Deep" or subrace == "Forest":
        attr_dex = stat_increase(attr_dex, 1)
    if subrace == "Rock":
        attr_con = stat_increase(attr_con, 1)
    age = normal(20,400)
    size_mod = normal(2,8)
    height = 2 * 12 + 11 + size_mod
    weight = 35 + size_mod
    eyes = ["Glittering Opaque Black", "Glittering Opaque Blue"]
    eyes = random.choice(eyes)
    skin = ["Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black", "Rocky Gray"]
    skin = random.choice(skin)
    hair = ["Red", "Black", "Grey", "Dark Brown", "Brown", "Dirty Blonde", "Blonde", "White"]
    hair = random.choice(hair)
    speed = 25
    traits.extend(["Gnome Cunning"])
    if subrace == "Deep":
        traits.extend(["Darkvision (120ft)", "Stone Camoflage"])
    if subrace == "Forest":
        traits.extend(["Darkvision (60ft)", "Natural Illusionist", "Speak with Small Beasts"])
    if subrace == "Rock":
        tool_profs.extend(["Artisan's Tools"])
        traits.extend(["Artificer's Lore", "Tinker"])

if race == "Goblin":
    attr_dex = stat_increase(attr_dex, 2)
    attr_con = stat_increase(attr_con, 1)
    age = normal(10,35)
    size_mod = normal(2,8)
    height = 2 * 12 + 11 + size_mod
    weight = 40 + size_mod
    eyes = "Beady Black"
    skin = ["Brownish Orange", "Greenish Orange", "Brownish Green", "Green"]
    skin = random.choice(skin)
    hair = ["Black", "Deep Grey", "Silver"]
    hair = random.choice(hair)
    speed = 30
    traits.extend(["Darkvision (60ft)", "Fury of the Small", "Nimble Escape"])

if race == "Goliath":
    attr_str = stat_increase(attr_str, 2)
    attr_con = stat_increase(attr_con, 1)
    age = normal(20,80)
    size_mod = normal(2,20)
    height = 6 * 12 + 8 + size_mod
    weight = 270 + size_mod * normal(2,12)
    eyes = ["Blue", "Green"]
    eyes = random.choice(eyes)
    skin = "Grey"
    hair = ["Black", "Dark Brown", "Dark Grey"]
    hair = random.choice(hair)
    speed = 30
    skill_profs.extend(["Athletics"])
    traits.extend(["Stone's Endurance", "Powerful Build", "Mountain Born"])
    
if race == "Hobgoblin":
    attr_con = stat_increase(attr_con, 2)
    attr_int = stat_increase(attr_int, 1)
    age = normal(20,80)
    size_mod = normal(2,16)
    height = 5 * 12 + 6 + size_mod
    weight = 175 + size_mod * normal(2,12)
    eyes = ["Black", "Red"]
    eyes = random.choice(eyes)
    skin = ["Orange", "Dirty Orange", "Red", "Dull Red", "Reddish Brown"]
    skin = random.choice(skin)
    hair = ["Dark Brown", "Dark Grey", "Orange", "Red"]
    hair = random.choice(hair)
    speed = 30
    traits.extend(["Darkvision (60ft)", "Martial Training", "Saving Face"])

if race == "Half-Elf":
    subrace = ["N/A", "Drow", "Sun", "Moon", "Wood"] # Keen Senses subrace removed because it is obsolete
    subrace = random.choice(subrace)
    attr_cha = stat_increase(attr_cha, 2)
    age = normal(20,160)
    size_mod = normal(2,16)
    height = 4 * 12 + 9 + size_mod
    weight = 110 + size_mod * normal(2,8)
    eyes = ["Blue", "Violet", "Green"]
    eyes = random.choice(eyes)
    skin = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown"]
    skin = random.choice(skin)
    hair = ["Red", "Blond", "Brown", "Black"]
    hair = random.choice(hair)
    speed = 30
    traits.extend(["Darkvision (60ft)", "Fey Ancestry"])
    if subrace == "N/A":
        traits.extend(["Skill Versatility"])
    if subrace == "Drow":
        traits.extend(["Drow Magic"])
    if subrace == "Sun" or subrace == "Moon":
        Choice = random.choice(["Elf Weapon Training", "Wizard Cantrip"])
        traits.extend([Choice])
    if subrace == "Wood":
        Choice = random.choice(["Elf Weapon Training", "Fleet of Foot", "Mask of the Wild"])
        traits.extend([Choice])

if race == "Halfling":
    subrace = ["Ghostwise", "Lightfoot", "Stout"]
    subrace = random.choice(subrace)
    attr_dex = stat_increase(attr_dex, 2)
    if subrace == "Ghostwise":
        attr_wis = stat_increase(attr_wis, 1)
    if subrace == "Lightfoot":
        attr_cha = stat_increase(attr_cha, 1)
    if subrace == "Stout":
        attr_con = stat_increase(attr_con, 1)
    age = normal(20,200)
    size_mod =  normal(2,8)
    height = 2 * 12 + 7 + size_mod
    weight = 35 + size_mod
    eyes = "Brown"
    skin = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black"]
    skin = random.choice(skin)
    hair = ["Aubrun", "Black", "Brown", "Gray"]
    hair = random.choice(hair)
    speed = 25
    traits.extend(["Lucky", "Brave", "Halfling Nimbleness"])
    if subrace == "Ghostwise":
        traits.extend(["Silent Speech"])
    if subrace == "Lightfoot":
        traits.extend(["Naturally Stealthy"])
    if subrace == "Stout":
        resistances.extend(["Poison"])
        traits.extend(["Stout Resilience"])
    
if race == "Half-Orc":
    attr_str = stat_increase(attr_str, 2)
    attr_con = stat_increase(attr_con, 1)
    age = normal(14,60)
    size_mod = normal(2,20)
    height = 4 * 12 + 10 + size_mod
    weight = 140 + size_mod * normal(2,12)
    eyes = ["Reddish Brown", "Reddish Blue", "Reddish Green", "Reddish Grey"]
    eyes = random.choice(eyes)
    skin = "Greyish Green"
    hair = ["Dark Brown", "Bald", "Red"]
    hair = random.choice(hair)
    speed = 30
    skill_profs.extend(["Intimidation"])
    traits.extend(["Darkvision (60ft)", "Relentless Endurance", "Savage Attacks"])

if race == "Human": # I have not accounted for the different Human ethnicities
    subrace = ["Stat Increase", "Variant", "Variant"] # Two chances for variant, just to spice things up
    subrace = random.choice(subrace)
    if subrace == "Stat Increase":
        attr_str = stat_increase(attr_str, 1)
        attr_dex = stat_increase(attr_dex, 1)
        attr_con = stat_increase(attr_con, 1)
        attr_int = stat_increase(attr_int, 1)
        attr_wis = stat_increase(attr_wis, 1)
        attr_cha = stat_increase(attr_cha, 1)
    if subrace == "Variant":
        choices = random.sample(stats, 2)  # Stats list is found on line 101 above the STR/DEX/CON/INT/WIS/CHA = 0
        if "STR" in choices:
            attr_str = stat_increase(attr_str, 1)
        if "DEX" in choices:
            attr_dex = stat_increase(attr_dex, 1)
        if "CON" in choices:
            attr_con = stat_increase(attr_con, 1)
        if "INT" in choices:
            attr_int = stat_increase(attr_int, 1)
        if "WIS" in choices:
            attr_wis = stat_increase(attr_wis, 1)
        if "CHA" in choices:
            attr_cha = stat_increase(attr_cha, 1)
    age = normal(20,60)
    size_mod = normal(2,20)
    height = 4 * 12 + 8 + size_mod
    weight = 110 + size_mod * normal(2,8)
    eyes = ["Brown", "Hazel", "Blue", "Green", "Grey", "Amber"]
    eyes = random.choice(eyes)
    skin = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black"]
    skin = random.choice(skin)
    hair = ["Black", "Brown", "Blonde", "Red", "White"]
    hair = random.choice(hair)
    speed = 30
    if subrace == "Variant":
        traits.extend(["Choice of Feat"])
        skill_profs.extend([random.choice(skills)])
        
if race == "Juiblexian":
    subrace = ["Corrosive", "Blasphemy", "Mnemonic"]
    subrace = random.choice(subrace)
    attr_con = stat_increase(attr_con, 2)
    if subrace == "Corrosive":
        attr_dex = stat_increase(attr_dex, 1)
    if subrace == "Blasphemy":
        attr_cha = stat_increase(attr_cha, 1)
    if subrace == "Mnemonic":
        attr_int = stat_increase(attr_int, 1)
    age = normal(100,200)
    size_mod = normal(2,20)
    height = 4 * 12 + 10 + size_mod
    weight = 80 + size_mod * normal(2,8)
    eyes = "N/A"
    skin = "Transparent " + random.choice(["Green", "Blueish White", "Yellow", "Orange", "Blue", "Red"])
    hair = "N/A"
    speed = 30
    immunities.extend(["Poison", "Poisoned"])
    traits.extend(["Amorphous Ooze", "Blind Vision", "Gelatinous Trance"])
    if subrace == "Corrosive":
        traits.extend(["Caustic Touch", "Corrosive Body"])
        resistances.extend(["Acid"])
    if subrace == "Blasphemy":
        traits.extend(["Elemental Chaos", "Innate Spellcasting"])
    if subrace == "Mnemonic":
        traits.extend(["False Appearance", "Mnemonic Echoes"])

if race == "Kender": # Extra Race I found https://www.dndbeyond.com/races/670-kender
    attr_dex = stat_increase(attr_dex, 2)
    attr_cha = stat_increase(attr_cha, 1)
    age = normal(15,80)
    size_mod = normal(2,8)
    height = 3 * 12 + 4 + size_mod
    weight = 50 + size_mod * random.randint(1,4)
    eyes = ["Brown", "Hazel", "Blue", "Green", "Grey", "Amber"]
    eyes = random.choice(eyes)
    skin = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black"]
    skin = random.choice(skin)
    hair = ["Black", "Brown", "Blonde", "Red", "White"]
    hair = random.choice(hair)
    speed = 25
    immunities.extend(["Frightened"])
    tool_profs.extend(["Thieves' Tools"])
    traits.extend(["Kender Pockets", "Nimbleness", "Taunt"])
    
if race == "Kenku":
    attr_dex = stat_increase(attr_dex, 2)
    attr_wis = stat_increase(attr_wis, 1)
    age = normal(12,45)
    size_mod = normal(2,16)
    height = 4 * 12 + 4 + size_mod
    weight = 50 + size_mod * random.randint(1,6)
    eyes = "Beady Black"
    skin = "Black"
    hair = "Black Feathers"
    speed = 30
    traits.extend(["Expert Forgery", "Mimicry"])
    KenkuSkills = ["Acrobatics", "Deception", "Stealth", "Sleight of Hand"]
    skill_profs.extend(random.sample(KenkuSkills, 2))
    
if race == "Kobold":
    attr_dex = stat_increase(attr_dex, 2)
    attr_str = stat_decrease(attr_str, 2)
    age = normal(8,80)
    size_mod = normal(2,8)
    height = 2 * 12 + 1 + size_mod
    weight = 25 + size_mod
    eyes = ["Burnt Orange", "Red"]
    eyes = random.choice(eyes)
    skin = ["Reddish Brown", "Green", "Blue"]
    skin = random.choice(skin)
    hair = "N/A"
    speed = 30
    traits.extend(["Darkvision (60ft)", "Grovel, Cower and Beg", "Pack Tactics", "Sunlight Sensitivity"])

if race == "Lizardfolk":
    attr_con = stat_increase(attr_con, 2)
    attr_wis = stat_increase(attr_wis, 1)
    age = normal(14,45)
    size_mod = normal(2,20)
    height = 4 * 12 + 9 + size_mod
    weight = 120 + size_mod * normal(2,12)
    eyes = ["Red", "Green", "Gold", "Orange", "Blue"]
    eyes = random.choice(eyes)
    skin = ["Green Scales", "Greenish Brown", "Brown Scales", "Black Scales", "Tan Scales", "Albino Scales"]
    skin = random.choice(skin)
    hair = ["Pair of Spikes", "Lots of Spikes", "N/A"]
    hair = random.choice(hair)
    speed = 30
    traits.extend(["Bite", "Cunning Artisan", "Hold Breath", "Natural Armour", "Hungry Jaws"])
    LizardfolkSkills = ["Animal Handling", "Nature", "Perception", "Stealth", "Survival"]
    skill_profs.extend(random.sample(LizardfolkSkills, 2))
    
if race == "Mousefolk": # Extra Race I found https://www.dndbeyond.com/races/61879-mousefolk
    attr_dex = stat_increase(attr_dex, 2)
    attr_cha = stat_increase(attr_cha, 1)
    age = normal(10,45)
    size_mod = normal(2,8)
    height = 2 * 12 + 11 + size_mod
    weight = 40 + size_mod
    eyes = ["Pink", "Black"]
    eyes = random.choice(eyes)
    skin = "Pink"
    hair = ["Beige Fur", "Black Fur", "Chocolate Fur", "Coffee Fur", "Cream Fur", "Ivory Fur", "Lilac Fur", "Silver Fur", "White Fur", "Tan Fur"]
    hair = random.choice(hair)
    speed = 25
    traits.extend(["Darkvision (60ft)", "Light Sleeper", "Mouse's Agility", "Mousefolk Senses", "Mouse's Survival"]) # I will be ediditing some of these for my campaign as they aren't well balanced
    
if race == "Orc":
    attr_str = stat_increase(attr_str, 2)
    attr_con = stat_increase(attr_con, 1)
    attr_int = stat_decrease(attr_int, 2)
    age = normal(12,30)
    size_mod = normal(2,16)
    height = 5 * 12 + 4 + size_mod
    weight = 175 + size_mod * normal(2,12)
    eyes = "Red"
    skin = ["Greenish Grey", "Light Grey", "Dark Grey"]
    skin = random.choice(skin)
    hair = "Black"
    speed = 30
    traits.extend(["Darkvision (60ft)", "Aggressive", "Powerful Build"])
    skill_profs.extend(["Intimidation"])
    
if race == "Succubus": # Extra class I found https://www.dndbeyond.com/races/1524-succubus
    attr_cha = stat_increase(attr_cha, 1)
    age = normal(20,1000)
    size_mod = normal(2,20)
    height = 4 * 12 + 8 + size_mod
    weight = 110 + size_mod * normal(2,8)
    eyes = ["Glowing Red", "Glowing Blue", "Glowing Brown", "Glowing Green"]
    eyes = random.choice(eyes)
    skin = ["Tan", "Olive", "White"]
    skin = random.choice(skin)
    hair = ["Black", "Red"]
    hair = random.choice(hair)
    speed = 30
    skill_profs.extend(["Persuasion"])
    traits.extend(["Charm", "Darkvision (60ft)", "Fiendish Nature", "Shapechanger", "Small Wings"]) # I might switch some of these around with playtesting
    vulnerabilities.extend(["Radiant"])

if race == "Tabaxi":
    attr_dex = stat_increase(attr_dex, 2)
    attr_cha = stat_increase(attr_cha, 1)
    age = normal(20,60)
    size_mod = normal(2,20)
    height = 4 * 12 + 10 + size_mod
    weight = 90 + size_mod * normal(2,8)
    eyes = ["Green", "Yellow"]
    eyes = random.choice(eyes)
    skin = "Pink"
    hair = ["Yelow", "Spotted Yellow", "Orange", "Spotted Orange", "Red", "Spotted Red"]
    hair = random.choice(hair)
    speed = 30
    traits.extend(["Darkvision (60ft)", "Feline Agility", "Cat Claws"])
    skill_profs.extend(["Perception", "Stealth"])
    
if race == "Tiefling":
    subrace = ["Asmodeus", "Baalzebul", "Devil's Tongue", "Dispater", "Feral", "Fierna", "Glasya", "Hellfire", "Levistus", "Mammon", "Mephistopheles", "Zariel"]
    subrace = random.choice(subrace)
    if subrace == "Asmodeus" or subrace == "Baalzebul" or subrace == "Devil's Tongue" or subrace == "Hellfire" or subrace == "Mammon" or subrace == "Mephistopheles":
        attr_cha = stat_increase(attr_cha, 2)
        attr_int = stat_increase(attr_int, 1)
    if subrace == "Dispater" or subrace == "Glasya":
        attr_cha = stat_increase(attr_cha, 2)
        attr_dex = stat_increase(attr_dex, 1)
    if subrace == "Feral":
        attr_dex = stat_increase(attr_dex, 2)
        attr_int = stat_increase(attr_int, 1)
    if subrace == "Fierna":
        attr_cha = stat_increase(attr_cha, 2)
        attr_wis = stat_increase(attr_wis, 1)
    if subrace == "Livistus":
        attr_cha = stat_increase(attr_cha, 2)
        attr_con = stat_increase(attr_con, 1)
    if subrace == "Zariel":
        attr_cha = stat_increase(attr_cha, 2)
        attr_str = stat_increase(attr_str, 1)
    age = normal(20,60)
    size_mod = normal(2,16)
    height = 4 * 12 + 9 + size_mod
    weight = 110 + size_mod * normal(2,8)
    eyes = ["Solid Orb of Red", "Solid Orb of Black", "Solid Orb of White", "Solid Orb of Silver", "Solid Orb of Gold"]
    eyes = random.choice(eyes)
    skin = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black", "Light Red", "Maroon", "Burgundy", "Dark Red", "Red"]
    skin = random.choice(skin)
    hair = ["Red", "Brown", "Black", "Dark Blue", "Purple"]
    hair = random.choice(hair)
    speed = 30
    traits.extend(["Darkvision (60ft)"])
    resistances.extend(["Fire"])
    if subrace == "Asmodeus" or subrace == "Feral":
        traits.extend(["Infernal Legacy"])
    if subrace == "Baalzebul":
        traits.extend(["Legacy of Maladomini"])
    if subrace == "Devil's Tongue":
        traits.extend(["Devil's Tongue"])
    if subrace == "Dispater":
        traits.extend(["Legacy of Dis"])
    if subrace == "Fierna":
        traits.extend(["Legacy of Phlegethos"])
    if subrace == "Glasya":
        traits.extend(["Legacy of Malbolge"])
    if subrace == "Hellfire":
        traits.extend(["Hellfire"])
    if subrace == "Levistus":
        traits.extend(["Legacy of Stygia"])
    if subrace == "Mammon":
        traits.extend(["Legacy of Minauros"])
    if subrace == "Mephistopheles":
        traits.extend(["Legacy of Cania"])
    if subrace == "Zariel":
        traits.extend(["Legacy of Avernus"])
    
if race == "Tortle":
    attr_str = stat_increase(attr_str, 2)
    attr_wis = stat_increase(attr_wis, 1)
    age = normal(30,320)
    size_mod = normal(2,20)
    height = 4 * 12 + 8 + size_mod
    weight = 350 + size_mod * normal(2,12)
    eyes = ["Yellow", "Green", "Red", "Orange", "Brown", "Brownish Yellow"]
    eyes = random.choice(eyes)
    skin = ["Olive Green", "Blueish Green"]
    skin = random.choice(skin)
    hair = "N/A"
    speed = 25
    skill_profs.extend(["Survival"])
    traits.extend(["Claws", "Hold Breath", "Natural Armour", "Shell Defense"])
    
if race == "Triton":
    attr_str = stat_increase(attr_str, 1)
    attr_con = stat_increase(attr_con, 1)
    attr_cha = stat_increase(attr_cha, 1)
    age = normal(15,170)
    size_mod = normal(2,20)
    height = 4 * 12 + 6 + size_mod
    weight = 90 + size_mod * normal(2,8)
    eyes = ["Brown", "Hazel", "Blue", "Green", "Grey", "Amber"]
    eyes = random.choice(eyes)
    skin = ["Silver", "Blueish Silver"]
    skin = random.choice(skin)
    hair = ["Deep Blue", "Greenish Blue", "Green"]
    hair = random.choice(hair)
    speed = 30
    traits.extend(["Amphibious", "Control Air and Water", "Emissary of the Sea", "Guardians of the Depths"])
    
if race == "Yuan-Ti Pureblood":
    attr_cha = stat_increase(attr_cha, 2)
    attr_int = stat_increase(attr_int, 1)
    age = normal(20,60)
    size_mod = normal(2,20)
    height = 4 * 12 + 8 + size_mod
    weight = 110 + size_mod * normal(2,8)
    eyes = ["Red", "Orange", "Silver", "Copper", "Green", "Yellow"]
    eyes = random.choice(eyes)
    skin = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black"]
    skin = random.choice(skin)
    hair = ["Black", "Brown", "Blonde", "Red", "White"]
    hair = random.choice(hair)
    speed = 30
    immunities.extend(["Poison", "Poisoned"])
    traits.extend(["Darkvision (60ft)", "Innate Spellcasting", "Magic Resistance"])
    
STRMOD = stat_mod(str)
DEXMOD = stat_mod(dex)
CONMOD = stat_mod(con)
INTMOD = stat_mod(int)
WISMOD = stat_mod(wis)
CHAMOD = stat_mod(cha)

# Alchemist, Artificer, Blood Hunter, Cardcaster, Diabolist, Feywalker, Morph, Occultist temporarily removed
character_class = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
character_class = random.choice(character_class)

# =============================================================================
# if Class == "Alchemist":
# =============================================================================
    
# =============================================================================
# if Class == "Artificer":
# =============================================================================

if character_class == "Barbarian":
    if level >= 3:
        subclass = ["Path of the Ancestral Guardian", "Path of the Battlerager", "Path of the Berserker", "Path of the Storm Herald", "Path of the Totem Warrior", "Path of the Zealot"]
        subclass = random.choice(subclass)
    hp = hp + hitpoints(12)
    armour_profs.extend(["Light Armour", "Medium Armour", "Shields"])
    weapon_profs.extend(["Simple Weapons", "Martial Weapons"])
    saving_throw_profs.extend(["STR", "CON"])
    skill_profs.extend(random.sample(["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"], 2))
    equipment.extend([random.choice(["Greataxe", random.choice(martial_melee)]), random.choice(["Two Handaxes", random.choice(simple_weapons)]), "Explorer's Pack", "Four Javelins"])
    
if character_class == "Bard":
    if level >= 3:
        subclass = ["College of Glamour", "College of Lore", "College of Satire", "College of Swords", "College of Valor", "College of Whispers"]
        subclass = random.choice(subclass)
    hp = hp + hitpoints(8)
    armour_profs.extend(["Light Armour"])
    weapon_profs.extend(["Simple Weapons", "Hand Crossbows", "Longswords", "Rapiers", "Shortswords"])
    tool_profs.extend(random.sample(musical_instruments, 3))
    saving_throw_profs.extend(["DEX", "CHA"])
    skill_profs.extend(random.sample(skills, 3))
    equipment.extend([random.choice(["Rapier", "Longsword", random.choice(simple_weapons)]), random.choice(["Diplomat's Pack", "Entertainer's Pack"]), random.choice(["Lute", random.choice(musical_instruments)]), "Leather Armour", "Dagger"])
    
# =============================================================================
# if Class == "Blood Hunter":
# =============================================================================

# =============================================================================
# if Class == "Cardcaster":
# =============================================================================
    
if character_class == "Cleric":
    subclass = ["Arcana Domain", "Ambition Domain", "City Domain", "Death Domain", "Forge Domain", "Grave Domain", "Knowledge Domain", "Life Domain", "Light Domain", "Nature Domain", "Order Domain", "Protection Domain", "Solidarity Domain", "Strength Domain", "Tempest Domain", "Trickery Domain", "War Domain", "Zeal Domain"]
    subclass = random.choice(subclass)
    hp = hp + hitpoints(8)
    armour_profs.extend(["Light Armour", "Medium Armour", "Shields"])
    weapon_profs.extend(["Simple Weapons"])
    saving_throw_profs.extend(["WIS", "CHA"])
    skill_profs.extend(random.sample(["History", "Insight", "Medicine", "Persuasion", "Religion"], 2))
    if "Warhammer" in weapon_profs or "Martial Weapons" in weapon_profs:
        equipment.extend([random.choice(["Mace", "Warhammer"])])
    else:
        equipment.extend(["Mace"])
    if "Chain Mail" in armour_profs or "Heavy Armour" in armour_profs:
        equipment.extend([random.choice(["Scale Mail", "Leather Armour", "Chain Mail"])])
    else:
        equipment.extend([random.choice(["Scale Mail", "Leather Armour"])])
    equipment.extend([random.choice(["Light Crossbow with 20 Bolts", random.choice(simple_weapons)]), random.choice(["Priest's Pack", "Explorer's Pack"]), "Shield", "Holy Symbol"])
    
# =============================================================================
# if Class == "Diabolist":
# =============================================================================
    
if character_class == "Druid":
    if level >= 2:
        subclass = ["Circle of Dreams", "Circle of the Land", "Circle of the Moon", "Circle of the Shepherd", "Circle of Spores", "Circle of Twilight"]
        subclass = random.choice(subclass)
        if subclass == "Circle of the Land":
            land = random.choice(["(Arctic)", "(Coast)", "(Desert)", "(Forest)", "(Grassland)", "(Mountain)", "(Swamp)", "(Underdark)"])
            subclass = "Circle of the Land " + land
    hp = hp + hitpoints(8)
    armour_profs.extend(["Light Armour", "Medium Armour", "Shields"])
    weapon_profs.extend(["Clubs", "Daggers", "Darts", "Javelins", "Maces", "Quarterstaffs", "Scimitars", "Sickles", "Slings", "Spears"])
    tool_profs.extend(["Herbalism Kit"])
    saving_throw_profs.extend(["INT", "WIS"])
    skill_profs.extend(random.sample(["Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"], 2))
    equipment.extend([random.choice(["Wooden Shield", random.choice(simple_weapons)]), random.choice(["Scimitar", random.choice(simple_melee)]), "Leather Armour", "Explorer's Pack", "Druidic Focus"])
    
# =============================================================================
# if Class == "Feywalker":
# =============================================================================
    
if character_class == "Fighter":
    fighting_style = ["Archery", "Defense", "Dueling", "Great Weapon Fighting", "Protection", "Two-Weapon Fighting"]
    fighting_style = random.choice(fighting_style)
    if level >= 3:
        subclass = ["Arcane Archer", "Battle Master", "Brute", "Cavalier", "Champion", "Eldritch Knight", "Purple Dragon Knight", "Samurai", "Scout", "Sharpshooter"]
        subclass = random.choice(subclass)
    hp = hp + hitpoints(10)
    armour_profs.extend(["Light Armour, Medium Armour, Heavy Armour", "Shields"])
    weapon_profs.extend(["Simple Weapons", "Martial Weapons"])
    saving_throw_profs.extend(["STR", "CON"])
    skill_profs.extend(random.sample(["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"], 2))
# =============================================================================
#   This whole equipment section got messed up because one choice of equipment gives multiple items, which gives my code lists within lists. My print functions don't work with lists within lists. I'm looking for a way to simplify this. Similar issue encountered with Paladin and Ranger
# =============================================================================
    EqptExtnd = [random.choice(["Light Crossbow with 20 Bolts", "Two Handaxes"]), random.choice(["Dungeoneer's Pack", "Explorer's Pack"])]
    EqptExtnd.extend(random.choice([["Chain Mail"], ["Leather Armour", "Longbow with 20 Arrows"]]))
    EqptExtnd.extend(random.choice([[random.choice(martial_weapons), "Shield"], random.sample(martial_weapons, 2)]))
    equipment.extend(EqptExtnd)
    
if character_class == "Monk":
    if level >= 3:
        subclass = ["Way of the Drunken Master", "Way of the Four Elements", "Way of the Kensei", "Way of the Long Death", "Way of the Open Hand", "Way of Shadow", "Way of the Sun Soul", "Way of Tranquility"]
        subclass = random.choice(subclass)
    hp = hp + hitpoints(8)
    weapon_profs.extend(["Simple Weapons", "Shortswords"])
    tool_profs.extend([random.choice([random.choice(musical_instruments), random.choice(artisan_tools)])])
    saving_throw_profs.extend(["STR", "DEX"])
    skill_profs.extend(random.sample(["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"], 2))
    equipment.extend([random.choice(["Shortsword", random.choice(simple_weapons)]), random.choice(["Dungeoneer's Pack", "Explorer's Pack"]), "10 Darts"])
    
# =============================================================================
# if Class == "Morph":
# =============================================================================
    
# =============================================================================
# if Class == "Occultist":
# =============================================================================
    
if character_class == "Paladin":
    if level >= 2:
        fighting_style = ["Defense", "Dueling", "Great Weapon Fighting", "Protection"]
        fighting_style = random.choice(fighting_style)
    if level >= 3:
        subclass = ["Oath of the Ancients", "Oath of Conquests", "Oath of the Crown", "Oath of Devotion", "Oath of Redemption", "Oath of Vengeance", "Oathbreaker", "Oath of Treachery"]
        subclass = random.choice(subclass)
    hp = hp + hitpoints(10)
    armour_profs.extend(["Light Armour", "Medium Armour", "Heavy Armour", "Shields"])
    weapon_profs.extend(["Simple Weapons", "Martial Weapons"])
    saving_throw_profs.extend(["WIS", "CHA"])
    skill_profs.extend(random.sample(["Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"], 2))
    EqptExtnd = random.choice([[random.choice(martial_weapons), "Shield"], random.sample(martial_weapons, 2)])
    EqptExtnd.extend([random.choice(["5 Javelins", random.choice(simple_melee)])])
    EqptExtnd.extend(["Chain Mail", "Holy Symbol"])
    equipment.extend(EqptExtnd)
    
if character_class == "Ranger":
    if level >= 2:
        fighting_style = ["Archery", "Defense", "Dueling", "Two-Weapon Fighting"]
        fighting_style = random.choice(fighting_style)
    if level >= 3:
        subclass = ["Beast Master", "Gloom Stalker", "Horizon Walker", "Hunter", "Monster Slayer", "Primeval Guardian"]
        subclass = random.choice(subclass)
    hp = hp + hitpoints(10)
    armour_profs.extend(["Light Armour", "Medium Armour", "Shields"])
    weapon_profs.extend(["Simple Weapons", "Martial Weapons"])
    saving_throw_profs.extend(["STR", "DEX"])
    skill_profs.extend(random.sample(["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"], 3))
    EqptExtnd =[random.choice(["Scale Mail", "Leather Armour"])]
    EqptExtnd.extend(random.choice([["Two Shortswords"], random.sample(simple_melee, 2)]))
    EqptExtnd.extend([random.choice(["Dungeoneer's Pack", "Explorer's Pack"])])
    EqptExtnd.extend(["Longbow with 20 Arrows"])
    equipment.extend(EqptExtnd)
    
if character_class == "Rogue":
    if level >= 3:
        subclass = ["Arcane Trickster", "Assassin", "Inquisitive", "Mastermind", "Scout", "Swashbuckler", "Thief"]
        subclass = random.choice(subclass)
    hp = hp + hitpoints(8)
    armour_profs.extend(["Light Armour"])
    weapon_profs.extend(["Simple Weapons", "Hand Crossbows", "Longswords", "Rapiers", "Shortswords"])
    tool_profs.extend(["Thieves' Tools"])
    saving_throw_profs.extend(["DEX", "INT"])
    skill_profs.extend(random.sample(["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"], 4))
    equipment.extend([random.choice(["Rapier", "Shortsword"]), random.choice(["Shortbow with 20 Arrows", "Shortsword"]), random.choice(["Burglar's Pack", "Dungeoneer's Pack", "Explorer's Pack"]), "Leather Armour", "Two Daggers", "Thieves's Tools"])
    
if character_class == "Sorcerer":
    subclass = ["Divine Soul", "Draconic Bloodline", "Giant Soul", "Pheonix Sorcery", "Pyromancer", "Sea Sorcery", "Shadow Magic", "Stone Soercery", "Storm Sorcery", "Wild Magic"]
    subclass = random.choice(subclass)
    hp = hp + hitpoints(6)
    weapon_profs.extend(["Daggers", "Darts", "Slings", "Quarterstaffs", "Light Crossbows"])
    saving_throw_profs.extend(["CON", "CHA"])
    skill_profs.extend(random.sample(["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"], 2))
    equipment.extend([random.choice(["Light Crossbow with 20 Bolts", random.choice(simple_weapons)]), random.choice(["Component Pouch", "Arcane Focus"]), random.choice(["Dungeoneer's Pack", "Explorer's Pack"]), "Two Daggers"])
    
if character_class == "Warlock":
    subclass = ["The Archfey", "The Celestial", "The Fiend", "The Ghost in the Machine", "The Great Old One", "The Hexblade", "The Raven Queen", "The Seeker", "The Undying"]
    subclass = random.choice(subclass)
    if level >= 3:
        fighting_style = ["Pact of the Chain", "Pact of the Blade", "Pact of the Tome"]
        fighting_style = random.choice(fighting_style)
    hp = hp + hitpoints(8)
    armour_profs.extend(["Light Armour"])
    weapon_profs.extend(["Simple Weapons"])
    saving_throw_profs.extend(["WIS", "CHA"])
    skill_profs.extend(random.sample(["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"], 2))
    equipment.extend([random.choice(["Light Crossbow with 20 Bolts", random.choice(simple_weapons)]), random.choice(["Component Pouch", "Arcane Focus"]), random.choice(["Scholar's Pack", "Dungeoneer's Pack"]), "Leather Armour", random.choice(simple_weapons), "Two Daggers"])
    
if character_class == "Wizard":
    if level >= 2:
        subclass = ["Artificier", "Bladesinger", "Lore Mastery", "School of Abjuration", "School of Conjuration", "School of Divination", "School of Enchantment", "School of Evocation", "School of Illusion", "School of Invention", "School of Necromancy", "School of Transmutation", "Technomancy", "Theurgy", "War Magic"]
        subclass = random.choice(subclass)
    hp = hp + hitpoints(6)
    weapon_profs.extend(["Daggers", "Darts", "Slings", "Quarterstaffs", "Light Crossbows"])
    saving_throw_profs.extend(["INT", "WIS"])
    skill_profs.extend(random.sample(["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"], 2))
    equipment.extend([random.choice(["Quarterstaff", "Dagger"]), random.choice(["Component Pouch", "Arcane Focus"]), random.choice(["Scholar's Pack", "Explorer's Pack"]), "Spellbook"])

# Currently Removed: "Dissenter"
background = ["Acolyte", "Anthropologist", "Archaeologist", "Black Fist Double Agent", "Caravan Specialist", "Charlatan", "City Watch", "Clan Crafter", "Cloistered Scholar", "Courtier", "Criminal", "Dragon Casualty", "Earthspur Miner", "Entertainer", "Faction Agent", "Far Traveller", "Folk Hero", "Gate Urchin", "Guild Artisan", "Harborfolk", "Haunted One", "Hermit", "Hillsfar Merchant", "Hillsfar Smuggler", "House Agent", "Inheritor", "Initiate", "Inquisitor", "Iron Route Bandit", "Knight of the Order", "Mercenary Veteran", "Mulmaster Aristocrat", "Noble", "Outlander", "Phlan Insurgent", "Phlan Refugee", "Sage", "Sailor", "Secret Identity", "Shade Fanatic", "Soldier", "Stojanow Prisoner", "Ticklebelly Nomad", "Trade Sheriff", "Urban Bounty Hunter", "Urchin", "Uthgardt Tribe Member", "Vizier", "Waterdhavian Noble"]
background = random.choice(background)

if background == "Acolyte":
    skill_profs.extend(["Insight", "Religion"])
    equipment.extend(["Holy Symbol", random.choice(["Prayer Book", "Prayer Wheel"]), "5 Sticks of Incense", "Vestments", "Common Clothes", "15 gp"])
    
if background == "Anthropologist":
    skill_profs.extend(["Insight", "Religion"])
    equipment.extend(["Leather-Bound Diary", "Bottle of Ink", "Ink Pen", "Set of Traveler's Clothes", "One Trinket of Special Significance", "10 gp"])
    
if background == "Archaeologist":
    skill_profs.extend(["History", "Survival"])
    tool_profs.extend([random.choice(["Cartographer's Tools", "Navigator's Tools"])])
    equipment.extend([random.choice(["Wooden Case Containing a Map to a Ruin", "Wooden Case Containing a Map to a Dungeon"]), "Bullseye Lantern", "Miner's Pick", "Set of Traveler's Clothes", "Shovel", "Two-Person Tent", "Trinket Recovered from a Dig Site", "25 gp"])

if background == "Black Fist Double Agent":
    skill_profs.extend(["Deception", "Insight"])
    black_fist_double_agent_tool = random.choice([random.choice(gaming_sets), random.choice(artisan_tools)])
    tool_profs.extend(["Disguise Kit", black_fist_double_agent_tool])
    equipment.extend(["Disguise Kit", "Common Clothes", "Tears of Virulence Emblem", "Writ of Free Agency Signed by the Lord Regent", black_fist_double_agent_tool, "15 gp"])
    
if background == "Caravan Specialist":
    skill_profs.extend(["Animal Handling", "Survival"])
    tool_profs.extend(["Land Vehicles"])
    equipment.extend(["Whip", "Tent", "Regional Map", "Traveling Clothes", "10 gp"])
    
if background == "Charlatan":
    skill_profs.extend(["Deception", "Sleight of Hand"])
    tool_profs.extend(["Disguise Kit", "Forgery Kit"])
    equipment.extend(["Fine Clothes", "Disguise Kit", random.choice(["Ten Stoppered Bottles Filled with Coloured Liquid", "Set of Weighted Dice", "Deck of Marked Cards", "Signet Ring of an Imaginary Duke"]), "15 gp"])
    
if background == "City Watch":
    background = random.choice(["City Watch Patrol", "City Watch Investigator"])
    skill_profs.extend(["Insight"])
    if background == "City Watch Patrol":
        skill_profs.extend(["Athletics"])
    if background == "City Watch Investigator":
        skill_profs.extend(["Investigation"])
    equipment.extend(["Uniform in the Style of Your Unit and Indicative of Your Rank", "Horn with which to Summon Help", "Set of Manacles", "10 gp"])
    
if background == "Clan Crafter":
    skill_profs.extend(["History", "Insight"])
    clan_crafter_artisan_tools = random.choice(artisan_tools)
    tool_profs.extend([clan_crafter_artisan_tools])
    equipment.extend([clan_crafter_artisan_tools, "Maker's Mark Chisel", "Traveler's Clothes", "Gem Worth 10 gp", "5 gp"])
    
if background == "Cloistered Scholar":
    skill_profs.extend(["History", random.choice(["Arcana", "Nature", "Religion"])])
    equipment.extend(["Scholar's Robes of Your Cloister", "Writing Kit", "Borrowed Book on the Subject of Your Current Study", "10 gp"])
    
if background == "Cormanthor Refugee":
    skill_profs.extend(["Nature", "Survival"])
    cormantor_refugee_artisan_tools = random.choice(artisan_tools) # Introducing a temporary variable so the same artisan's tools will be included in the equipment and proficiencies
    tool_profs.extend([cormantor_refugee_artisan_tools])
    equipment.extend(["Two-Person Tent", cormantor_refugee_artisan_tools, "Holy Symbol", "Traveler's Clothes", "5 gp"])
    
if background == "Courtier":
    skill_profs.extend(["Insight", "Persuasion"])
    equipment.extend(["Set of Fine Clothes", "5 gp"])
    
if background == "Criminal":
    specialty = ["Blackmailer", "Burglar", "Enforcer", "Fence", "Highway Robber", "Hired Killer", "Pickpocket", "Smuggler", "Spy"]
    background = "Criminal " + random.choice(specialty)
    skill_profs.extend(["Deception", "Stealth"])
    tool_profs.extend([random.choice(gaming_sets), "Thieves' Tools"])

# =============================================================================
# if Background == "Dissenter":  # Don't know what Dissenters get for proficiencies or equipment
#     SkillProficiencies.extend([])
# =============================================================================
    
if background == "Dragon Casualty": # Tool proficiency is based on origin
    origin = random.choice(["Dockworker/Fisherman", "Tradesperson/Merchant", "Black Fist Soldier", "Adventurer", "Entertainer", "Scholar/Healer", "Criminal", "Unskilled Labourer"])
    background = "Dragon Casualty who used to be a " + origin
    if origin == "Dockworker/Fisherman":
        tool_profs.extend(["Water Vehicles"])
    if origin == "Tradesperson/Merchant":
        tool_profs.extend([random.choice(artisan_tools)])
    if origin == "Black Fist Soldier":
        tool_profs.extend([random.choice([random.choice(artisan_tools), "Land Vehicles"])])
    if origin == "Adventurer":
        tool_profs.extend(["Land Vehicles"])
    if origin == "Entertainer":
        tool_profs.extend([random.choice(musical_instruments)])
    if origin == "Scholar/Healer":
        tool_profs.extend([random.choice(["Alchemist's Supplies", "Herbalism Kit"])])
    if origin == "Criminal":
        tool_profs.extend([random.choice(["Thieves' Tools", "Forgery Kit", "Disguise Kit"])])
    if origin == "Unskilled Labourer":
        tool_profs.extend([random.choice(gaming_sets)])
    skill_profs.extend(["Intimidation", "Survival"])
    equipment.extend(["Dagger", "Tattered Rags", "Loaf of Moldy Bread", "Small Cast-Off Scale Belonging to Vorgansharax - The Maimed Virulence", "5 gp"])

if background == "Earthspur Miner":
    skill_profs.extend(["Athletics", "Survival"])
    equipment.extend([random.choice(["Shovel", "Miner's Pick"]), "Block and Tackle", "Climber's Kit", "Set of Common Clothes", "5 gp"])
    
if background == "Entertainer":
    routine = random.sample(["an Actor", "a Dancer", "a Fire-Eater", "a Gladiator", "a Jester", "a Juggler", "an Instrumentalist", "a Poet", "a Singer", "a Storyteller", "a Tumbler"], 3) # The handbook says up to 3 routines, going with 3 to spice things up. Gladiator is also included in here for fun
    background = "Entertainer who is " + ", and ".join(routine)
    skill_profs.extend(["Acrobatics", "Performance"])
    EntertainerMusicalInstrument = random.choice(musical_instruments)  # Introducing a temporary variable so the same instrument will be included in the equipment and proficiencies
    tool_profs.extend(["Disguise Kit", EntertainerMusicalInstrument])
    equipment.extend([EntertainerMusicalInstrument, random.choice(["Love Letter from an Admirer", "Lock of Hair from an Admirer", "Trinket from an Admirer"]), "Costume", "15 gp"])
    if "a Gladiator" in routine:
        GladiatorWeapon = random.choice(["Trident", "Net"])
        weapon_profs.extend([GladiatorWeapon])
        equipment.extend([GladiatorWeapon])
    
if background == "Faction Agent":
    faction = random.choice(["The Emerald Enclave", "The Harpers", "The Lord's Alliance", "The Order of the Gauntlet", "The Zhentarim"])
    background = "Faction Agent of " + faction
    skill_profs.extend(["Insight"])
    if faction == "The Emerald Enclave":
        skill_profs.extend(["Nature"])
    if faction == "The Harpers":
        skill_profs.extend(["Investigation"])
    if faction == "The Lord's Alliance":
        skill_profs.extend(["History"])
    if faction == "The Order of the Gauntlet":
        skill_profs.extend(["Religion"])
    if faction == "The Zhentarim":
        skill_profs.extend(["Deception"])
    equipment.extend([random.choice(["Badge of " + faction, "Emblem of " + faction]), "Set of Common Clothes", "15 gp"])
    if faction == "The Harpers" or faction == "The Zhentarim":
        equipment.extend(["Copy of a Code-Book from " + faction])
    else: 
        equipment.extend(["Copy of a Seminal Text from " + faction])
    
if background == "Far Traveler":
    reason = random.choice(["Emissary", "Exile", "Fugitive", "Pilgrim", "Sightseer", "Wanderer"])
    origin = random.choice(["Evermeet", "Halruaa", "Kara-Tur", "Mulhorand", "Sossal", "Zakhara", "The Underdark"])
    background = "Far Traveler " + reason + " from " + origin
    skill_profs.extend(["Insight", "Perception"])
    far_traveler_tool = random.choice([random.choice(musical_instruments), random.choice(gaming_sets)])
    tool_profs.extend([far_traveler_tool])
    equipment.extend([far_traveler_tool, "Poorly Wrought Maps from " + origin, "Small Piece of Jewelry Worth 10 gp from " + origin, "5 gp"])
    
if background == "Folk Hero":
    skill_profs.extend(["Animal Handling", "Survival"])
    folk_hero_tools = random.choice(artisan_tools)
    tool_profs.extend([folk_hero_tools, "Land Vehicles"])
    equipment.extend([folk_hero_tools, "Shovel", "Iron Pot", "Set of Common Clothes", "10 gp"])
    
if background == "Gate Urchin":
    skill_profs.extend(["Deception", "Sleight of Hand"])
    gate_urchin_musical_instrument = random.choice(musical_instruments)
    tool_profs.extend(["Thieves' Tools", gate_urchin_musical_instrument])
    equipment.extend(["Battered Alms Box", gate_urchin_musical_instrument, random.choice(["Cast-Off Military Jacket", "Cast-Off Cap", "Cast-Off Scarf"]), "Set of Common Clothes", "10 gp"])
    
if background == "Guild Artisan":
    skill_profs.extend(["Insight", "Persuasion"])
    guild_artisan_tools = random.choice(artisan_tools)
    tool_profs.extend([guild_artisan_tools])
    equipment.extend([guild_artisan_tools, "Letter of Introduction from Your Guild", "15 gp"])
    
if background == "Harborfolk":
    skill_profs.extend(["Athletics", "Sleight of Hand"])
    harborfolk_gaming_set = random.choice(gaming_sets)
    tool_profs.extend([harborfolk_gaming_set, "Water Vehicles"])
    equipment.extend([harborfolk_gaming_set, "Fishing Tackle", "Set of Common Clothes", "Rowboat", "5 gp"])
    
if background == "Haunted One":
    skill_profs.extend(random.choice(["Arcana", "Investigation", "Religion", "Survival"]))
    equipment.extend(["Monster Hunter's Pack", "Gothic Trinket"])

if background == "Hermit":
    skill_profs.extend(["Medicine", "Religion"])
    tool_profs.extend(["Herbalism Kit"])
    equipment.extend(["Scroll Case Stuffed Full of Notes from Your " + random.choice(["Prayers", "Studies"]), "Winter Blanket", "Set of Common Clothes", "Herbalism Kit", "5 gp"])
    
if background == "Hillsfar Merchant":
    skill_profs.extend(["Insight", "Persuasion"])
    tool_profs.extend(["Land Vehicles", "Water Vehicles"])
    equipment.extend(["Set of Clothes", "Signet Ring", "Letter of Introduction from Your Family's Trading House", "25 gp"])

if background == "Hillsfar Smuggler":
    skill_profs.extend(["Perception", "Stealth"])
    tool_profs.extend(["Forgery Kit"])
    equipment.extend(["Forgery Kit", "Set of Common Clothes", "5 gp"])
    
if background == "House Agent":
    house = random.choice(["Cannith", "Deneith", "Ghallanda", "Jorasco", "Kundarak", "Lyrandar", "Medani", "Orien", "Phiarlan", "Sivis", "Tharashk", "Thuranni", "Vadalis"])
    background = "House Agent of the " + house + " House"
    skill_profs.extend(["Investigation", "Persuasion"])
    if house == "Cannith":
        tool_profs.extend(["Alchemist's Supplies", "Tinker's Tools"])
    if house == "Deneith":
        tool_profs.extend([random.choice(gaming_sets), "Land Vehicles"])
    if house == "Ghallanda":
        tool_profs.extend(["Brewer's Supplies", "Cook's Utensils"])
    if house == "Jorasco":
        tool_profs.extend(["Alchemist's Supplies", "Herbalism Kit"])
    if house == "Kundarak":
        tool_profs.extend(["Tinker's Tools", "Thieves' Tools"])
    if house == "Lyrandar":
        tool_profs.extend(["Sea Vehicles", "Air Vehicles", "Navigator's Tools"])
    if house == "Medani":
        tool_profs.extend(["Thieves' Tools", "Disguise Kit"])
    if house == "Orien":
        tool_profs.extend(["Land Vehicles", random.choice(gaming_sets)])
    if house == "Phiarlan":
        tool_profs.extend(["Disguise Kit", random.choice(musical_instruments)])
    if house == "Sivis":
        tool_profs.extend(["Calligrapher's Tools", "Forgery Kit"])
    if house == "Tharashk":
        tool_profs.extend(["Thieve's Tools", random.choice(gaming_sets)])
    if house == "Thuranni":
        tool_profs.extend(["Poisoner's Kit", random.choice(gaming_sets)])
    if house == "Vadalis":
        tool_profs.extend(["Land Vehicles", "Herbalism Kit"])
    equipment.extend(["Set of Fine Clothes", house + " Signet Ring", "ID Papers", "20 gp"])
    
if background == "Inheritor":
    skill_profs.extend(["Survival", random.choice(["Arcana", "History", "Religion"])])
    inheritor_tool = random.choice([random.choice(gaming_sets), random.choice(musical_instruments)])
    tool_profs.extend([inheritor_tool])
    equipment.extend(["Your Inheritance: " + random.choice([random.choice(["A Map", "A Letter", "A Journal"]), "A Trinket", "An Article of Clothing", "A Piece of Jewelry", "An Arcane " + random.choice(["Book", "Formulary"]), "A Written " + random.choice(["Story", "Song", "Poem", "Secret"]), "A Tattoo"]), "Set of Traveler's Clothes", inheritor_tool, "15 gp"])
    
if background == "Initiate":
    skill_profs.extend(["Athletics", "Intimidation"])
    initiate_gaming_set = random.choice(gaming_sets)
    tool_profs.extend([initiate_gaming_set, "Land Vehicles"])
    equipment.extend(["Simple Puzzle Box", "Scroll Containing the Teachings of the Gods", initiate_gaming_set, "Set of Common Clothes", "15 gp"])
    
if background == "Inquisitor":
    skill_profs.extend(["Investigation", "Religion"])
    tool_profs.extend([random.choice(artisan_tools), "Thieves' Tools"])
    equipment.extend(["Holy Symbol", "Set of Traveler's Clothes", "15 gp"])
    
if background == "Iron Route Bandit":
    skill_profs.extend(["Animal Handling", "Stealth"])
    tool_profs.extend([random.choice(gaming_sets), "Land Vehicles"])
    equipment.extend(["Set of Dark Common Clothes", "Pack Saddle", "Burglar's Pack", "5 gp"])
    
if background == "Knight of the Order":
    order = random.choice(["the Unicorn", "Myth Drannor", "the Silver Chalice"])
    background = "Knight of the Order of " + order
    skill_profs.extend(["Persuasion"])
    if order == "the Unicorn":
        skill_profs.extend([random.choice(["Arcana", "Religion"])])
    if order == "Myth Drannor":
        skill_profs.extend([random.choice(["Nature", "History"])])
    if order == "the Silver Chalice":
        skill_profs.extend([random.choice(["History", "Religion"])])
    tool_profs.extend([random.choice([random.choice(gaming_sets), random.choice(musical_instruments)])])
    equipment.extend(["Set of Traveler's Clothes", random.choice(["Signet", "Banner", "Seal"]) + " Representing Your Rank in the Order of " + order, "10 gp"])
    
if background == "Mercenary Veteran":
    company = random.choice(["The Chill", "Silent Rain", "The Bloodaxes"])
    background = "Mercenary Veteran from " + company
    skill_profs.extend(["Athletics", "Persuasion"])
    mercenary_veteran_gaming_set = random.choice(gaming_sets)
    tool_profs.extend([mercenary_veteran_gaming_set, "Land Vehicles"])
    equipment.extend(["Uniform from " + company, "Insignia of Your Rank from " + company, mercenary_veteran_gaming_set, "10 gp"])
    
if background == "Mulmaster Aristocrat":
    skill_profs.extend(["Deception", "Performance"])
    mulmaster_aristocrat_artisan_tool = random.choice(artisan_tools)
    mulmaster_aristocrat_musical_instrument = random.choice(musical_instruments)
    tool_profs.extend([mulmaster_aristocrat_artisan_tool, mulmaster_aristocrat_musical_instrument])
    equipment.extend([random.choice([mulmaster_aristocrat_artisan_tool, mulmaster_aristocrat_musical_instrument]), "Set of Fine Clothes", "10 gp"])
    
if background == "Noble":
    skill_profs.extend(["History", "Persuasion"])
    tool_profs.extend([random.choice(gaming_sets)])
    equipment.extend(["Set of Fine Clothes", "Signet Ring", "Scroll of Pedigree", "25 gp"])
    
if background == "Outlander":
    origin = random.choice(["Forester", "Trapper", "Homesteader", "Guide", "Exile", "Outcast", "Bounty Hunter", "Pilgrim", "Tribal Nomad", "Hunter-Gatherer", "Tribal Marauder"])
    background = "Outlander " + origin
    skill_profs.extend(["Athletics", "Survival"])
    tool_profs.extend([random.choice(musical_instruments)])
    equipment.extend(["Staff", "Hunting Trap", "Trophy from an Animal You Killed", "Set of Traveler's Clothes", "10 gp"])
    
if background == "Phlan Insurgent":
    skill_profs.extend(["Stealth", "Survival"])
    tool_profs.extend([random.choice(artisan_tools), "Land Vehicles"])
    equipment.extend(["Bag of 20 Caltrops", "Small Trinket from Your Home", "Healer's Kit", "Set of Dark Common Clothes", "5 gp"])

if background == "Phlan Refugee":
    skill_profs.extend(["Athletics", "Insight"])
    phlan_refugee_tool = random.choice(artisan_tools)
    tool_profs.extend([phlan_refugee_tool])
    equipment.extend([phlan_refugee_tool, "Token from Home", "Set of Traveler's Clothes", "15 gp"])
    
if background == "Sage":
    specialty = random.choice(["Alchemist", "Astronomer", "Discredited Academic", "Librarian", "Professor", "Researcher", "Wizard's Apprentice", "Scribe"])
    background = "Sage " + specialty
    skill_profs.extend(["Arcana", "History"])
    equipment.extend(["Bottle of Black Ink", "Quill", "Small Knife", "Letter from a Dead Colleague Posing a Question You Cannot yet Answer", "Set of Common Clothes", "10 gp"])
    
if background == "Sailor":
    skill_profs.extend(["Athletics", "Perception"])
    tool_profs.extend(["Navigator's Tools", "Water Vehicles"])
    equipment.extend(["Belaying Pin (Club)", "50 ft of Silk Rope", "Lucky Charm (Trinket)", "Set of Common Clothes", "10 gp"])
    
if background == "Secret Identity": # Has to be non human
    skill_profs.extend(["Deception", "Stealth"])
    tool_profs.extend(["Disguise Kit", "Forgery Kit"])
    equipment.extend(["Disguise Kit", "Forgery Kit", "Set of Common Clothes", "5 gp"])
    
if background == "Shade Fanatic":
    skill_profs.extend(["Deception", "Intimidation"])
    tool_profs.extend(["Forgery Kit"])
    equipment.extend(["Forgery Kit", "Transparent Cylinder of Shadow that has no Opening", "Signet Ring", "Set of Fine Clothes", "15 gp"])
    
if background == "Soldier":
    specialty = random.choice(["Officer", "Scout", "Infantry", "Cavalry", "Healer", "Quartermaster", "Standard Bearer", "Support Staff"])
    background = "Soldier " + specialty
    skill_profs.extend(["Athletics", "Intimidation"])
    tool_profs.extend([random.choice(gaming_sets), "Land Vehicles"])
    equipment.extend(["Insignia of Rank", "Trophy Taken from a Fallen Enemy", random.choice(["Bond Dice Set", "Playing Card Set"]), "Set of Common Clothes", "10 gp"])
    
if background == "Stojanow Prisoner":
    skill_profs.extend(["Deception", "Perception"])
    tool_profs.extend([random.choice(gaming_sets), "Thieves' Tools"])
    equipment.extend(["Small Knife", "Set of Common Clothes", "Trinket from Home", "10 gp"])
    
if background == "Ticklebelly Nomad":
    skill_profs.extend(["Animal Handling", "Nature"])
    tool_profs.extend(["Herbalism Kit"])
    equipment.extend(["Herbalism Kit", "Small Article of Jewelry Distinct to Your Tribe", "Hunting Trap", "Set of Common Clothes", "5 gp"])
    
if background == "Trade Sheriff":
    skill_profs.extend(["Investigation", "Persuasion"])
    tool_profs.extend(["Thieves' Tools"])
    equipment.extend(["Thieves' Kit", "Gray Cloak", "Sherrif's Insignia", "Set of Fine Clothes", "17 gp"])
    
if background == "Urban Bounty Hunter":
    skill_profs.extend(random.sample(["Deception", "Insight", "Persuasion", "Stealth"], 2))
    tool_profs.extend(random.sample([random.choice(gaming_sets), random.choice(musical_instruments), "Theives' Tools"],2))
    equipment.extend([random.choice(["Set of Common Clothes", "Set of Traveler's Clothes", "Set of Fine Clothes"]), "20 gp"])
    
if background == "Urchin":
    skill_profs.extend(["Sleight of Hand", "Stealth"])
    tool_profs.extend(["Disguise Kit", "Thieve's Tools"])
    equipment.extend(["Small Knife", "Map of Your Home City", "Pet Mouse", "Token to Remember Your Parents", "Set of Common Clothes", "10 gp"])
    
if background == "Uthgardt Tribe Member":
    skill_profs.extend(["Athletics", "Survival"])
    tool_profs.extend([random.choice([random.choice(artisan_tools), random.choice(musical_instruments)])])
    equipment.extend(["Hunting Trap", random.choice(["Totemic Token", "Set of Tattoos"]) + " Marking Your Loyalty to Uthgar", "Set of Traveler's Clothes", "10 gp"])
    
if background == "Vizier":
    skill_profs.extend(["History", "Religion"])
    vizier_artisan_tool = random.choice(artisan_tools)
    vizier_musical_instrument = random.choice(musical_instruments)
    tool_profs.extend([vizier_artisan_tool, vizier_musical_instrument])
    equipment.extend([random.choice([vizier_artisan_tool, vizier_musical_instrument]), "Scroll of Your God's Teachings", "Vizier's Cartouche", "Set of Fine Clothes", "25 gp"])
    
if background == "Waterdhavian Noble":
    skill_profs.extend(["History", "Persuasion"])
    tool_profs.extend([random.choice([random.choice(gaming_sets), random.choice(musical_instruments)])])
    equipment.extend(["Set of Fine Clothes", random.choice(["Signet Ring", "Brooch"]), "Scroll of Pedigree", "Skin of Fine " + random.choice(["Zzar", "Wine"]), "25 gp"])

alignment = ["Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral", "True Neutral", "Chaotic Neutral", "Lawful Evil", "Neutral Evil", "Chaotic Evil"]
alignment = random.choice(alignment)

skill_expertises = [item for item, count in collections.Counter(skill_profs).items() if count > 1] # I included this so if you get the same skill proficiency from two different sources, it becomes an expertise (it's pretty darn rare)
tool_expertises = [item for item, count in collections.Counter(tool_profs).items() if count > 1] # You can delete these two rows if you don't want innate expertises

print("Race:", race)
if subrace != "N/A":
    print("Subrace:", subrace)
print("Class:", character_class)
if subclass != "N/A":
    print("Sub-Class:", subclass)
if fighting_style != "N/A":
    print("Fighting Style:", fighting_style)
print("Level:", level)
print("Alignment:", alignment)
print("Background:", background)
print("STR ", attr_str, " STRMOD: ", str_mod)
print("DEX ", attr_dex, " DEXMOD: ", dex_mod)
print("CON ", attr_con, " CONMOD: ", con_mod)
print("INT ", attr_int, " INTMOD: ", int_mod)
print("WIS ", attr_wis, " WISMOD: ", wis_mod)
print("CHA ", attr_cha, " CHAMOD: ", cha_mod)
print("Hit Points: ", hp)
if race == "Dwarf":
    print("Speed:", speed, "Feet (Your Speed is not Reduced by Wearing Heavy Armour)")
else:
    print("Speed:", speed, "Feet")
if armour_profs != []:
    print("Armour Proficiencies:", ", ".join(sorted(remove_duplicates(armour_profs))))
if weapon_profs != []:
    print("Weapon Proficienceis:", ", ".join(sorted(remove_duplicates(weapon_profs))))
if tool_profs != []:
    print("Tool Proficiencies:", ", ".join(sorted(remove_duplicates(tool_profs))))
if tool_expertises != []:
    print ("Tool Expertises: ", ", ".join(sorted(remove_duplicates(tool_expertises))))
if saving_throw_profs != []:
    print("Saving Throw Proficiencies:", ", ".join(sorted(remove_duplicates(saving_throw_profs))))
if skill_profs != []:
    print("Skill Proficiencies:", ", ".join(sorted(remove_duplicates(skill_profs))))
if skill_expertises != []:
    print ("Skill Expertises: ", ", ".join(sorted(remove_duplicates(skill_expertises))))
if resistances != []:
    print("Resistances:", ", ".join(sorted(remove_duplicates(resistances))))
if immunities != []:
    print("Immunities:", ", ".join(sorted(remove_duplicates(immunities))))
if vulnerabilities != []:
    print("Vulnerabilities:", ", ".join(sorted(remove_duplicates(vulnerabilities))))
if traits != []:
    print("Traits:", ", ".join(sorted(remove_duplicates(traits))))
if equipment != []:
    print("Equipment and Weapons:", ", ".join(sorted(remove_duplicates(equipment))))
if age != "N/A":
    print("Age:", age, "Years")
else:
    print("Age: N/A")
print("Height: ", (height//12), "' ", height%12, '"', sep='')
print("Weight:", weight, "Pounds")
print("Eye Colour:", eyes)
print("Skin Colour:", skin)
print("Hair Colour:", hair)