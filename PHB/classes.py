import enum
import random

from common import *
from choices import Choice, ChoiceUnit

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
    armour_profs: list[ChoiceUnit[ArmourTypes]] = []
    saving_throw_profs: list[ChoiceUnit[Attributes]] = []
    skill_profs: list[ChoiceUnit[Skills]] = []
    weapon_profs: list[ChoiceUnit[WeaponTypes | Weapons]] = []
    traits: list[tuple[str, int] | tuple[str, int, enum.StrEnum]] #TODO Ability score improvement not included in traits since it feels redundant to put it 5 times in every class (lvl 4,8,12,16,19)
    combat_gear: list[ChoiceUnit[CombatGear]] = []
    gear: list[ChoiceUnit[AllGear]] = []
    tool_profs: list[ChoiceUnit[AllTools]] = []

    hit_die = 0
    
    def __init__(self):
        pass

    def define_subclass(self):
        pass

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
    skill_profs = [Choice([Skills.ANIMAL_HANDLING, Skills.ATHLETICS, Skills.INTIMIDATION, Skills.NATURE, Skills.PERCEPTION, Skills.SURVIVAL], 2)]
    combat_gear = [Choice([Weapons.GREATAXE, Choice(list(MARTIAL_MELEE))]), Choice([(Weapons.HANDAXE, 2), Choice(list(WeaponTypes.SIMPLE_WEAPONS))]), (Weapons.JAVELIN, 4)]
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
    skill_profs = [Choice(list(Skills), 3)]
    tool_profs = [Choice(list(MusicalInstruments), 3)]
    combat_gear = [Choice([Weapons.RAPIER, Weapons.LONGSWORD, Choice(list(WeaponTypes.SIMPLE_WEAPONS))]), Weapons.DAGGER, Armours.LEATHER]
    gear = [Choice([Packs.DIPLOMAT, Packs.ENTERTAINER]), Choice([MusicalInstruments.LUTE, Choice(list(MusicalInstruments))])]
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
    skill_profs = [Choice([Skills.HISTORY, Skills.INSIGHT, Skills.MEDICINE, Skills.PERSUASION, Skills.RELIGION], 2)]
    combat_gear = [Choice([(Weapons.LIGHT_CROSSBOW, (Ammunition.BOLTS, 20)), Choice(list(WeaponTypes.SIMPLE_WEAPONS))]), Armours.SHIELD]
    gear = [Choice([Packs.PRIEST, Packs.EXPLORER]), Choice(list(HolySymbols))]
    
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
    skill_profs = [Choice([Skills.ANIMAL_HANDLING, Skills.ARCANA, Skills.INSIGHT, Skills.MEDICINE, Skills.NATURE, Skills.PERCEPTION, Skills.RELIGION, Skills.SURVIVAL], 2)]
    combat_gear = [Choice([Weapons.SCIMITAR, Choice(list(SIMPLE_MELEE))]), Choice([Choice(list(WeaponTypes.SIMPLE_WEAPONS)), Armours.SHIELD]), Armours.LEATHER]
    gear = [Packs.EXPLORER, Choice(list(DruidicFocus))]
    traits = [("Druidic", 1), ("Spellcasting", 1), ("Wild Shape", 2), ("Timeless Body", 18), ("Beast Spells", 18), ("Archdruid", 20)]

    def __init__(self): #TODO check if depreciated, if so, work it back into the thing somehow
        super().__init__()

    def define_subclass(self):
        super().define_subclass() # TODO: druid subclasses are weird
    
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
    skill_profs = [Choice([Skills.ACROBATICS, Skills.ANIMAL_HANDLING, Skills.ATHLETICS, Skills.HISTORY, Skills.INSIGHT, Skills.INTIMIDATION, Skills.PERCEPTION, Skills.SURVIVAL], 2)]
    combat_gear = [Choice([Armours.CHAIN_MAIL, (Armours.LEATHER, Weapons.LONGBOW, (Ammunition.ARROWS, 20))]), Choice([(Choice(list(WeaponTypes.MARTIAL_WEAPONS)), Armours.SHIELD), Choice(list(WeaponTypes.MARTIAL_WEAPONS), 2)]), Choice([(Weapons.LIGHT_CROSSBOW, (Ammunition.BOLTS, 20)), ([Weapons.HANDAXE]*2)])]
    gear = [Choice([Packs.DUNGEONEER, Packs.EXPLORER])]
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
    skill_profs = [Choice([Skills.ACROBATICS, Skills.ATHLETICS, Skills.HISTORY, Skills.INSIGHT, Skills.RELIGION, Skills.STEALTH], 2)]
    combat_gear = [Choice([Weapons.SHORTSWORD, Choice(list(WeaponTypes.SIMPLE_WEAPONS))]), (Weapons.DART, 10)] #TODO check if tuple[list[]] is legal, can always do InitialArray + [Dart]*10
    gear = [Choice([Packs.DUNGEONEER, Packs.EXPLORER])]
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
    skill_profs = [Choice([Skills.ATHLETICS, Skills.INSIGHT, Skills.INTIMIDATION, Skills.MEDICINE, Skills.PERSUASION, Skills.RELIGION], 2)]
    combat_gear = [Choice([(Choice(list(WeaponTypes.MARTIAL_WEAPONS)), Armours.SHIELD), Choice(list(WeaponTypes.MARTIAL_WEAPONS), 2)]),
                   Choice([(Weapons.JAVELIN, 5), Choice(list(SIMPLE_MELEE))]), Armours.CHAIN_MAIL]
    gear = [Choice([Packs.PRIEST, Packs.EXPLORER]), Choice(list(HolySymbols))]
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
    skill_profs = [Choice([Skills.ANIMAL_HANDLING, Skills.ATHLETICS, Skills.INSIGHT, Skills.INVESTIGATION, Skills.NATURE, Skills.PERCEPTION, Skills.STEALTH, Skills.SURVIVAL], 3)]
    combat_gear = [Choice([Armours.SCALE_MAIL, Armours.LEATHER]), Choice([([Weapons.SHORTSWORD]*2), Choice(list(SIMPLE_MELEE), 2)]), Weapons.LONGBOW, (Ammunition.ARROWS, 20)]
    gear = [Choice([Packs.DUNGEONEER, Packs.EXPLORER])]
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
    skill_profs = [Choice([Skills.ACROBATICS, Skills.ATHLETICS, Skills.DECEPTION, Skills.INSIGHT, Skills.INTIMIDATION, Skills.INVESTIGATION, Skills.PERCEPTION, Skills.PERFORMANCE, Skills.PERSUASION, Skills.SLEIGHT_OF_HAND, Skills.STEALTH], 4)]
    combat_gear = [Choice([Weapons.RAPIER, Weapons.SHORTSWORD]), Choice([(Weapons.SHORTBOW, (Ammunition.ARROWS, 20)), Weapons.SHORTSWORD]), Armours.LEATHER, (Weapons.DAGGER, 2)]
    gear = [Choice([Packs.BURGLAR, Packs.DUNGEONEER, Packs.EXPLORER]), Tools.THIEF]
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
    skill_profs = [Choice([Skills.ARCANA, Skills.DECEPTION, Skills.INSIGHT, Skills.INTIMIDATION, Skills.PERSUASION, Skills.RELIGION], 2)]
    combat_gear = [Choice([(Weapons.LIGHT_CROSSBOW, (Ammunition.BOLTS, 20)), Choice(list(WeaponTypes.SIMPLE_WEAPONS))]), (Weapons.DAGGER, 2)]
    gear = [Choice([Gear.COMPONENT_POUCH, Choice(list(ArcaneFocus))]), Choice([Packs.DUNGEONEER, Packs.EXPLORER])]
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
    skill_profs = [Choice([Skills.ARCANA, Skills.DECEPTION, Skills.HISTORY, Skills.INTIMIDATION, Skills.INVESTIGATION, Skills.NATURE, Skills.RELIGION], 2)]
    combat_gear = [Choice([(Weapons.LIGHT_CROSSBOW, (Ammunition.BOLTS, 20)), Choice(list(WeaponTypes.SIMPLE_WEAPONS))]), Armours.LEATHER, Choice(list(WeaponTypes.SIMPLE_WEAPONS)), (Weapons.DAGGER, 2)]
    gear = [Choice([Gear.COMPONENT_POUCH, Choice(list(ArcaneFocus))]), Choice([Packs.SCHOLAR, Packs.DUNGEONEER])]
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
    skill_profs = [Choice([Skills.ARCANA, Skills.HISTORY, Skills.INSIGHT, Skills.INVESTIGATION, Skills.MEDICINE, Skills.RELIGION], 2)]
    combat_gear = [Choice([Weapons.QUARTERSTAFF, Weapons.DAGGER])]
    gear = [Choice([Gear.COMPONENT_POUCH, Choice(list(ArcaneFocus))]), Choice([Packs.SCHOLAR, Packs.EXPLORER]), Gear.SPELLBOOK]
    traits = [("Spellcasting", 1), ("Arcane Recovery", 1), ("Spell Mastery", 18), ("Signature Spells", 20)]