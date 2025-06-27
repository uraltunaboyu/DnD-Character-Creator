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
import enum
import random
from typing import Any

from choices import Options, resolve, Choice, ChoiceUnit

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

### COMMON DEFINITIONS ###

class DamageType(enum.StrEnum): # TODO organize classes here
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

class Armours(enum.StrEnum):
    PADDED = "Padded armour"
    LEATHER = "Leather armour"
    STUD_LEATHER = "Studded leather armour"
    HIDE = "Hide armour"
    CHAIN_SHIRT = "Chain shirt"
    SCALE_MAIL = "Scale mail"
    BREASTPLATE = "Breastplate"
    HALF_PLATE = "Half plate armour"
    RING_MAIL = "Ring mail"
    CHAIN_MAIL = "Chain mail"
    SPLINT = "Splint armour"
    PLATE = "Plate armour"
    SHIELD = "Shield"

class ArmourTypes(enum.StrEnum):
    LIGHT = "Light Armour"
    MEDIUM = "Medium Armour"
    HEAVY = "Heavy Armour"
    SHIELD = "Shield"
    def to_list(self) -> list[Armours]:
        return {
            ArmourTypes.LIGHT: [Armours.PADDED, Armours.LEATHER, Armours.STUD_LEATHER],
            ArmourTypes.MEDIUM: [Armours.HIDE, Armours.CHAIN_SHIRT, Armours.SCALE_MAIL,\
                                 Armours.BREASTPLATE, Armours.HALF_PLATE],
            ArmourTypes.HEAVY: [Armours.RING_MAIL, Armours.CHAIN_MAIL, Armours.SPLINT, Armours.PLATE],
            ArmourTypes.SHIELD: [Armours.SHIELD]
        }[self]

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
    HAND_CROSSBOW = "Hand crossbow"
    HANDAXE = "Handaxe"
    HEAVY_CROSSBOW = "Heavy crossbow"
    JAVELIN = "Javelin"
    LANCE = "Lance"
    LIGHT_CROSSBOW = "Light crossbow"
    LIGHT_HAMMER = "Light hammer"
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
    WAR_PICK = "War pick"
    WARHAMMER = "Warhammer"
    WHIP = "Whip"

class Ammunition(enum.StrEnum):
    ARROWS = "arrows"
    BLOWGUN_NEEDLES = "blowgun Needles"
    BOLTS = "Crossbow bolts"
    SLING_BULLETS = "Sling bullets"

class ArcaneFocus(enum.StrEnum):
    CRYSTAL = "Crystal focus"
    ORB = "Orb focus"
    ROD = "Rod focus"
    STAFF = "Staff focus"
    WAND = "Wand focus"

class DruidicFocus(enum.StrEnum):
    SPRIG = "Sprig of mistletoe focus"
    TOTEM = "Totem focus"
    WOODEN_STAFF = "Wooden staff focus"
    YEW_WAND = "Yew wand focus"

class HolySymbols(enum.StrEnum):
    AMULET = "Amulet Symbol"
    EMBLEM = "Emblem Symbol"
    RELIQUARY = "Reliquary Symbol"

class Gear(enum.StrEnum):
    ABACUS = "Abacus"
    ACID = "Acid (vial)"
    ALCHEMIST_FIRE = "Alchemist's fire (flask)"
    ANTITOXIN = "Antitoxin (vial)"
    BACKPACK = "Backpack"
    BALL_BEARING = "Ball bearings (bag of 1,000)"
    BARREL = "Barrel"
    BASKET = "Basket"
    BEDROLL = "Bedroll"
    BELL = "Bell"
    BLANKET = "Blanket"
    BLOCK_TACKLE = "Block and tackle"
    BOOK = "Book"
    BOTTLE = "Bottle, glass"
    BUCKET = "Bucket"
    CALTROPS = "Caltrops (bag of 20)"
    CANDLE = "Candle"
    CASE_BOLT = "Case, crossbow bolt"
    CASE_MAP = "Case, map or scroll"
    CHAIN = "Chain (10 ft)"
    CHALK = "Chalk"
    CHEST = "Chest"
    CLIMB_KIT = "Climber's kit"
    CLOTHES_COMMON = "Set of common clothes"
    CLOTHES_COSTUME = "Set of costume clothes"
    CLOTHES_FINE = "Set of fine clothes"
    CLOTHES_TRAVELER = "set of traveler's clothes"
    COMPONENT_POUCH = "Component pouch"
    CROWBAR = "Crowbar"
    FISHING_TACKLE = "Fishing tackle"
    FLASK_TANKARD = "Flask or tankard"
    GRAPPLING = "Grappling hook"
    HAMMER = "Hammer"
    HAMMER_SLEDGE = "Hammer, sledge"
    HEALER = "Healer's kit"
    HOLY_WATER = "Holy water (flask)"
    HOURGLASS = "Hourglass"
    HUNTING_TRAP = "Hunting trap"
    INK = "Ink (1 ounce bottle)"
    INK_PEN = "Ink pen"
    JUG_PITCHER = "Jug or pitcher"
    LADDER = "Ladder (10-foot)"
    LAMP = "Lamp"
    LANTERN_BULLSEYE = "Lantern, bullseye"
    LANTERN_HOODED = "Lantern, hooded"
    LOCK = "Lock"
    MAGNIFYING = "Magnifying  glass"
    MANCLES = "Manacles"
    MESS_KIT = "Mess kit"
    MIRROR = "Mirror, steel"
    OIL = "Oil (flask)"
    PAPER = "Paper (one sheet)"
    PARCHMENT = "Parchment (one sheet)"
    PERFUME = "Perfume (vial)"
    PICK = "Pick, miner's"
    PITON = "Piton"
    POISON = "Poison, basic (vial)"
    POLE = "Pole (10 ft)"
    POT = "Pot, iron"
    POUCH = "Pouch"
    QUIVER = "Quiver"
    RAM = "Ram, portable"
    RATION = "Rations (1 day)"
    ROBES = "Robes"
    ROPE_HEMP = "Rope, hempen (50 ft)"
    ROPE_SILK = "Rope, silk (50 ft)"
    SACK = "Sack"
    SCALE = "Scale, merchant's"
    SEALING_WAX = "Sealing Wax"
    SHOVEL = "Shovel"
    SIGNAL_WHISTLE = "Signal Whistle"
    SIGNET_RING = "Signet Ring"
    SOAP = "Soap"
    SPELLBOOK = "Spellbook"
    SPIKES = "Spikes, iron (10)"
    SPYGLASS = "Spyglass"
    TENT = "Tent, two-person"
    TINDERBOX = "Tinderbox"
    TORCH = "Torch"
    VIAL = "Vial"
    WATERSKIN = "Waterskin"
    WHETSTONE = "Whetstone"

class Packs(enum.StrEnum):
    BURGLAR = "Burglar's pack"
    DIPLOMAT = "Diplomat's pack"
    DUNGEONEER = "Dungeoneer's pack"
    ENTERTAINER = "Entertainer's pack"
    EXPLORER = "Explorer's pack"
    PRIEST = "Priest's pack"
    SCHOLAR = "Scholar's pack"

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

AllGear = AllTools | ArcaneFocus | DruidicFocus | HolySymbols | Gear | MusicalInstruments | Packs

CombatGear = tuple[Ammunition, int] | Armours | Weapons | tuple[Weapons, int]

MARTIAL_MELEE: list[CombatGear] = [Weapons.BATTLEAXE, Weapons.FLAIL, Weapons.GLAIVE, Weapons.GREATAXE,\
                 Weapons.GREATSWORD, Weapons.HALBERD, Weapons.LANCE, Weapons.LONGSWORD,\
                 Weapons.MAUL, Weapons.MORNINGSTAR, Weapons.PIKE, Weapons.RAPIER,\
                 Weapons.SCIMITAR, Weapons.SCIMITAR, Weapons.SHORTSWORD, Weapons.TRIDENT,\
                 Weapons.WAR_PICK, Weapons.WARHAMMER, Weapons.WHIP]

MARTIAL_RANGED: list[CombatGear]= [Weapons.BLOWGUN, Weapons.HAND_CROSSBOW, Weapons.HEAVY_CROSSBOW,\
                  Weapons.SHORTBOW, Weapons.NET]

SIMPLE_MELEE: list[CombatGear] = [Weapons.CLUB, Weapons.DAGGER, Weapons.GREATCLUB, Weapons.HANDAXE,\
                Weapons.JAVELIN, Weapons.LIGHT_HAMMER, Weapons.MACE,Weapons.QUARTERSTAFF,\
                Weapons.SICKLE, Weapons.SPEAR]

SIMPLE_RANGED: list[CombatGear] = [Weapons.LIGHT_CROSSBOW, Weapons.DART, Weapons.SHORTBOW, Weapons.SLING]

class WeaponTypes(enum.StrEnum):
    MARTIAL_WEAPONS = "Martial Weapons"
    SIMPLE_WEAPONS = "Simple Weapons"
    def to_list(self) -> list[CombatGear]:
        return {
            WeaponTypes.MARTIAL_WEAPONS: MARTIAL_MELEE + MARTIAL_RANGED,
            WeaponTypes.SIMPLE_WEAPONS: SIMPLE_MELEE + SIMPLE_RANGED
        }[self]

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

class Traits(enum.StrEnum):
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

AllTraits = Traits | BackgroundTrait

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

class Race: #TODO Races need to be swapped to Options() syntax
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
    traits: list[Traits] = []
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
            self.traits.append(Traits.FIRE_BREATH_CONE)
        elif subrace == Dragonborn.Subrace.GREEN:
            self.resistances.append(DamageType.POISON)
            self.traits.append(Traits.POISON_BREATH)
        elif subrace == Dragonborn.Subrace.BLUE:
            self.resistances.append(DamageType.LIGHTNING)
            self.traits.append(Traits.LIGHTNING_BREATH)
        elif subrace == Dragonborn.Subrace.WHITE:
            self.resistances.append(DamageType.COLD)
            self.traits.append(Traits.COLD_BREATH)
        elif subrace == Dragonborn.Subrace.BLACK:
            self.resistances.append(DamageType.ACID)
            self.traits.append(Traits.ACID_BREATH)
        elif subrace == Dragonborn.Subrace.GOLD:
            self.resistances.append(DamageType.FIRE)
            self.traits.append(Traits.FIRE_BREATH_CONE)
        elif subrace == Dragonborn.Subrace.BRASS:
            self.resistances.append(DamageType.FIRE)
            self.traits.append(Traits.FIRE_BREATH_LINE)
        elif subrace == Dragonborn.Subrace.COPPER:
            self.resistances.append(DamageType.ACID)
            self.traits.append(Traits.ACID_BREATH)
        elif subrace == Dragonborn.Subrace.BRONZE:
            self.resistances.append(DamageType.FIRE)
            self.traits.append(Traits.FIRE_BREATH_LINE)

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
    traits = [Traits.DWARVEN_RESILIENCE, Traits.DARKVISION60]
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
    traits = [Traits.DARKVISION60, Traits.KEEN_SENSES, Traits.FEY_ANCESTRY, Traits.TRANCE]
    languages = [Languages.COMMON, Languages.ELVISH]
    
    def apply_subrace(self, subrace: Any):
        if subrace == Elf.Subrace.DROW:
            self.stat_increases.append((Attributes.CHA, 1))
            self.traits.remove(Traits.DARKVISION60)
            self.traits.extend([Traits.DARKVISION120, Traits.DROW_MAGIC, Traits.SUNLIGHT_SENSITIVITY])
            self.weapon_proficiencies.extend([Weapons.RAPIER, Weapons.SHORTSWORD, Weapons.HAND_CROSSBOW])
            self.size_mod_range = (2, 12)
            self.base_height = 4 * 12 + 5
            self.base_weight = 75
            self.weight_range = (1, 6)
        elif subrace == Elf.Subrace.HIGH:
            self.stat_increases.append((Attributes.INT, 1))
            self.traits.extend([Traits.CANTRIP])
            self.weapon_proficiencies.extend([Weapons.LONGSWORD, Weapons.SHORTSWORD, Weapons.SHORTBOW, Weapons.LONGBOW])
            self.possible_languages = list(Languages)
            self.language_count = 1
            self.size_mod_range = (2, 20)
            self.base_height = 4 * 12 + 6
            self.base_weight = 90
            self.weight_range = (1, 4)
        elif subrace == Elf.Subrace.WOOD:
            self.stat_increases.append((Attributes.WIS, 1))
            self.traits.extend([Traits.MASK_OF_THE_WILD])
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
    traits = [Traits.DARKVISION60, Traits.GNOME_CUNNING]
    languages = [Languages.COMMON, Languages.GNOMISH]
    
    def apply_subrace(self, subrace: Any):
        if subrace == Gnome.Subrace.FOREST:
            self.stat_increases.append((Attributes.DEX, 1))
            self.traits.extend([Traits.NATURAL_ILLUSIONIST, Traits.SPEAK_WITH_SMALL_BEASTS])
        elif subrace == Gnome.Subrace.ROCK:
            self.stat_increases.append((Attributes.CON, 1))
            self.traits.extend([Traits.ARTIFICERS_LORE, Traits.TINKER])
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
    traits = [Traits.DARKVISION60, Traits.FEY_ANCESTRY]
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
    traits = [Traits.BRAVE, Traits.HALFLING_NIMBLENESS, Traits.LUCKY]
    languages = [Languages.COMMON, Languages.HALFLING]
    
    def apply_subrace(self, subrace: Any):
        if subrace == Halfling.Subrace.LIGHTFOOT:
            self.stat_increases.append((Attributes.CHA, 1))
            self.traits.append(Traits.NATURALLY_STEALTHY)
        elif subrace == Halfling.Subrace.STOUT:
            self.stat_increases.append((Attributes.CON, 1))
            self.traits.append(Traits.STOUT_RESILIENCE)
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
    traits = [Traits.DARKVISION60, Traits.RELENTLESS_ENDURANCE, Traits.SAVAGE_ATTACKS]
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
            self.stat_increases.extend([
                (Attributes.STR, 1),
                (Attributes.DEX, 1),
                (Attributes.CON, 1),
                (Attributes.INT, 1),
                (Attributes.WIS, 1),
                (Attributes.CHA, 1)
            ])
        elif subrace == Human.Subrace.VARIANT:
            # TODO two random Attributes increase by 1
            self.possible_skill_profs = list(Skills)
            self.skill_prof_count = 1
            self.traits.append(Traits.FEAT)

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
    traits = [Traits.DARKVISION60, Traits.INFERNAL_LEGACY]
    resistances = [DamageType.FIRE]
    languages = [Languages.COMMON, ExoticLanguages.INFERNAL]
  
class ClassName(enum.StrEnum):
    BARBARIAN = "Barbarian"
    BARD = "Bard"
    CLERIC = "Cleric"
    DRUID = "Druid"
    FIGHTER = "Fighter"
    MONK = "Monk"
    PALADIN = "Paladin"
    RANGER = "Ranger"
    ROGUE = "Rogue"
    SORCERER = "Sorcerer"
    WARLOCK = "Warlock"
    WIZARD = "Wizard"

class CharacterClass:
    name: ClassName
    armour_profs: list[ArmourTypes] | Choice[ArmourTypes] = []
    saving_throw_profs: list[Attributes] | Choice[AllGear] = []
    skill_profs: list[Skills] | Choice[Skills] = []
    weapon_profs: list[WeaponTypes | Weapons] | Choice[WeaponTypes | Weapons] = []
    traits: list[tuple[str, int] | tuple[str, int, enum.StrEnum]] #TODO Ability score improvement not included in traits since it feels redundant to put it 5 times in every class (lvl 4,8,12,16,19)
    combat_gear: list[CombatGear | Choice[ChoiceUnit[CombatGear]]] = []
    gear: list[AllGear | Choice[ChoiceUnit[AllGear]]] = []
    tool_profs: list[AllTools | Choice[ChoiceUnit[AllTools]]] = []

    hit_die = 0
    skill_prof_count = 1 #TODO double check, I think depreciated (same with below for some)

    def __init__(self):
        pass

    def define_subclass(self):
        self.subclass = random.choice(self.subclasses or ["None"])

    def resolve_traits(self):
        pass

    def resolve_proficiencies(self, proficiencies):
        pass

class FightingClass(CharacterClass):
    fighting_styles: list[str] = []
    
    def define_fighting_style(self): # TODO Convert to Options()?
        self.fighting_style = random.choice(self.fighting_styles)

### CLASS DEFINITIONS ###

class Barbarian(CharacterClass):
    name = ClassName.BARBARIAN
    hit_die = 12
    # Subclass at Level 3, officially called "Primal Path"
    # Base Rules = Berserker, Totem Warior
    class Subclasses(enum.StrEnum): # TODO level check for subclass
        BERSERKER = "Berserker"
        TOTEM_WARRIOR = "Totem Warrior"
        
        @enum.property
        def value(self) -> str:
            return f"Path of the {str(self)}"
        
        def to_traits(self) -> list[tuple[str, int]]:
            return {
                Barbarian.Subclasses.BERSERKER: [("Frenzy", 3), ("Mindless Rage", 6), ("Intimidating Presence", 10), ("Retaliation", 14)],
                Barbarian.Subclasses.TOTEM_WARRIOR: [("Spirit Seeker", 3), ("Totem Spirit", 3), ("Aspect of the Beast", 6), ("Spirit Walker", 10), ("Totemic Attunement", 14)]
            }[self]
    armour_profs = [ArmourTypes.LIGHT, ArmourTypes.MEDIUM, ArmourTypes.SHIELD]
    weapon_profs = list(WeaponTypes)
    saving_throw_profs = [Attributes.STR, Attributes.CON]
    skill_profs = Choice([Skills.ANIMAL_HANDLING, Skills.ATHLETICS, Skills.INTIMIDATION, Skills.NATURE, Skills.PERCEPTION, Skills.SURVIVAL], 2)
    combat_gear = [Choice(MARTIAL_MELEE), Choice(WeaponTypes.SIMPLE_WEAPONS.to_list()), (Weapons.JAVELIN, 4)] # type: ignore[arg-type]
    gear = [Packs.EXPLORER]
    traits = [("Rage", 1), ("Unarmoured Defense", 1), ("Danger Sense", 2), ("Reckless Attack", 2),\
              ("Extra Attack", 5), ("Fast Movement", 5), ("Feral Instinct", 7), ("Brutal Critical", 9),\
              ("Relentless Rage", 11), ("Persistent Rage", 15), ("Indomitable Might", 18), ("Primal Champion", 20)]

class Bard(CharacterClass):
    name = ClassName.BARD
    hit_die = 8
    # Subclass at Level 3, officially called "Bard College"
    # Base Rules = Lore, Valor
    class Subclasses(enum.StrEnum):
        LORE = "Lore"
        VALOR = "Valor"

        @enum.property
        def value(self) -> str:
            return f"College of {str(self)}"
                
        def to_traits(self) -> list[tuple[str, int]]:
            return {
                Bard.Subclasses.LORE: [("Bonus Proficiencies", 3), ("Cutting Words", 3), ("Additional Magical Secrets", 6), ("Peerless Skill", 14)],
                Bard.Subclasses.VALOR: [("Bonus Proficiencies", 3), ("Combat Inspiration", 3), ("Extra Attack", 6), ("Battle Magic", 14)]
            }[self]
    armour_profs = [ArmourTypes.LIGHT]
    weapon_profs = [WeaponTypes.SIMPLE_WEAPONS, Weapons.HAND_CROSSBOW, Weapons.LONGSWORD, Weapons.RAPIER, Weapons.SHORTSWORD]
    saving_throw_profs = [Attributes.DEX, Attributes.CHA]
    skill_profs = Choice(list(Skills), 3)
    tool_profs = Choice(list(MusicalInstruments), 3)
    combat_gear = [Weapons.DAGGER, Armours.LEATHER, Choice([Weapons.RAPIER, Weapons.LONGSWORD] + WeaponTypes.SIMPLE_WEAPONS.to_list())] # TODO make sure type alias is being used
    gear = [Choice([Packs.DIPLOMAT, Packs.ENTERTAINER]), Choice(list(MusicalInstruments))]
    traits = [("Spellcasting", 1), ("Bardic Inspiration", 1), ("Jack of All Trades", 2), ("Song of Rest", 2), ("Expertise", 3),\
              ("Font of Inspiration", 5), ("Countercharm", 6), ("Magical Secrets", 10), ("Superior Inspiration", 20)]
    
class Cleric(CharacterClass):
    name = ClassName.CLERIC
    hit_die = 8
    # Subclass at Level 1, officially called "Divine Domain"
    # Base Rules = Knowledge, Life, Light, Nature, Tempest, Trickery, War
    class Subclasses(enum.StrEnum):
        KNOWLEDGE = "Knowledge Domain"
        LIFE = "Life Domain"
        LIGHT = "Light Domain"
        NATURE = "Nature Domain"
        TEMPEST = "Tempest Domain"
        TRICKERY = "Trickery Domain"
        WAR = "War Domain"
                
        def to_traits(self) -> list[tuple[str, int]]:
            return {
                Cleric.Subclasses.KNOWLEDGE: [("Blessing of Knowledge", 1), ("Channel Divinity: Knowledge of the Ages", 2), ("Channel Divinity: Read Thoughts", 6), ("Potent Spellcasting", 9), ("Visions of the Past", 17)],
                Cleric.Subclasses.LIFE: [("Bonus Proficiency", 1), ("Disciple of Life", 1), ("Channel Divinity: Preserve Life", 2), ("Blessed Healer", 6), ("Divine Strike", 8), ("Supreme Healing", 17)],
                Cleric.Subclasses.LIGHT: [("Bonus Cantrip", 1), ("Warding Flare", 1), ("Channel Divinity: Radiance of the Dawn", 2), ("Improved Flare", 6), ("Potent Spellcasting", 8), ("Corona of Light", 17)],
                Cleric.Subclasses.NATURE: [("Acolyte of Nature", 1), ("Bonus Proficiency", 1), ("Channel Divinity: Charm Animals and PLants", 2), ("Dampen Elements", 8), ("Divine Strike", 8), ("Master of Nature", 17)],
                Cleric.Subclasses.TEMPEST: [("Bonus Proficiencies", 1), ("Wrath of the Storm", 1), ("Channel Divinity: Destructive Wrath", 2), ("Thunderbolt Strike", 6), ("Divine Strike", 8), ("Stormborn", 17)],
                Cleric.Subclasses.TRICKERY: [("Blessing of the Trickster", 1), ("Channel Divinity: Invoke Duplicity", 2), ("Channel Divinity: Cloak of Shadows", 6), ("Divine Strike", 8), ("Improved Duplicity", 17)],
                Cleric.Subclasses.WAR: [("Bonus Proficiencies", 1), ("War Priest", 1), ("Channel Divinity: Guided Strike", 2), ("Channel Divinity: War God's Blessing", 6), ("Divine Strike", 8), ("Avatar of Battle", 17)],
            }[self]
    armour_profs = [ArmourTypes.LIGHT, ArmourTypes.MEDIUM, ArmourTypes.SHIELD]
    weapon_profs = [WeaponTypes.SIMPLE_WEAPONS]
    saving_throw_profs = [Attributes.WIS, Attributes.CHA]
    skill_profs = Options([Skills.HISTORY, Skills.INSIGHT, Skills.MEDICINE, Skills.PERSUASION, Skills.RELIGION], num_choices=2)
    combat_gear = Options([Options([Weapons.LIGHT_CROSSBOW, (Ammunition.BOLTS, 20)], [Armours.SHIELD]), Options(WeaponTypes.SIMPLE_WEAPONS.to_list(), [Armours.SHIELD])])
    gear = [Options([Packs.PRIEST, Packs.EXPLORER]), Options(list(HolySymbols))]
    
    traits = [("Spellcasting", 1), ("Channel Divinity", 2), ("Destroy Undead", 5), ("Divine Intervention", 10)]
    # TODO Figure out the if statement of equipment (depends on proficiencies)
    # if "Warhammer" in weapon_profs or "Martial Weapons" in weapon_profs:
    #     equipment.extend([random.choice(["Mace", "Warhammer"])])
    # else:
    #     equipment.extend(["Mace"])
    # if "Chain Mail" in armour_profs or "Heavy Armour" in armour_profs:
    #     equipment.extend([random.choice(["Scale Mail", "Leather Armour", "Chain Mail"])])
    # else:
    #     equipment.extend([random.choice(["Scale Mail", "Leather Armour"])])
    
class Druid(CharacterClass):
    name = ClassName.DRUID
    hit_die = 8
    # Subclass at Level 2, officially called "Druid Circle"
    # Base Rules = Land, Moon
    class Subclasses(enum.StrEnum):
        LAND = "Land"
        MOON = "Moon"

        @enum.property # Save logic for later if we expand
        def value(self) -> str:
            return f"Circle of the {str(self)}"

        def to_traits(self) -> list[tuple[str, int]]:
            return {
                Druid.Subclasses.LAND: [("Bonus Cantrip", 2), ("Natural Recovery", 2), ("Circle Spells", 3), ("Land's Stride", 14), ("Nature's Ward", 10), ("Nature's Sanctuary", 14)],
                Druid.Subclasses.MOON: [("Combat Wild Shape", 2), ("Circle Forms", 2), ("Primal Strike", 6), ("Elemental Wild Shape", 10), ("Thousand Forms", 14)]
            }[self]
    land_domains = ["Arctic", "Coast", "Desert", "Forest", "Grassland", "Mountain", "Swamp", "Underdark"]
    armour_profs = [ArmourTypes.LIGHT, ArmourTypes.MEDIUM, ArmourTypes.SHIELD]
    weapon_profs = [Weapons.CLUB, Weapons.DAGGER, Weapons.DART, Weapons.JAVELIN, Weapons.MACE, Weapons.QUARTERSTAFF, Weapons.SCIMITAR, Weapons.SICKLE, Weapons.SLING, Weapons.SPEAR]
    tool_profs = [Tools.HERBALIST]
    saving_throw_profs = [Attributes.INT, Attributes.WIS]
    skill_profs = Options([Skills.ANIMAL_HANDLING, Skills.ARCANA, Skills.INSIGHT, Skills.MEDICINE, Skills.NATURE, Skills.PERCEPTION, Skills.RELIGION, Skills.SURVIVAL], num_choices=2)
    combat_gear = [Options([Weapons.SCIMITAR] + SIMPLE_MELEE), Options([Armours.LEATHER])] # TODO Shield or simple weapon
    gear = [Options([Packs.EXPLORER]), Options(list(DruidicFocus))]
    traits = [("Druidic", 1), ("Spellcasting", 1), ("Wild Shape", 2), ("Timeless Body", 18), ("Beast Spells", 18), ("Archdruid", 20)]

    def __init__(self): #TODO check if depreciated, if so, work it back into the thing somehow
        super().__init__()

    def define_subclass(self):
        super().define_subclass()
        if self.subclass == Druid.Subclasses.LAND:
            land = random.choice(self.land_domains)
            self.subclass = "Circle of the Land " + land
    
class Fighter(FightingClass):
    name = ClassName.FIGHTER
    hit_die = 10
    # Chosen at level 1
    # Base Rules = Archery, Defense, Dueling, Great Weapon Fighting, Protection, Two-Weapon Fighting
    fighting_styles = ["Archery", "Defense", "Dueling", "Great Weapon Fighting", "Protection", "Two-Weapon Fighting"]
    # Sublass at Level 3, officially called "Martial Archetype"
    # Base Rules = Battle Master, Champion, Eldritch Knight
    class Subclasses(enum.StrEnum):
        BATTLE_MASTER = "Battle Master"
        CHAMPION = "Champion"
        ELDRITCH = "Eldritch Knight"
                
        def to_traits(self) -> list[tuple[str, int]]:
            return {
                Fighter.Subclasses.BATTLE_MASTER: [("Combat Superiority", 3), ("Student of War", 3), ("Know Your Enemy", 7), ("Improved Combat Superiority", 10), ("Relentless", 15)],
                Fighter.Subclasses.CHAMPION: [("Improved Critical", 3), ("Remarkable Athlete", 7), ("Additional Fighting Style", 10), ("Superior Critical", 15), ("Survivor", 18)],
                Fighter.Subclasses.ELDRITCH: [("Spellcasting", 3), ("Weapon Bond", 3), ("War Magic", 7), ("Eldritch Strike", 10), ("Arcane Charge", 15), ("Improved War Magic", 18)]
            }[self]
    armour_profs = list(ArmourTypes)
    weapon_profs = list(WeaponTypes)
    saving_throw_profs = [Attributes.STR, Attributes.CON]
    skill_profs = Options([Skills.ACROBATICS, Skills.ANIMAL_HANDLING, Skills.ATHLETICS, Skills.HISTORY, Skills.INSIGHT, Skills.INTIMIDATION, Skills.PERCEPTION, Skills.SURVIVAL], num_choices=2)
    weapons = [Options([Weapons.LIGHT_CROSSBOW, [Weapons.HANDAXE]*2])] # TODO a) Chainmail, b) Leather armour, longbow, 20 arrows TODO 2 handaxes may not work properly
    gear = [Options([Packs.DUNGEONEER, Packs.EXPLORER])] # TODO a) Martial weapon, shield, b) two martial weapons
    traits = [("Second Wind", 1), ("Action Surge", 2), ("Extra Attack", 5), ("Indomitable", 9)]

class Monk(CharacterClass):
    name = ClassName.MONK
    hit_die = 8
    # Subclass at Level 3, officially called "Monastic Tradition"
    # Base Rules = Four Elements, Open Hand, Shadow
    class Subclasses(enum.StrEnum):
        FOUR_ELEMENTS = "Way of the Four Elements"
        OPEN_HAND = "Way of the Open Hand"
        SHADOW = "Way of Shadow"
                
        def to_traits(self) -> list[tuple[str, int]]:
            return {
                Monk.Subclasses.FOUR_ELEMENTS: [("Disciple of the Elements", 3)],
                Monk.Subclasses.OPEN_HAND: [("Open Hand Technique", 3), ("Wholeness of Body", 6), ("Tranquility", 11), ("Quivering Palm", 17)],
                Monk.Subclasses.SHADOW: [("Shadow Arts", 3), ("Shadow Step", 6), ("Cloak of Shadows", 11), ("Opportunist", 17)]
            }[self]
    weapon_profs = [WeaponTypes.SIMPLE_WEAPONS, Weapons.SHORTSWORD]
    saving_throw_profs = [Attributes.STR, Attributes.DEX]
    skill_profs = Options([Skills.ACROBATICS, Skills.ATHLETICS, Skills.HISTORY, Skills.INSIGHT, Skills.RELIGION, Skills.STEALTH], num_choices=2)
    weapons = [Options([Weapons.SHORTSWORD] + WeaponTypes.SIMPLE_WEAPONS.to_list(), [Weapons.DART]*10)]
    gear = [Options([Packs.DUNGEONEER, Packs.EXPLORER])]
    traits = [("Unarmoured Defense", 1), ("Martial Arts", 1), ("Ki", 2), ("Unarmoured Movement", 2), ("Deflect Missiles", 3), ("Slow Fall", 4),\
              ("Extra Attack", 5), ("Stunning Strike", 5), ("Ki-Empowered Movement", 6), ("Evasion", 7), ("Stillness of Mind", 7), ("Purity of Body", 10),\
              ("Tongue of the Sun and Moon", 13), ("Diamond Soul", 14), ("Timeless Body", 15), ("Empty Body", 18), ("Perfect Self", 20)]
    
class Paladin(FightingClass):
    name = ClassName.PALADIN
    hit_die = 10
    # Fighting Style at Level 2
    # Base Rules = Defense, Dueling, Great Weapon Fighting, Protection
    fighting_style = ["Defense", "Dueling", "Great Weapon Fighting", "Protection"]
    # Subclass at Level 3, officially called "Sacred Oath"
    # Base Rules = Ancients, Devotion, Vengeance
    class Subclasses(enum.StrEnum):
        ANCIENTS = "Oath of the Ancients"
        DEVOTION = "Oath of Devotion"
        VENGEANCE = "Oath of Vengeance"
                
        def to_traits(self) -> list[tuple[str, int]]:
            return {
                Paladin.Subclasses.ANCIENTS: [("Tenets of the Ancients", 3), ("Oath Spells", 3), ("Channel Divinity", 3), ("Aura of Warding", 7), ("Undying Sentinel", 15), ("Elder Champion", 20)],
                Paladin.Subclasses.DEVOTION: [("Tenets of Devotion", 3), ("Oath Spells", 3), ("Channel Divinity", 3), ("Aura of Devotion", 7), ("Purity of Spirit", 15), ("Holy Nimbus", 20)],
                Paladin.Subclasses.VENGEANCE: [("Tenets of Vengeance", 3), ("Oath Spells", 3), ("Channel Divinity", 3), ("Relentless Avenger", 7), ("Soul of Vengeance", 15), ("Avenging Angel", 20)]
            }[self]
    armour_profs = list(ArmourTypes)
    weapon_profs = list(WeaponTypes)
    saving_throw_profs = [Attributes.WIS, Attributes.CHA]
    skill_profs = Options([Skills.ATHLETICS, Skills.INSIGHT, Skills.INTIMIDATION, Skills.MEDICINE, Skills.PERSUASION, Skills.RELIGION], num_choices=2)
    weapons = [Options([[Weapons.JAVELIN]*5 + SIMPLE_MELEE])] # TODO a) Martial weapon, shield, b) two martial weapons
    gear = [Options([Packs.PRIEST, Packs.EXPLORER]), Options(list(HolySymbols)), Options([Armours.CHAIN_MAIL])]
    traits = [("Divine Sense", 1), ("Lay On Hands", 1), ("Spellcasting", 2), ("Divine Smite", 2), ("Divine Health", 3), ("Extra Attack", 5),\
              ("Aura of Protection", 6), ("Aura of Courage", 10), ("Improved Divine Smite", 11), ("Cleansing Touch", 14)]

class Ranger(FightingClass):
    name = ClassName.RANGER
    hit_die = 10
    # Fighting Style at Level 2
    # Base Rules = Archery, Defense, Dueling, Two-Weapon Fighting
    fighting_style = ["Archery", "Defense", "Dueling", "Two-Weapon Fighting"]
    # Subclass at Level 3, officially called "Ranger Conclave"
    # Base Rules = Beast Master, Hunter
    class Subclasses(enum.StrEnum):
        BEAST_MASTER = "Beast Master"
        HUNTER = "Hunter"
                
        def to_traits(self) -> list[tuple[str, int]]:
            return {
                Ranger.Subclasses.BEAST_MASTER: [("Ranger's Companion", 3), ("Exceptional Training", 7), ("Bestial Fury", 11), ("Share Spells", 15)],
                Ranger.Subclasses.HUNTER: [("Hunter's Prey", 3), ("Defensive Tactics", 7), ("Multiattack", 11), ("Superior Hunter's Defense", 15)]
            }[self]
    armour_profs = [ArmourTypes.LIGHT, ArmourTypes.MEDIUM, ArmourTypes.SHIELD]
    weapon_profs = list(WeaponTypes)
    saving_throw_profs = [Attributes.STR, Attributes.DEX]
    skill_profs = Options([Skills.ANIMAL_HANDLING, Skills.ATHLETICS, Skills.INSIGHT, Skills.INVESTIGATION, Skills.NATURE, Skills.PERCEPTION, Skills.STEALTH, Skills.SURVIVAL], num_choices=3)
    weapons = [Weapons.SHORTBOW] # TODO a) 2 shortswords, b) two simple melee weapons
    gear = [Options([Armours.SCALE_MAIL, Armours.LEATHER]), Options([Packs.DUNGEONEER, Packs.EXPLORER]), Options([(Ammunition, 20)])]
    traits = [("Favoured Enemy", 1), ("Natural Explorer", 1), ("Spellcasting", 2), ("Primeval Awareness", 3), ("Extra Attack", 5), ("Land's Stride", 8),\
              ("Hide in Plain Sight", 10), ("Vanish", 14), ("Feral Sense", 18), ("Foe Slayer", 20)]

class Rogue(CharacterClass):
    name = ClassName.ROGUE
    hit_die = 8
    # Subclass at Level 3, officially called "Roguish Archtype"
    # Base Rules = Arcane Trickster, Assassin, Thief
    class Subclasses(enum.StrEnum):
        ARCANE = "Arcane Trickster"
        ASSASSIN = "Assassin"
        THIEF = "Theif"
                
        def to_traits(self) -> list[tuple[str, int]]:
            return {
                Rogue.Subclasses.ARCANE: [("Spellcasting", 3), ("Mage Hand Legerdemain", 3), ("Magical Ambush", 9), ("Versatile Trickster", 13), ("Spell Thief", 17)],
                Rogue.Subclasses.ASSASSIN: [("Bonus Proficiencies", 3), ("Assassinate", 3), ("Infiltration Expertise", 9), ("Imposter", 13), ("Death Strike", 17)],
                Rogue.Subclasses.THIEF: [("Fast Hands", 3), ("Second-Story Work", 3), ("Supreme Sneak", 9), ("Use Magic Device", 13), ("Thief's Reflexes", 17)]
            }[self]
    armour_profs = [ArmourTypes.LIGHT]
    weapon_profs = [WeaponTypes.SIMPLE_WEAPONS, Weapons.HAND_CROSSBOW, Weapons.LONGSWORD, Weapons.RAPIER, Weapons.SHORTSWORD]
    tool_profs = [Tools.THIEF]
    saving_throw_profs = [Attributes.DEX, Attributes.INT]
    available_skill_profs = Options([Skills.ACROBATICS, Skills.ATHLETICS, Skills.DECEPTION, Skills.INSIGHT, Skills.INTIMIDATION, Skills.INVESTIGATION, Skills.PERCEPTION, Skills.PERFORMANCE, Skills.PERSUASION, Skills.SLEIGHT_OF_HAND, Skills.STEALTH], num_choices=4)
    weapons = [Options([Weapons.RAPIER, Weapons.SHORTSWORD], [Weapons.DAGGER]*2)] # TODO a) Shortbow, 20 arrows, b) Shortsword 
    gear = [Options([Packs.BURGLAR, Packs.DUNGEONEER, Packs.EXPLORER]), Options([Armours.LEATHER]), Options([Tools.THIEF])]
    traits = [("Expertise", 1), ("Sneak Attack", 1), ("Thieve's Cant", 1), ("Cunning Action", 2), ("Uncanny Dodge", 5), ("Evasion", 7),\
              ("Reliable Talent", 11), ("Blindsense", 14), ("Slippery Mind", 15), ("Elusive", 18), ("Stroke of Luck", 20)]

class Sorcerer(CharacterClass):
    name = ClassName.SORCERER
    hit_die = 6
    # Subclass at Level 1, officially called "Sorcerous Origin"
    # Base Rules = Draconic Bloodline, Wild Magic
    class Subclasses(enum.StrEnum):
        DRACONIC = "Draconic Bloodline"
        WILD_MAGIC = "Wild Magic"
                 
        def to_traits(self) -> list[tuple[str, int]]:
            return {
                Sorcerer.Subclasses.DRACONIC: [("Dragon Ancestor", 1), ("Draconic Resilience", 1), ("Elemental Affinity", 6), ("Dragon Wings", 14), ("Draconic Presence", 18)], #TODO random pick draconic ancestor
                Sorcerer.Subclasses.WILD_MAGIC: [("Wild Magic Surge", 1), ("Tides of Chaos", 1), ("Bend Luck", 6), ("Controlled Chaos", 14), ("Spell Bombardment", 18)]
            }[self]
    weapon_profs = [Weapons.DAGGER, Weapons.DART, Weapons.SLING, Weapons.QUARTERSTAFF, Weapons.LIGHT_CROSSBOW]
    saving_throw_profs = [Attributes.CON, Attributes.CHA]
    skill_profs = Options([Skills.ARCANA, Skills.DECEPTION, Skills.INSIGHT, Skills.INTIMIDATION, Skills.PERSUASION, Skills.RELIGION], num_choices=2)
    weapons = [[Weapons.DAGGER]*2] #TODO a) light crossbow, 20 bolts, b) simple weapon
    gear = [Options([list(ArcaneFocus) + [Gear.COMPONENT_POUCH]]), Options([Packs.DUNGEONEER, Packs.EXPLORER])]
    traits = [("Spellcasting", 1), ("Font of Magic", 2), ("Metamagic", 3), ("Sorcerous Restorations", 20)]
    
class Warlock(FightingClass):
    name = ClassName.WARLOCK
    hit_die = 8
    # Subclass at Level 1, officially called "Otherworldly Patron"
    # Base Rules = Archfey, Fiend, Great Old One
    class Subclasses(enum.StrEnum):
        ARCHFEY = "The Archfey"
        FIEND = "The Fiend"
        GREAT_OLD_ONE = "The Great Old One"
                 
        def to_traits(self) -> list[tuple[str, int]]:
            return {
                Warlock.Subclasses.ARCHFEY: [("Expanded Spell List", 1), ("Fey Presence", 1), ("Misty Escape", 6), ("Beguiling Defenses", 10), ("Dark Delirium", 14)],
                Warlock.Subclasses.FIEND: [("Expanded Spell List", 1), ("Dark One's Blessing", 1), ("Dark One's Own Luck", 6), ("Fiendish Resilience", 10), ("Hurl Through Hell", 14)],
                Warlock.Subclasses.GREAT_OLD_ONE: [("Expanded Spell List", 1), ("Awakened Mind", 1), ("Entropic Ward", 6), ("Thought Shield", 10), ("Create Thrall", 14)]
            }[self]
    # Fighting Style at Level 3, officially called "Pact Boon"
    fighting_styles = ["Pact of the Blade", "Pact of the Chain", "Pact of the Tome"]
    armour_profs = [ArmourTypes.LIGHT]
    weapon_profs = [WeaponTypes.SIMPLE_WEAPONS]
    saving_throw_profs = [Attributes.WIS, Attributes.CHA]
    skill_profs = Options([Skills.ARCANA, Skills.DECEPTION, Skills.HISTORY, Skills.INTIMIDATION, Skills.INVESTIGATION, Skills.NATURE, Skills.RELIGION], num_choices=2)
    weapons = [Options(WeaponTypes.SIMPLE_WEAPONS.to_list(), [Weapons.DAGGER]*2)] #TODO a) light crossbow, 20 bolts, b) simple weapon
    gear = [Options(list(ArcaneFocus) + [Gear.COMPONENT_POUCH]), Options([Packs.SCHOLAR, Packs.DUNGEONEER]), Options([Armours.LEATHER])]
    traits = [("Pact Magic", 1), ("Eldritch Invocations", 2), ("Mystic Arcanum", 11), ("Eldritch Master", 20)]

class Wizard(CharacterClass):
    name = ClassName.WIZARD
    hit_die = 6
    # Sublass at Level 2, officially called "Arcane Tradition"
    # Base Rules = Abjuration, Conjuration, Divination, Enchantment, Evocation, Illusion, Necromancy, Transmutation
    class Subclasses(enum.StrEnum):
        ABJURATION = "School of Abjuration"
        CONJURATION = "School of Conjuration"
        DIVINATION = "School of Divination"
        ENCHANTMENT = "School of Enchantment"
        EVOCATION = "School of Evocation"
        ILLUSION = "School of Illusion"
        NECROMANCY = "School of Necromancy"
        TRANSMUTATION = "School of Transmutation"
                 
        def to_traits(self) -> list[tuple[str, int]]:
            return {
                Wizard.Subclasses.ABJURATION: [("Abjuration Savant", 2), ("Arcane Ward", 2), ("Projected Ward", 6), ("Improved Abjuration", 10), ("Spell Resistance", 14)],
                Wizard.Subclasses.CONJURATION: [("Conjuration Savant", 2), ("Minor Conjuration", 2), ("Benign Transposition", 6), ("Focused Conjuration", 10), ("Durable Summons", 14)],
                Wizard.Subclasses.DIVINATION: [("Divination Savant", 2), ("Portent", 2), ("Expert Divination", 6), ("The Third Eye", 10), ("Greater Portent", 14)],
                Wizard.Subclasses.ENCHANTMENT: [("Enchantment Savant", 2), ("Hypnotic Gaze", 2), ("Instinctive Charm", 6), ("Split Enchantment", 10), ("Alter Memories", 14)],
                Wizard.Subclasses.EVOCATION: [("Evocation Savant", 2), ("Sculpt Spells", 2), ("Potent Cantrip", 6), ("Empowered Evocation", 10), ("Overchannel", 14)],
                Wizard.Subclasses.ILLUSION: [("Illusion Savant", 2), ("Improved Minor Illusion", 2), ("Malleable Illusions", 6), ("Illusory Self", 10), ("Illusory Reality", 14)],
                Wizard.Subclasses.NECROMANCY: [("Necromancy Savant", 2), ("Grim Harvest", 2), ("Undead Thralls", 6), ("Inured to Undeath", 10), ("Command Undead", 14)],
                Wizard.Subclasses.TRANSMUTATION: [("Transmutation Savant", 2), ("Minor Alchemy", 2), ("Transmuter's Stone", 6), ("Shapechanger", 10), ("Master Transmuter", 14)]
            }[self]
    weapon_profs = [Weapons.DAGGER, Weapons.DART, Weapons.SLING, Weapons.QUARTERSTAFF, Weapons.LIGHT_CROSSBOW]
    saving_throw_profs = [Attributes.INT, Attributes.WIS]
    available_skill_profs = Options([Skills.ARCANA, Skills.HISTORY, Skills.INSIGHT, Skills.INVESTIGATION, Skills.MEDICINE, Skills.RELIGION], num_choices=2)
    weapons = [Options([Weapons.QUARTERSTAFF, Weapons.DAGGER])]
    gear = [Options([list(ArcaneFocus) + [Gear.COMPONENT_POUCH]]), Options([Packs.SCHOLAR, Packs.EXPLORER]), Options([Gear.SPELLBOOK])]
    traits = [("Spellcasting", 1), ("Arcane Recovery", 1), ("Spell Mastery", 18), ("Signature Spells", 20)]


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

class Background: #TODO most background need to be swapped to Options() syntax
    name: BackgroundName
    sub_backrounds: list[str]
    skill_profs: list[Skills]
    tool_profs: list[AllTools] #TODO Need this to accept Options() type
    languages: list[Languages] #TODO Need this to accept Options() type
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
    skill_profs = [Skills.INSIGHT, Skills.RELIGION]
    languages = [Options(list(Languages), num_choices=2)]
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

# skill_expertises = [item for item, count in collections.Counter(skill_profs).items() if count > 1] # I included this so if you get the same skill proficiency from two different sources, it becomes an expertise (it's pretty darn rare)
# tool_expertises = [item for item, count in collections.Counter(tool_profs).items() if count > 1] # You can delete these two rows if you don't want innate expertises

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

# print("Race:", race)
# if subrace != "N/A":
#     print("Subrace:", subrace)
# print("Class:", character_class)
# if subclass != "N/A":
#     print("Sub-Class:", subclass)
# if fighting_style != "N/A":
#     print("Fighting Style:", fighting_style)
# print("Level:", level)
# print("Alignment:", alignment)
# print("Background:", background)
# print("STR ", attr_str, " STRMOD: ", str_mod)
# print("DEX ", attr_dex, " DEXMOD: ", dex_mod)
# print("CON ", attr_con, " CONMOD: ", con_mod)
# print("INT ", attr_int, " INTMOD: ", int_mod)
# print("WIS ", attr_wis, " WISMOD: ", wis_mod)
# print("CHA ", attr_cha, " CHAMOD: ", cha_mod)
# print("Hit Points: ", hp)
# if race == "Dwarf":
#     print("Speed:", speed, "Feet (Your Speed is not Reduced by Wearing Heavy Armour)")
# else:
#     print("Speed:", speed, "Feet")
# if armour_profs != []:
#     print("Armour Proficiencies:", ", ".join(sorted(remove_duplicates(armour_profs))))
# if weapon_profs != []:
#     print("Weapon Proficienceis:", ", ".join(sorted(remove_duplicates(weapon_profs))))
# if tool_profs != []:
#     print("Tool Proficiencies:", ", ".join(sorted(remove_duplicates(tool_profs))))
# if tool_expertises != []:
#     print ("Tool Expertises: ", ", ".join(sorted(remove_duplicates(tool_expertises))))
# if saving_throw_profs != []:
#     print("Saving Throw Proficiencies:", ", ".join(sorted(remove_duplicates(saving_throw_profs))))
# if skill_profs != []:
#     print("Skill Proficiencies:", ", ".join(sorted(remove_duplicates(skill_profs))))
# if skill_expertises != []:
#     print ("Skill Expertises: ", ", ".join(sorted(remove_duplicates(skill_expertises))))
# if resistances != []:
#     print("Resistances:", ", ".join(sorted(remove_duplicates(resistances))))
# if immunities != []:
#     print("Immunities:", ", ".join(sorted(remove_duplicates(immunities))))
# if vulnerabilities != []:
#     print("Vulnerabilities:", ", ".join(sorted(remove_duplicates(vulnerabilities))))
# if traits != []:
#     print("Traits:", ", ".join(sorted(remove_duplicates(traits))))
# if equipment != []:
#     print("Equipment and Weapons:", ", ".join(sorted(remove_duplicates(equipment))))
# if age != "N/A":
#     print("Age:", age, "Years")
# else:
#     print("Age: N/A")
# print("Height: ", (height//12), "' ", height%12, '"', sep='')
# print("Weight:", weight, "Pounds")
# print("Eye Colour:", eyes)
# print("Skin Colour:", skin)
# print("Hair Colour:", hair)