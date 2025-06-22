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

import collections
from dataclasses import dataclass, replace
import enum
import random
from typing import Callable, Any

def normal(min:int, max:int) -> int: # Not exactly sure how this one is working, but it gives a more realistic result for age, height and weight
    r: int = round(random.triangular(low = min, high = max))# Round gives us a whole number for a character's age
    return r

def hitpoints(max_dice:int) -> int:
    n: int = 1
    hitpoints: int = 0
    
    if level == 1:
        hitpoints = max_dice + con_mod
        if hitpoints <= max_dice:  # This makes it so that the minimum HP is your HP die but you can start stronger if it "rolls well"
            hitpoints = max_dice
        return hitpoints
    else:
        hitpoints = max_dice + level * con_mod
        while n < level:
            hitpoints = hitpoints + random.randint(1, max_dice)
            n = n + 1
    if hitpoints <= max_dice + (level - 1):  # This makes it so the minimum HP increase is 1, I don't like to play with weakening characters
        hitpoints = max_dice + (level - 1)
    return hitpoints

def stat_increase(stat:int, num_increase:int) -> int:
    if stat <= 20 - num_increase:
        stat = stat + num_increase
    else:
        stat = 20
    return stat
        
def stat_decrease(stat:int, num_decrease:int) -> int:
    if stat >= 1 + num_decrease:
        stat = stat - num_decrease
    else:
        stat = 1
    return stat
        
def stat_mod(stat:int) -> int:
    return (stat - 10) // 2
    
def remove_duplicates(input:list[str]) -> list[str]:
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
martial_melee = ["Battleaxe", "Flail", "Glaive", "Greataxe", "Greatsword", "Halberd", "Lance", "Longsword", "Maul", "Morningstar", "Pike", "Rapier", "Scimitar", "Shortsword", "Trident", "War Pick", "Warhammer", "Whip"]
martial_ranged = ["Blowgun", "Hand Crossbow", "Heavy Crossbow", "Longbow", "Net"]
martial_weapons = martial_melee + martial_ranged
simple_melee = ["Club", "Dagger", "Greatclub", "Handaxe", "Javelin", "Light Hammer", "Mace", "Quarterstaff", "Sickle", "Spear"]
simple_ranged = ["Light Crossbow", "Dart", "Shortbow", "Sling"]
simple_weapons = simple_melee + simple_ranged

### COMMON DEFINITIONS ###

class DamageType(enum.StrEnum):
    BLUDGEONING = "Bludgeoning"
    PIERCING = "Piercing"
    SLASHING = "Slashing"
    ACID = "Acid"
    COLD = "Cold"
    FIRE = "Fire"
    FORCE = "Force"
    LIGHTNING = "Lightning"
    NECROTIC = "Necrotic"
    POISON = "Poison"
    PSYCHIC = "Psychic"
    RADIANT = "Radiant"
    THUNDER = "Thunder"

class ArmourTypes(enum.StrEnum):
    LIGHT = "Light Armour"
    MEDIUM = "Medium Armour"
    HEAVY = "Heavy Armour"
    SHIELD = "Shield"

class Weapons(enum.StrEnum):
    BATTLEAXE = "Battleaxe"
    BLOWGUN = "Blowgun"
    CLUB = "Club"
    DAGGER = "Dagger"
    DART = "Dart"
    FLAIL = "Flail"
    GLAIVE = "Glaive"
    GREATAXE = "Greataxe"
    GREATCLUB = "Greatclub"
    GREATSWORD = "Greatsword"
    HALBERD = "Halberd"
    HAND_CROSSBOW = "Hand Crossbow"
    HANDAXE = "Handaxe"
    HEAVY_CROSSBOW = "Heavy Crossbow"
    JAVELIN = "Javelin"
    LANCE = "Lance"
    LIGHT_CROSSBOW = "Light Crossbow"
    LIGHT_HAMMER = "Light Hammer"
    LONGBOW = "Longbow"
    LONGSWORD = "Longsword"
    MACE = "Mace"
    MAUL = "Maul"
    MORNINGSTAR = "Morningstar"
    NET = "Net"
    PIKE = "Pike"
    QUARTERSTAFF = "Quarterstaff"
    RAPIER = "Rapier"
    SCIMITAR = "Scimitar"
    SHORTBOW = "Shortbow"
    SHORTSWORD = "Shortsword"
    SICKLE = "Sickle"
    SLING = "Sling"
    SPEAR = "Spear"
    TRIDENT = "Trident"
    WAR_PICK = "War Pick"
    WARHAMMER = "Warhammer"
    WHIP = "Whip"

class Languages(enum.StrEnum):
    COMMON = "Common"
    DWARVISH = "Dwarvish"
    ELVISH = "Elvish"
    GIANT = "Giant"
    GNOMISH = "Gnomish"
    GOBLIN = "Goblin"
    HALFLING = "Halfling"
    ORC = "Orc"

class ExoticLanguages(enum.StrEnum):
    ABYSSAL = "Abyssal"
    CELESTIAL = "Celestial"
    DRACONIC = "Draconic"
    DEEP_SPEECH = "Deep Speech"
    INFERNAL = "Infernal"
    PRIMORDIAL = "Primordial"
    SYLVAN = "Sylvan"
    UNDERCOMMON = "Undercommon"

AllLanguages = Languages | ExoticLanguages

class Tools(enum.StrEnum): # TODO Check grammar on plural
    DISGUISE = "Disguise Kit"
    FORGERY = "Forgery Kit"
    HERBALIST = "Herbalism Kit"
    LAND_VEHICLES = "Land Vehicles"
    NAVIGATOR = "Navigator's Tools"
    THIEF = "Thieves' Tools"
    WATER_VEHICLES = "Water Vehicles"

class ArtisanTools(enum.StrEnum):
    ALCHEMIST = "Alchemist's Supplies"
    BREWER = "Brewer's Supplies"
    CALLIGRAPHER = "Calligrapher's Supplies"
    CARPENTER = "Carpenter's Tools"
    CARTOGRAPHER = "Cartographer's Tools"
    COBBLER = "Cobbler's Tools"
    COOK = "Cook's Utensils"
    GLASSBLOWER = "Glassblower's Tools"
    JEWELER = "Jeweler's Tools"
    LEATHERWORKER = "Leatherworker's Tools"
    MASON = "Mason's Tools"
    PAINTER = "Painter's Tools"
    POTTER = "Potter's Tools"
    SMITH = "Smith's Tools"
    TINKER = "Tinker's Tools"
    WEAVER = "Weaver's Tools"
    WOODCARVER = "Woodcarver's Tools"

class GamingSets(enum.StrEnum):
    DICE = "Dice Set"
    DRAGONCHESS = "Dragonchess Set"
    PLAYING_CARDS = "Playing Card Set"
    THREE_DRAGON_ANTE = "Three-Dragon Ante Set"

class MusicalInstruments(enum.StrEnum):
    BAGPIPES = "Bagpipes"
    DRUM = "Drum"
    DULCIMER = "Dulcimer"
    FLUTE = "Flute"
    LUTE = "Lute"
    LYRE = "Lyre"
    HORN = "Horn"
    PAN_FLUTE = "Pan Flute"
    SHAWM = "Shawm"
    VIOL = "Viol"

AllTools = Tools | ArtisanTools | GamingSets | MusicalInstruments

class WeaponTypes(enum.StrEnum):
    MARTIAL_WEAPONS = "Martial Weapons"
    SIMPLE_WEAPONS = "Simple Weapons"

class Sizes(enum.StrEnum):
    TINY = "Tiny"
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"
    HUGE = "Huge"
    GARGANTUAN = "Gargantuan"

class Attributes(enum.StrEnum):
    STR = "Strength"
    DEX = "Dexterity"
    CON = "Constitution"
    INT = "Intelligence"
    WIS = "Wisdom"
    CHA = "Charisma"

class Skills(enum.StrEnum):
    ACROBATICS = "Acrobatics"
    ANIMAL_HANDLING = "Animal Handling"
    ARCANA = "Arcana"
    ATHLETICS = "Athletics"
    DECEPTION = "Deception"
    HISTORY = "History"
    INSIGHT = "Insight"
    INTIMIDATION = "Intimidation"
    INVESTIGATION = "Investigation"
    MEDICINE = "Medicine"
    NATURE = "Nature"
    PERCEPTION = "Perception"
    PERFORMANCE = "Performance"
    PERSUASION = "Persuasion"
    RELIGION = "Religion"
    SLEIGHT_OF_HAND = "Sleight of Hand"
    STEALTH = "Stealth"
    SURVIVAL = "Survival"

class Trait(enum.StrEnum):
    ACID_BREATH = "Acid Breath Weapon (5x30 ft line)"
    LIGHTNING_BREATH = "Lightning Breath Weapon (5x30 ft line)"
    FIRE_BREATH_LINE = "Fire Breath Weapon (5x30 ft line)"
    FIRE_BREATH_CONE = "Fire Breath Weapon (15 ft cone)"
    POISON_BREATH = "Poison Breath Weapon (15 ft cone)"
    COLD_BREATH = "Cold Breath Weapon (15 ft cone)"
    ARTIFICERS_LORE = "Artificer's Lore"
    BRAVE = "Brave"
    CANTRIP = "Cantrip"
    DARKVISION60 = "Darkvision (60 ft)"
    DARKVISION120 = "Darkvision (120 ft)"
    DROW_MAGIC = "Drow Magic"
    DWARVEN_RESILIENCE = "Dwarven Resilience"
    FEY_ANCESTRY = "Fey Ancestry"
    GNOME_CUNNING = "Gnome Cunning"
    HALFLING_NIMBLENESS = "Halfling Nimbleness"
    INFERNAL_LEGACY = "Infernal Legacy"
    KEEN_SENSES = "Keen Senses"
    LUCKY = "Lucky"
    MASK_OF_THE_WILD = "Mask of the Wild"
    NATURAL_ILLUSIONIST = "Natural Illusionist"
    NATURALLY_STEALTHY = "Naturally Stealthy"
    RELENTLESS_ENDURANCE = "Relentless Endurance"
    SAVAGE_ATTACKS = "Savage Attacks"
    SPEAK_WITH_SMALL_BEASTS = "Speak with Small Beasts"
    STOUT_RESILIENCE = "Stout Resilience"
    SUNLIGHT_SENSITIVITY = "Sunlight Sensitivity"
    TINKER = "Tinker"
    FEAT = "Feat"
    TRANCE = "Trance"

class BackgroundTrait(enum.StrEnum):
    BY_POPULAR_DEMAND = "By Popular Demand"
    BAD_REPUTATION = "Bad Reputation"
    CITY_SECRETS = "City Secrets"
    CRIMINAL_CONTACT = "Criminal Contact"
    FALSE_IDENTITY = "False Identity"
    GUILD_MEMBERSHIP = "Guild Membership"
    MILITARY_RANK = "Military Rank"
    POSITION_OF_PRIVILEGE = "Position of Privilege"
    RESEARCHER = "Researcher"
    RETAINERS = "Retainers"
    RUSTIC_HOSPITALITY = "Rustic Hospitality"
    SHELTER_OF_THE_FAITHFUL = "Shelter of the Faithful"
    SHIPS_PASSAGE = "Ship's Passage"
    WANDERER = "Wanderer"

AllTraits = Trait | BackgroundTrait

### RACE DEFINITIONS ###

class RaceName(enum.StrEnum):
    DRAGONBORN = "Dragonborn"
    DWARF = "Dwarf"
    ELF = "Elf"
    GNOME = "Gnome"
    HALFLING = "Halfling"
    HALF_ELF = "Half-Elf"
    HALF_ORC = "Half-Orc"
    HUMAN = "Human"
    TIEFLING = "Tiefling"
    
RaceAttributes = int | list[str | Trait | DamageType | tuple[Attributes, int] | Skills] | tuple[int, int]

class Race:
    name: RaceName
    subraces: list[Any]
    stat_increases: list[tuple[Attributes, int]] = []
    age_range: tuple[int, int]
    size_mod_range: tuple[int, int]
    base_height: int
    base_weight: int
    weight_range: tuple[int, int]
    speed: int
    size: Sizes
    eyes: list[str]
    skin: list[str]
    hair: list[str]
    traits: list[Trait] = []
    resistances: list[DamageType] = []
    immunities: list[DamageType] = []
    vulnerabilities: list[DamageType] = []
    skill_proficiencies: list[Skills] = []
    possible_skill_profs: list[Skills] = []
    skill_prof_count: int
    tool_proficiencies: list[AllTools] = []
    weapon_proficiencies: list[Weapons | WeaponTypes] = []
    languages: list[AllLanguages] = []
    possible_languages: list[AllLanguages] = []
    language_count: int

    def apply_subrace(self, subrace: Any):
        pass
'''
class (Race):
    name = RaceName.
    class Subrace(enum.StrEnum):
        
    subraces = list(Subrace)
    stat_increases = [
        (Attributes., 2),
        (Attributes., 1)
    ]
    age_range = ()
    size_mod_range = ()
    base_height = 
    base_weight = 
    weight_range = ()
    speed = 30
    size = Sizes.
    eyes = []
    skin = []
    hair = []
    traits = [Trait.]
    resistances = []
    immunities = []
    vulnerabilities = []
    skill_proficiencies = []
    possible_skill_profs = []
    skill_prof_count = 0
    weapon_proficiencies = []
    languages = []
    possible_languages = []
    language_count = 0
    
    def apply_subrace(self, subrace: Any):
        if subrace == :
            self.
'''

class Dragonborn(Race):
    name = RaceName.DRAGONBORN
    # subraces = ["Red", "Green", "Blue", "White", "Black", "Gold", "Silver", "Brass", "Copper", "Bronze"]
    class Subrace(enum.StrEnum):
        RED = "Red"
        GREEN = "Green"
        BLUE = "Blue"
        WHITE = "White"
        BLACK = "Black"
        GOLD = "Gold"
        SILVER = "Silver"
        BRASS = "Brass"
        COPPER = "Copper"
        BRONZE = "Bronze"
    subraces = list(Subrace)
    stat_increases = [
        (Attributes.STR, 2),
        (Attributes.CHA, 1)
    ]
    age_range = (15, 60)
    size_mod_range = (2, 16)
    base_height = 5 * 12 + 6
    base_weight = 175
    weight_range = (2, 12)
    speed = 30
    size = Sizes.MEDIUM
    eyes = ["Red", "Gold"]
    languages = [Languages.COMMON, ExoticLanguages.DRACONIC]
    
    def apply_subrace(self, subrace: Any):
        self.skin = [f"{subrace} Scales"]
        if subrace == Dragonborn.Subrace.RED:
            self.resistances.append(DamageType.FIRE)
            self.traits.append(Trait.FIRE_BREATH_CONE)
        elif subrace == Dragonborn.Subrace.GREEN:
            self.resistances.append(DamageType.POISON)
            self.traits.append(Trait.POISON_BREATH)
        elif subrace == Dragonborn.Subrace.BLUE:
            self.resistances.append(DamageType.LIGHTNING)
            self.traits.append(Trait.LIGHTNING_BREATH)
        elif subrace == Dragonborn.Subrace.WHITE:
            self.resistances.append(DamageType.COLD)
            self.traits.append(Trait.COLD_BREATH)
        elif subrace == Dragonborn.Subrace.BLACK:
            self.resistances.append(DamageType.ACID)
            self.traits.append(Trait.ACID_BREATH)
        elif subrace == Dragonborn.Subrace.GOLD:
            self.resistances.append(DamageType.FIRE)
            self.traits.append(Trait.FIRE_BREATH_CONE)
        elif subrace == Dragonborn.Subrace.BRASS:
            self.resistances.append(DamageType.FIRE)
            self.traits.append(Trait.FIRE_BREATH_LINE)
        elif subrace == Dragonborn.Subrace.COPPER:
            self.resistances.append(DamageType.ACID)
            self.traits.append(Trait.ACID_BREATH)
        elif subrace == Dragonborn.Subrace.BRONZE:
            self.resistances.append(DamageType.FIRE)
            self.traits.append(Trait.FIRE_BREATH_LINE)

class Dwarf(Race):
    name = RaceName.DWARF
    class Subrace(enum.StrEnum):
        HILL = "Hill"
        MOUNTAIN = "Mountain"
    subraces = list(Subrace)
    stat_increases = [
        (Attributes.CON, 2)
    ]
    age_range = (20, 320)
    size_mod_range = (2, 8)
    base_height = 3 * 12 + 8
    base_weight = 115
    weight_range = (2, 12)
    speed = 25
    size = Sizes.MEDIUM
    eyes = ["Brown", "Hazel", "Green"]
    skin = ["White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown",\
            "Dark Brown", "Very Dark Brown/Black"]
    hair = ["Bald", "Brown", "Black", "Blond", "Red"]
    traits = [Trait.DWARVEN_RESILIENCE, Trait.DARKVISION60]
    resistances = [DamageType.POISON]
    
    def apply_subrace(self, subrace: Any):
        if subrace == Dwarf.Subrace.HILL:
            self.stat_increases.append((Attributes.WIS, 1))
            self.base_height = 3 * 12 + 8
            self.base_weight = 115
            # TODO add a hill dwarf check to the character for max hp (+1 per level)
        if subrace == Dwarf.Subrace.MOUNTAIN:
            self.stat_increases.append((Attributes.STR, 2))
            self.base_height = 4 * 12
            self.base_weight = 130

class Elf(Race):
    name = RaceName.ELF
    class Subrace(enum.StrEnum):
        DROW = "Drow"
        HIGH = "High"
        WOOD = "Wood"
    subraces = list(Subrace)
    stat_increases = [
        (Attributes.DEX, 2),
    ]
    age_range = (20, 700) # Sizing in subrace
    speed = 30
    size = Sizes.MEDIUM
    eyes = ["Blue", "Violet", "Green"]
    skin = ["Lightly Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown"]
    hair = ["Dark Brown", "Autumn Orange", "Mossy Green", "Deep Gold"]
    traits = [Trait.DARKVISION60, Trait.KEEN_SENSES, Trait.FEY_ANCESTRY, Trait.TRANCE]
    languages = [Languages.COMMON, Languages.ELVISH]
    
    def apply_subrace(self, subrace: Any):
        if subrace == Elf.Subrace.DROW:
            self.stat_increases.append((Attributes.CHA, 1))
            self.traits.remove(Trait.DARKVISION60)
            self.traits.extend([Trait.DARKVISION120, Trait.DROW_MAGIC, Trait.SUNLIGHT_SENSITIVITY])
            self.weapon_proficiencies.extend([Weapons.RAPIER, Weapons.SHORTSWORD, Weapons.HAND_CROSSBOW])
            self.size_mod_range = (2, 12)
            self.base_height = 4 * 12 + 5
            self.base_weight = 75
            self.weight_range = (1, 6)
        elif subrace == Elf.Subrace.HIGH:
            self.stat_increases.append((Attributes.INT, 1))
            self.traits.extend([Trait.CANTRIP])
            self.weapon_proficiencies.extend([Weapons.LONGSWORD, Weapons.SHORTSWORD, Weapons.SHORTBOW, Weapons.LONGBOW])
            self.possible_languages = list(Languages)
            self.language_count = 1
            self.size_mod_range = (2, 20)
            self.base_height = 4 * 12 + 6
            self.base_weight = 90
            self.weight_range = (1, 4)
        elif subrace == Elf.Subrace.WOOD:
            self.stat_increases.append((Attributes.WIS, 1))
            self.traits.extend([Trait.MASK_OF_THE_WILD])
            self.weapon_proficiencies.extend([Weapons.LONGSWORD, Weapons.SHORTSWORD, Weapons.SHORTBOW, Weapons.LONGBOW])
            self.speed = 35
            self.size_mod_range = (2, 20)
            self.base_height = 4 * 12 + 6
            self.base_weight = 100
            self.weight_range = (1, 4)

class Gnome(Race):
    name = RaceName.GNOME
    class Subrace(enum.StrEnum):
        FOREST = "Forest"
        ROCK = "Rock"
    subraces = list(Subrace)
    stat_increases = [
        (Attributes.INT, 2)
    ]
    age_range = (20, 400)
    size_mod_range = (2, 8)
    base_height = 2 * 12 + 11
    base_weight = 35
    weight_range = (1, 1)
    speed = 25
    size = Sizes.SMALL
    eyes = ["Glittering Opaque Black", "Glittering Opaque Blue"]
    skin = ["Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black", "Rocky Gray"]
    hair = ["Red", "Black", "Grey", "Dark Brown", "Brown", "Dirty Blonde", "Blonde", "White"]
    traits = [Trait.DARKVISION60, Trait.GNOME_CUNNING]
    languages = [Languages.COMMON, Languages.GNOMISH]
    
    def apply_subrace(self, subrace: Any):
        if subrace == Gnome.Subrace.FOREST:
            self.stat_increases.append((Attributes.DEX, 1))
            self.traits.extend([Trait.NATURAL_ILLUSIONIST, Trait.SPEAK_WITH_SMALL_BEASTS])
        elif subrace == Gnome.Subrace.ROCK:
            self.stat_increases.append((Attributes.CON, 1))
            self.traits.extend([Trait.ARTIFICERS_LORE, Trait.TINKER])
            self.tool_proficiencies.append(ArtisanTools.TINKER)

class HalfElf(Race):
    name = RaceName.HALF_ELF
    class Subrace(enum.StrEnum):
        DROW = "Drow"
        HIGH = "High"
        WOOD = "Wood"
    subraces = list(Subrace)
    stat_increases = [
        (Attributes.CHA, 2) # TODO "Any other two stats increase by 1"
    ]
    age_range = (20, 160)
    size_mod_range = (2, 16)
    base_height = 4 * 12 + 9
    base_weight = 110
    weight_range = (2, 8)
    speed = 30
    size = Sizes.MEDIUM
    eyes = ["Blue", "Violet", "Green"]
    skin = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown"]
    hair = ["Red", "Blond", "Brown", "Black"]
    traits = [Trait.DARKVISION60, Trait.FEY_ANCESTRY]
    possible_skill_profs = list(Skills)
    skill_prof_count = 2
    languages = [Languages.COMMON, Languages.ELVISH]
    possible_languages = list(Languages)
    language_count = 1

class Halfling(Race):
    name = RaceName.HALFLING
    class Subrace(enum.StrEnum):
        LIGHTFOOT = "Lightfoot"
        STOUT = "Stout"
    subraces = list(Subrace)
    stat_increases = [
        (Attributes.DEX, 2)
    ]
    age_range = (20, 200)
    size_mod_range = (2, 8)
    base_height = 2 * 12 + 7
    base_weight = 35
    weight_range = (1, 1)
    speed = 25
    size = Sizes.SMALL
    eyes = ["Brown"]
    skin = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black"]
    hair = ["Aubrun", "Black", "Brown", "Gray"]
    traits = [Trait.BRAVE, Trait.HALFLING_NIMBLENESS, Trait.LUCKY]
    languages = [Languages.COMMON, Languages.HALFLING]
    
    def apply_subrace(self, subrace: Any):
        if subrace == Halfling.Subrace.LIGHTFOOT:
            self.stat_increases.append((Attributes.CHA, 1))
            self.traits.append(Trait.NATURALLY_STEALTHY)
        elif subrace == Halfling.Subrace.STOUT:
            self.stat_increases.append((Attributes.CON, 1))
            self.traits.append(Trait.STOUT_RESILIENCE)
            self.resistances.append(DamageType.POISON)

class HalfOrc(Race):
    name = RaceName.HALF_ORC
    stat_increases = [
        (Attributes.STR, 2),
        (Attributes.CON, 1)
    ]
    age_range = (14, 60)
    size_mod_range = (2, 20)
    base_height = 4 * 12 + 10
    base_weight = 140
    weight_range = (2, 12)
    speed = 30
    size = Sizes.MEDIUM
    eyes = ["Reddish Brown", "Reddish Blue", "Reddish Green", "Reddish Grey"]
    skin = ["Greyish Green"]
    hair = ["Dark Brown", "Bald", "Red"]
    traits = [Trait.DARKVISION60, Trait.RELENTLESS_ENDURANCE, Trait.SAVAGE_ATTACKS]
    skill_proficiencies = [Skills.INTIMIDATION]
    languages = [Languages.COMMON, Languages.ORC]

class Human(Race):
    name = RaceName.HUMAN
    class Subrace(enum.StrEnum):
        NORMAL = "Normal"
        VARIANT = "Variant"
    subraces = list(Subrace)
    age_range = (20, 60)
    size_mod_range = (2, 20)
    base_height = 4 * 12 + 8
    base_weight = 110
    weight_range = (2, 8)
    speed = 30
    size = Sizes.MEDIUM
    eyes = ["Brown", "Hazel", "Blue", "Green", "Grey", "Amber"]
    skin = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black"]
    hair = ["Black", "Brown", "Blonde", "Red", "White"]
    languages = [Languages.COMMON]
    possible_languages = list(Languages)
    language_count = 1
    
    def apply_subrace(self, subrace: Any):
        if subrace == Human.Subrace.NORMAL:
            self.stat_increases.extend(
                (Attributes.STR, 1),
                (Attributes.DEX, 1),
                (Attributes.CON, 1),
                (Attributes.INT, 1),
                (Attributes.WIS, 1),
                (Attributes.CHA, 1)
            )
        elif subrace == Human.Subrace.VARIANT:
            # TODO two random Attributes increase by 1
            self.possible_skill_profs = list(Skills)
            self.skill_prof_count = 1
            self.traits.append(Trait.FEAT)

class Tiefling(Race):
    name = RaceName.TIEFLING
    stat_increases = [
        (Attributes.CHA, 2),
        (Attributes.INT, 1)
    ]
    age_range = (20, 60)
    size_mod_range = (2, 16)
    base_height = 4 * 12 + 9
    base_weight = 110
    weight_range = (2, 8)
    speed = 30
    size = Sizes.MEDIUM
    eyes = ["Solid Orbs of Red", "Solid Orbs of Black", "Solid Orbs of White", "Solid Orbs of Silver", "Solid Orbs of Gold"]
    skin = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black", "Light Red", "Maroon", "Burgundy", "Dark Red", "Red"]
    hair = ["Red", "Brown", "Black", "Dark Blue", "Purple"]
    traits = [Trait.DARKVISION60, Trait.INFERNAL_LEGACY]
    resistances = [DamageType.FIRE]
    languages = [Languages.COMMON, ExoticLanguages.INFERNAL]
  
str_mod = stat_mod(attr_str)
dex_mod = stat_mod(attr_dex)
con_mod = stat_mod(attr_con)
int_mod = stat_mod(attr_int)
wis_mod = stat_mod(attr_wis)
cha_mod = stat_mod(attr_cha)


class CharacterClass:
    # TODO traits in class specifics, many bits are level gaited. Example commented into Barbarian
    armour_profs: list[ArmourTypes] = []
    equipment: list[str] = []
    saving_throw_profs: list[Attributes] = []
    subclasses: list[str] = []
    available_skill_profs: list[Skills] = []
    tool_profs: list[AllTools] = []
    weapon_profs: list[WeaponTypes | Weapons] = []

    hit_die = 0
    skill_prof_count = 1

    def __init__(self):
        pass

    def define_subclass(self):
        self.subclass = random.choice(self.subclasses or ["None"])

class FightingClass(CharacterClass):
    fighting_styles: list[str] = []
    
    def define_fighting_style(self):
        self.fighting_style = random.choice(self.fighting_styles)

### CLASS DEFINITIONS ###

class Barbarian(CharacterClass):
    hit_die = 12
    # Subclass at Level 3, officially called "Primal Path"
    # Base Rules = Berserker, Totem Warior
    # The rest are official, but paywalled
    subclasses = ["Path of the Ancestral Guardian", "Path of the Battlerager", "Path of the Beast", "Path of the Berserker", "Path of the Giant", "Path of the Storm Herald", "Path of the Totem Warrior", "Path of Wild Magic", "Path of the Zealot"]
    armour_profs = [ArmourTypes.LIGHT, ArmourTypes.MEDIUM, ArmourTypes.SHIELD]
    weapon_profs = list(WeaponTypes)
    saving_throw_profs = [Attributes.STR, Attributes.CON]
    available_skill_profs = [Skills.ANIMAL_HANDLING, Skills.ATHLETICS, Skills.INTIMIDATION, Skills.NATURE, Skills.PERCEPTION, Skills.SURVIVAL]
    skill_prof_count = 2
    # TRAITS = [(NAME, LEVEL OF UNLOCK, SOURCE=base class)] #Note the Primal Path Traits depend on subclass
    # traits = [("Rage", 1), ("Unarmoured Defense", 1), ("Danger Sense", 2), ("Reckless Attack", 2), ("Primal Path Trait I", 3, subclass), ("Primal Knowledge", 3), ("Extra Attack", 5), ("Fast Movement", 5), ("Feral Instinct", 7),
    #           ("Primal Path Trait II", 6, subclass), ("Brutal Critical", 9), ("Primal Path Trait III", 10, subclass), ("Relentless Rage", 11), ("Primal Path Trait IV", 14, subclass), ("Persistent Rage", 15), ("Indomitable Might", 18),
    #           ("Primal Champion", 20)]
    # TODO: equipment from [random.choice(["Greataxe", random.choice(martial_melee)]), random.choice(["Two Handaxes", random.choice(simple_weapons)]), "Explorer's Pack", "Four Javelins"]

class Bard(CharacterClass): #subclass lvl 3
    hit_die = 8
    # Subclass at Level 3, officially called "Bard College"
    # Base Rules = Lore, Valor
    subclasses = ["College of Creation", "College of Eloquence", "College of Glamour", "College of Lore", "College of Spirits", "College of Swords", "College of Valor", "College of Whispers"]
    armour_profs = [ArmourTypes.LIGHT]
    weapon_profs = [WeaponTypes.SIMPLE_WEAPONS, Weapons.HAND_CROSSBOW, Weapons.LONGSWORD, Weapons.RAPIER, Weapons.SHORTSWORD]
    saving_throw_profs = [Attributes.DEX, Attributes.CHA]
    available_skill_profs = list(Skills)
    skill_prof_count = 3
    # TODO: Equipment from [random.choice(["Rapier", "Longsword", random.choice(simple_weapons)]), random.choice(["Diplomat's Pack", "Entertainer's Pack"]), random.choice(["Lute", random.choice(musical_instruments)]), "Leather Armour", "Dagger"]
    def __init__(self):
        super().__init__()
        self.tool_profs = [random.sample(list(MusicalInstruments), 3)]
    
class Cleric(CharacterClass): #TODO NOT DONE
    hit_die = 8
    # Subclass at Level 1, officially called "Divine Domain"
    # Base Rules = Knowledge, Life, Light, Nature, Tempest, Trickery, War
    subclasses = ["Arcana Domain", "Death Domain", "Forge Domain", "Grave Domain", "Knowledge Domain", "Life Domain", "Light Domain", "Nature Domain", "Order Domain", "Peace Domain", "Tempest Domain", "Trickery Domain", "Twilight Domain", "War Domain"]
    armour_profs = [ArmourTypes.LIGHT, ArmourTypes.MEDIUM, ArmourTypes.SHIELD]
    weapon_profs = [WeaponTypes.SIMPLE_WEAPONS]
    saving_throw_profs = [Attributes.WIS, Attributes.CHA]
    available_skill_profs = [Skills.HISTORY, Skills.INSIGHT, Skills.MEDICINE, Skills.PERSUASION, Skills.RELIGION]
    skill_prof_count = 2
    # TODO Figure out the below legacy bits, including equipment
    # if "Warhammer" in weapon_profs or "Martial Weapons" in weapon_profs:
    #     equipment.extend([random.choice(["Mace", "Warhammer"])])
    # else:
    #     equipment.extend(["Mace"])
    # if "Chain Mail" in armour_profs or "Heavy Armour" in armour_profs:
    #     equipment.extend([random.choice(["Scale Mail", "Leather Armour", "Chain Mail"])])
    # else:
    #     equipment.extend([random.choice(["Scale Mail", "Leather Armour"])])
    #equipment.extend([random.choice(["Light Crossbow with 20 Bolts", random.choice(simple_weapons)]), random.choice(["Priest's Pack", "Explorer's Pack"]), "Shield", "Holy Symbol"])
    
class Druid(CharacterClass):
    hit_die = 8
    # Subclass at Level 2, officially called "Druid Circle"
    # Base Rules = Land, Moon
    subclasses = ["Circle of Dreams", "Circle of the Land", "Circle of the Moon", "Circle of the Shepherd", "Circle of Spores", "Circle of Stars", "Circle of Wildfire"]
    armour_profs = [ArmourTypes.LIGHT, ArmourTypes.MEDIUM, ArmourTypes.SHIELD]
    weapon_profs = [Weapons.CLUB, Weapons.DAGGER, Weapons.DART, Weapons.JAVELIN, Weapons.MACE, Weapons.QUARTERSTAFF, Weapons.SCIMITAR, Weapons.SICKLE, Weapons.SLING, Weapons.SPEAR]
    tool_profs = [Tools.HERBALIST]
    saving_throw_profs = [Attributes.INT, Attributes.WIS]
    available_skill_profs = [Skills.ANIMAL_HANDLING, Skills.ARCANA, Skills.INSIGHT, Skills.MEDICINE, Skills.NATURE, Skills.PERCEPTION, Skills.RELIGION, Skills.SURVIVAL]
    skill_prof_count = 2
    equipment = [] # mega TODO from [random.choice(["Wooden Shield", random.choice(simple_weapons)]), random.choice(["Scimitar", random.choice(simple_melee)]), "Leather Armour", "Explorer's Pack", "Druidic Focus"]
    def __init__(self):
        super().__init__()

    def define_subclass(self):
        super().define_subclass()
        if self.subclass == "Circle of the Land":
            land = random.choice(["(Arctic)", "(Coast)", "(Desert)", "(Forest)", "(Grassland)", "(Mountain)", "(Swamp)", "(Underdark)"])
            self.subclass = "Circle of the Land " + land
    
class Fighter(FightingClass):
    hit_die = 10
    # Base Rules = Archery, Defense, Dueling, Great Weapon Fighting, Protection, Two-Weapon Fighting
    fighting_styles = ["Archery", "Blind Fighting", "Defense", "Dueling", "Great Weapon Fighting", "Interception", "Protection", "Superior Technique", "Thrown Weapon Fighting", "Two-Weapon Fighting", "Unarmed Fighting"]
    # Sublass at Level 3, officially called "Martial Archetype"
    # Base Rules = Battle Master, Champion, Eldritch Knight
    subclasses = ["Arcane Archer", "Banneret", "Battle Master", "Cavalier", "Champion", "Echo Knight", "Eldritch Knight", "Psi Warrior", "Rune Knight", "Samurai"]
    armour_profs = list(ArmourTypes)
    weapon_profs = list(WeaponTypes)
    saving_throw_profs = [Attributes.STR, Attributes.CON]
    available_skill_profs = [Skills.ACROBATICS, Skills.ANIMAL_HANDLING, Skills.ATHLETICS, Skills.HISTORY, Skills.INSIGHT, Skills.INTIMIDATION, Skills.PERCEPTION, Skills.SURVIVAL]
    skill_prof_count = 2
    equipment = [] # mega TODO
    # EqptExtnd = [random.choice(["Light Crossbow with 20 Bolts", "Two Handaxes"]), random.choice(["Dungeoneer's Pack", "Explorer's Pack"])]
    # EqptExtnd.extend(random.choice([["Chain Mail"], ["Leather Armour", "Longbow with 20 Arrows"]]))
    # EqptExtnd.extend(random.choice([[random.choice(martial_weapons), "Shield"], random.sample(martial_weapons, 2)]))
    # equipment.extend(EqptExtnd)

class Monk(CharacterClass):
    hit_die = 8
    # Subclass at Level 3, officially called "Monastic Tradition"
    # Base Rules = Four Elements, Open Hand, Shadow
    subclasses = ["Way of the Astral Self", "Way of the Ascendant Dragon", "Way of the Drunken Master", "Way of the Four Elements", "Way of the Kensei", "Way of the Long Death", "Way of Mercy", "Way of the Open Hand", "Way of Shadow", "Way of the Sun Soul"]
    weapon_profs = [WeaponTypes.SIMPLE_WEAPONS, Weapons.SHORTSWORD]
    saving_throw_profs = [Attributes.STR, Attributes.DEX]
    available_skill_profs = [Skills.ACROBATICS, Skills.ATHLETICS, Skills.HISTORY, Skills.INSIGHT, Skills.RELIGION, Skills.STEALTH]
    skill_prof_count = 2
    equipment = [] # mega TODO from [random.choice(["Shortsword", random.choice(simple_weapons)]), random.choice(["Dungeoneer's Pack", "Explorer's Pack"]), "10 Darts"]

    def __init__(self):
        super().__init__()
        self.tool_profs = [random.choice(list(MusicalInstruments) + list(Tools))]
    
class Paladin(FightingClass):
    hit_die = 10
    # Fighting Style at Level 2
    # Base Rules = Defense, Dueling, Great Weapon Fighting, Protection
    fighting_style = ["Blessed Warrior", "Blind Fighting", "Defense", "Dueling", "Great Weapon Fighting", "Interception", "Protection"]
    # Subclass at Level 3, officially called "Sacred Oath"
    # Base Rules = Ancients, Devotion, Vengeance
    subclasses = ["Oath of the Ancients", "Oath of Conquest", "Oath of the Crown", "Oath of Devotion", "Oath of Glory", "Oath of Redemption", "Oath of Vengeance", "Oath of the Watchers", "Oathbreaker"]
    armour_profs = list(ArmourTypes)
    weapon_profs = list(WeaponTypes)
    saving_throw_profs = [Attributes.WIS, Attributes.CHA]
    available_skill_profs = [Skills.ATHLETICS, Skills.INSIGHT, Skills.INTIMIDATION, Skills.MEDICINE, Skills.PERSUASION, Skills.RELIGION]
    skill_prof_count = 2
    equipment = [] # mega TODO
    # EqptExtnd = random.choice([[random.choice(martial_weapons), "Shield"], random.sample(martial_weapons, 2)])
    # EqptExtnd.extend([random.choice(["5 Javelins", random.choice(simple_melee)])])
    # EqptExtnd.extend(["Chain Mail", "Holy Symbol"])
    # equipment.extend(EqptExtnd)

class Ranger(FightingClass):
    hit_die = 10
    # Fighting Style at Level 2
    # Base Rules = Archery, Defense, Dueling, Two-Weapon Fighting
    fighting_style = ["Archery", "Blind Fighting", "Defense", "Druidic Warrior", "Dueling", "Thrown Weapon Fighting", "Two-Weapon Fighting"]
    # Subclass at Level 3, officially called "Ranger Conclave"
    # Base Rules = Beast Master, Hunter
    subclasses = ["Beast Master", "Fey Wanderer", "Gloom Stalker", "Horizon Walker", "Hunter", "Monster Slayer", "Swarmkeeper", "Drakewarden"]
    armour_profs = [ArmourTypes.LIGHT, ArmourTypes.MEDIUM, ArmourTypes.SHIELD]
    weapon_profs = list(WeaponTypes)
    saving_throw_profs = [Attributes.STR, Attributes.DEX]
    available_skill_profs = [Skills.ANIMAL_HANDLING, Skills.ATHLETICS, Skills.INSIGHT, Skills.INVESTIGATION, Skills.NATURE, Skills.PERCEPTION, Skills.STEALTH, Skills.SURVIVAL]
    skill_prof_count = 3
    equipment = [] # mega TODO
    # EqptExtnd =[random.choice(["Scale Mail", "Leather Armour"])]
    # EqptExtnd.extend(random.choice([["Two Shortswords"], random.sample(simple_melee, 2)]))
    # EqptExtnd.extend([random.choice(["Dungeoneer's Pack", "Explorer's Pack"])])
    # EqptExtnd.extend(["Longbow with 20 Arrows"])
    # equipment.extend(EqptExtnd)

class Rogue(CharacterClass):
    hit_die = 8
    # Subclass at Level 3, officially called "Roguish Archtype"
    # Base Rules = Arcane Trickster, Assassin, Thief
    subclasses = ["Arcane Trickster", "Assassin", "Inquisitive", "Mastermind", "Phantom", "Scout", "Soulknife", "Swashbuckler", "Thief"]
    armour_profs = [ArmourTypes.LIGHT]
    weapon_profs = [WeaponTypes.SIMPLE_WEAPONS, Weapons.HAND_CROSSBOW, Weapons.LONGSWORD, Weapons.RAPIER, Weapons.SHORTSWORD]
    tool_profs = [Tools.THIEF]
    saving_throw_profs = [Attributes.DEX, Attributes.INT]
    available_skill_profs = [Skills.ACROBATICS, Skills.ATHLETICS, Skills.DECEPTION, Skills.INSIGHT, Skills.INTIMIDATION, Skills.INVESTIGATION, Skills.PERCEPTION, Skills.PERFORMANCE, Skills.PERSUASION, Skills.SLEIGHT_OF_HAND, Skills.STEALTH]
    skill_prof_count = 4
    equipment = [] # mega TODO [random.choice(["Rapier", "Shortsword"]), random.choice(["Shortbow with 20 Arrows", "Shortsword"]), random.choice(["Burglar's Pack", "Dungeoneer's Pack", "Explorer's Pack"]), "Leather Armour", "Two Daggers", "Thieves's Tools"]

class Sorcerer(CharacterClass):
    hit_die = 6
    # Subclass at Level 1, officially called "Sorcerous Origin"
    # Base Rules = Draconic Bloodline, Wild Magic
    subclasses = ["Aberrant Mind", "Clockwork Soul", "Divine Soul", "Draconic Bloodline", "Lunar Sorcery", "Shadow Magic", "Storm Sorcery", "Wild Magic"]
    weapon_profs = [Weapons.DAGGER, Weapons.DART, Weapons.SLING, Weapons.QUARTERSTAFF, Weapons.LIGHT_CROSSBOW]
    saving_throw_profs = [Attributes.CON, Attributes.CHA]
    available_skill_profs = [Skills.ARCANA, Skills.DECEPTION, Skills.INSIGHT, Skills.INTIMIDATION, Skills.PERSUASION, Skills.RELIGION]
    available_skill_profs = 2
    equipment = [] # mega TODO [random.choice(["Light Crossbow with 20 Bolts", random.choice(simple_weapons)]), random.choice(["Component Pouch", "Arcane Focus"]), random.choice(["Dungeoneer's Pack", "Explorer's Pack"]), "Two Daggers"]
    
class Warlock(FightingClass):
    hit_die = 8
    # Subclass at Level 1, officially called "Otherworldly Patron"
    # Base Rules = Archfey, Fiend, Great Old One
    subclasses = ["The Archfey", "The Celestial", "The Fathomless", "The Fiend", "The Genie", "The Great Old One", "The Hexblade", "The Undead", "The Undying"]
    # Fighting Style at Level 3, officially called "Pact Boon"
    fighting_styles = ["Pact of the Blade", "Pact of the Chain", "Pact of the Tome", "Pact of the Talisman"]
    armour_profs = [ArmourTypes.LIGHT]
    weapon_profs = [WeaponTypes.SIMPLE_WEAPONS]
    saving_throw_profs = [Attributes.WIS, Attributes.CHA]
    available_skill_profs = [Skills.ARCANA, Skills.DECEPTION, Skills.HISTORY, Skills.INTIMIDATION, Skills.INVESTIGATION, Skills.NATURE, Skills.RELIGION]
    equipment = [] # mega TODO [random.choice(["Light Crossbow with 20 Bolts", random.choice(simple_weapons)]), random.choice(["Component Pouch", "Arcane Focus"]), random.choice(["Scholar's Pack", "Dungeoneer's Pack"]), "Leather Armour", random.choice(simple_weapons), "Two Daggers"]

class Wizard(CharacterClass):
    hit_die = 6
    # Sublass at Level 2, officially called "Arcane Tradition"
    # Base Rules = Abjuration, Conjuration, Divination, Enchantment, Evocation, Illusion, Necromancy, Transmutation
    subclasses = ["Abjuration", "Bladesinging", "Chronurgy", "Conjuration", "Divination", "Enchantment", "Evocation", "Graviturgy", "Illusion", "Necromancy", "Order of Scribes", "Transmutation", "War Magic"]
    weapon_profs = [Weapons.DAGGER, Weapons.DART, Weapons.SLING, Weapons.QUARTERSTAFF, Weapons.LIGHT_CROSSBOW]
    saving_throw_profs = [Attributes.INT, Attributes.WIS]
    available_skill_profs = [Skills.ARCANA, Skills.HISTORY, Skills.INSIGHT, Skills.INVESTIGATION, Skills.MEDICINE, Skills.RELIGION]
    skill_prof_count = 2
    equipment = [] # mega TODO [random.choice(["Quarterstaff", "Dagger"]), random.choice(["Component Pouch", "Arcane Focus"]), random.choice(["Scholar's Pack", "Explorer's Pack"]), "Spellbook"]


### BACKGROUND DEFINITIONS ###

class BackgroundName(enum.StrEnum):
    ACOLYTE = "Acolyte"
    CHARLATAN = "Charlatan"
    CRIMINAL = "Criminal"
    ENTERTAINER = "Entertainer"
    FOLK_HERO = "Folk Hero"
    GUILD_ARTISAN = "Guild Artisan"
    HERMIT = "Hermit"
    KNIGHT = "Knight"
    NOBLE = "Noble"
    OUTLANDER = "Outlander"
    PIRATE = "Pirate"
    SAGE = "Sage"
    SAILOR = "Sailor"
    SCRIBE = "Scribe"
    SOLDIER = "Soldier"
    URCHIN = "Urchin"

class Background:
    name: BackgroundName
    sub_backrounds: list[str]
    skill_profs: list[Skills]
    tool_profs: list[AllTools]
    possible_tool_profs: list[AllTools]
    tool_prof_count: int
    possible_languages: list[Languages]
    language_count: int
    traits: list[AllTraits]
    gp: int
    equipment: list[str]

    def apply_subbackground(self, subbackground: Any):
        pass
    
'''
class (Background):
    name = BackgroundName.
    class SubBackground(enum.StrEnum):
        a
    sub_backgrounds = []
    skill_profs = []
    tool_profs = []
    possible_tool_profs = []
    tool_prof_count = 0
    possible_languages = []
    language_count = 0
    traits = []
    gp = 0
    equipment = []

    def apply_subbackground(self, subbackground):
        if subbackground == 
'''

class Acolyte(Background):
    name = BackgroundName.ACOLYTE
    sub_backrounds = []
    skill_profs = [Skills.INSIGHT, Skills.RELIGION]
    tool_profs = []
    possible_tool_profs = []
    tool_prof_count = 0
    possible_languages = list(Languages)
    language_count = 2
    traits = [BackgroundTrait.SHELTER_OF_THE_FAITHFUL]
    gp = 15
    equipment = [] # mega TODO ["Holy Symbol", random.choice(["Prayer Book", "Prayer Wheel"]), "5 Sticks of Incense", "Vestments", "Common Clothes"]

class Charlatan(Background):
    name = BackgroundName.CHARLATAN
    sub_backrounds = []
    skill_profs = [Skills.DECEPTION, Skills.SLEIGHT_OF_HAND]
    tool_profs = [Tools.DISGUISE, Tools.FORGERY]
    possible_tool_profs = []
    tool_prof_count = 0
    possible_languages = []
    language_count = 0
    traits = [BackgroundTrait.FALSE_IDENTITY]
    gp = 15
    equipment = [] # mega TODO ["Fine Clothes", "Disguise Kit", random.choice(["Ten Stoppered Bottles Filled with Coloured Liquid", "Set of Weighted Dice", "Deck of Marked Cards", "Signet Ring of an Imaginary Duke"])

class Criminal(Background):
    name = BackgroundName.CRIMINAL
    sub_backrounds = ["Blackmailer", "Burglar", "Enforcer", "Fence", "Highway Robber", "Hired Killer", "Pickpocket",
                       "Smuggler", "Spy"] # TODO make it so subbackground gets added to display name for Background
    skill_profs = [Skills.DECEPTION, Skills.STEALTH]
    tool_profs = [Tools.THIEF]
    possible_tool_profs = list(GamingSets)
    tool_prof_count = 1
    possible_languages = []
    language_count = 0
    traits = [BackgroundTrait.CRIMINAL_CONTACT]
    gp = 15
    equipment = [] # Crowbar, dark clothes including hood
       
class Entertainer(Background):
    name = BackgroundName.ENTERTAINER
    sub_backrounds = ["Actor", "Dancer", "Fire-Eater", "Gladiator", "Jester", "Juggler", "Instrumentalist",
                      "Poet", "Singer", "Storyteller", "Tumbler"] # TODO every entertainer gets 1-3 routines they're good at
    skill_profs = [Skills.ACROBATICS, Skills.PERFORMANCE]
    tool_profs = [Tools.DISGUISE]
    possible_tool_profs = list(MusicalInstruments)
    tool_prof_count = 1
    possible_languages = []
    language_count = 0
    traits = [BackgroundTrait.BY_POPULAR_DEMAND]
    gp = 15
    equipment = [] # Whichver musical instrument proficiency picks, "Costume", random.choice(["Love Letter from an Admirer", "Lock of Hair from an Admirer", "Trinket from an Admirer"])
  
class FolkHero(Background):
    name = BackgroundName.FOLK_HERO
    sub_backrounds = []
    skill_profs = [Skills.ANIMAL_HANDLING, Skills.SURVIVAL]
    tool_profs = [Tools.LAND_VEHICLES]
    possible_tool_profs = list(ArtisanTools)
    tool_prof_count = 1
    possible_languages = []
    language_count = 0
    traits = [BackgroundTrait.RUSTIC_HOSPITALITY]
    gp = 10
    equipment = [] # proficient artisan tool, Shovel, Iron Pot, Set of Common Clothes

class GuildArtisan(Background):
    name = BackgroundName.GUILD_ARTISAN
    sub_backrounds = ["Alchemists, Apothecaries", "Armorours, Locksmiths, Finesmiths", "Brewers, Distillers, Vintners", "Calligraphers, Scribes, Scriveners",
                      "Carpenters, Roofers, Pasterers", "Cobblers, Shoemakers", "Cooks, Bakers", "Glassblowers, Glaziers", "Jewelers, Gemcutters",
                      "Leatherworkers, Skinners, Tanners", "Masons, Stonecutters", "Painters, Limners, Sign-Makers", "Potters, Tile-Makers", "Merchants",
                      "Shipwrights, Sailmakers", "Smiths, Metal-Forgers", "Tinkers, Pewterers, Casters", "Weavers, Dryers", "Woodcarvers, Coopers, Bowyers"]
    skill_profs = [Skills.INSIGHT, Skills.PERSUASION]
    tool_profs = []
    possible_tool_profs = list(ArtisanTools)
    tool_prof_count = 1
    possible_languages = []
    language_count = 0
    traits = [BackgroundTrait.GUILD_MEMBERSHIP]
    gp = 15
    equipment = [] # proficient artisan tool, Letter of Introduction from your guild

class Hermit(Background):
    name = BackgroundName.HERMIT
    sub_backrounds = []
    skill_profs = [Skills.MEDICINE, Skills.RELIGION]
    tool_profs = [Tools.HERBALIST]
    possible_tool_profs = []
    tool_prof_count = 0
    possible_languages = list(Languages)
    language_count = 1
    gp = 5
    equipment = [] # "Scroll Case Stuffed Full of Notes from Your " + random.choice(["Prayers", "Studies"]), "Winter Blanket", "Set of Common Clothes", "Herbalism Kit"]

class Noble(Background):
    name = BackgroundName.NOBLE
    class SubBackground(enum.StrEnum):
        ARISTOCRAT = "Aristocrat"
        KNIGHT = "Knight"
    sub_backrounds = ["Aristocrat", "Knight"]
    skill_profs = [Skills.HISTORY, Skills.PERSUASION]
    tool_profs = []
    possible_tool_profs = list(GamingSets)
    tool_prof_count = 1
    possible_languages = list(Languages)
    language_count = 1
    gp = 25
    equipment = [] # ["Set of Fine Clothes", "Signet Ring", "Scroll of Pedigree"]

    def apply_subbackground(self, subbackground):
        if subbackground == Noble.SubBackground.ARISTOCRAT:
            self.traits.append(BackgroundTrait.POSITION_OF_PRIVILEGE)
        elif subbackground == Noble.SubBackground.KNIGHT:
            self.traits.append(BackgroundTrait.RETAINERS)

class Outlander(Background):
    name = BackgroundName.OUTLANDER
    sub_backgrounds = ["Forester", "Trapper", "Homesteader", "Guide", "Exile/Outcast", "Bounty Hunter",
                       "Pilgrim", "Tribal Nomad", "Hunter-Gatherer", "Tribal Marauder"]
    skill_profs = [Skills.ATHLETICS, Skills.SURVIVAL]
    tool_profs = []
    possible_tool_profs = list(MusicalInstruments)
    tool_prof_count = 1
    possible_languages = list(Languages)
    language_count = 1
    traits = [BackgroundTrait.WANDERER]
    gp = 10
    equipment = [] #["Staff", "Hunting Trap", "Trophy from an Animal You Killed", "Set of Traveler's Clothes"]

class Sage(Background):
    name = BackgroundName.SAGE
    sub_backgrounds = ["Alchemist", "Astronomer", "Discredited Academic", "Librarian", "Professor",
                       "Researcher", "Wizard's Apprentice", "Scribe"]
    skill_profs = [Skills.ARCANA, Skills.HISTORY]
    tool_profs = []
    possible_tool_profs = []
    tool_prof_count = 0
    possible_languages = list(Languages)
    language_count = 2
    traits = [BackgroundTrait.RESEARCHER]
    gp = 10
    equipment = [] #["Bottle of Black Ink", "Quill", "Small Knife", "Letter from a Dead Colleague Posing a Question You Cannot yet Answer", "Set of Common Clothes"]

class Sailor(Background):
    name = BackgroundName.SAILOR
    class SubBackground(enum.StrEnum):
        SAILOR = "Sailor"
        PIRATE = "Pirate"
    sub_backgrounds = ["Sailor", "Pirate"]
    skill_profs = [Skills.ATHLETICS, Skills.PERCEPTION]
    tool_profs = [Tools.NAVIGATOR, Tools.WATER_VEHICLES]
    possible_tool_profs = []
    tool_prof_count = 0
    possible_languages = []
    language_count = 0
    traits = []
    gp = 10
    equipment = [] #["Belaying Pin (Club)", "50 ft of Silk Rope", "Lucky Charm (Trinket)", "Set of Common Clothes"]

    def apply_subbackground(self, subbackground):
        if subbackground == Sailor.SubBackground.SAILOR:
            self.traits.append(BackgroundTrait.SHIPS_PASSAGE)
        elif subbackground == Sailor.SubBackground.PIRATE:
            self.traits.append(BackgroundTrait.BAD_REPUTATION)

class Soldier(Background):
    name = BackgroundName.SOLDIER
    sub_backgrounds = ["Officer", "Scout", "Infantry", "Cavalry", "Healer",
                       "Quartermaster", "Standard Bearer", "Support Staff"]
    skill_profs = [Skills.ATHLETICS, Skills.INTIMIDATION]
    tool_profs = [Tools.LAND_VEHICLES]
    possible_tool_profs = list(GamingSets)
    tool_prof_count = 1
    possible_languages = []
    language_count = 0
    traits = [BackgroundTrait.MILITARY_RANK]
    gp = 10
    equipment = [] # ["Insignia of Rank", "Trophy Taken from a Fallen Enemy", random.choice(["Bond Dice Set", "Playing Card Set"]), "Set of Common Clothes"]

class Urchin(Background):
    name = BackgroundName.URCHIN
    sub_backgrounds = []
    skill_profs = [Skills.SLEIGHT_OF_HAND, Skills.STEALTH]
    tool_profs = [Tools.DISGUISE, Tools.THIEF]
    possible_tool_profs = []
    tool_prof_count = 0
    possible_languages = []
    language_count = 0
    traits = [BackgroundTrait.CITY_SECRETS]
    gp = 10
    equipment = [] # ["Small Knife", "Map of Your Home City", "Pet Mouse", "Token to Remember Your Parents", "Set of Common Clothes"]

skill_expertises = [item for item, count in collections.Counter(skill_profs).items() if count > 1] # I included this so if you get the same skill proficiency from two different sources, it becomes an expertise (it's pretty darn rare)
tool_expertises = [item for item, count in collections.Counter(tool_profs).items() if count > 1] # You can delete these two rows if you don't want innate expertises

class Character:
    character_class: CharacterClass | None = None
    skill_profs: list[Skills] = []
    hp: int = 0
    gp: int = 0
    subclass: str = ""
    
    def create(self):
        pass

    def display_character(self):
        # print everything
        # self.character_class.print_extra_attributes()
        pass

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