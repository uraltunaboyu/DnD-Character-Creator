import enum

class DamageType(enum.StrEnum): # TODO organize classes alphabetically(?) or by group/type(?)
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
    PURSE = "Purse"
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

MARTIAL_RANGED: list[CombatGear] = [Weapons.BLOWGUN, Weapons.HAND_CROSSBOW, Weapons.HEAVY_CROSSBOW,\
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
    DWARVEN_TOUGHNESS = "Dwarven Toughness"
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
    STONECUNNING = "Stonecunning"
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