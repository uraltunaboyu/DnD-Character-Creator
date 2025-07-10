import enum
from typing import Any

from common import *
from choices import Choice, ChoiceUnit

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

class Race:
    name: RaceName
    subraces: list[Any] # TODO should make the way we deal with subraces match subclasses
    stat_increases: list[ChoiceUnit[tuple[Attributes, int]]] = []
    age_range: tuple[int, int]
    base_height: int # Number in inches, written as {feet}*12 + {inches} for ease of visibility. Ex. 6'8" -> 6*12 + 8
    base_weight: int # Number in lbs
    height_mod_range: tuple[int, int]
    weight_range: tuple[int, int]
    speed: int
    size: Sizes
    eyes: list[str]
    skin: list[str]
    hair: list[str]
    resistances: list[DamageType] = []
    immunities: list[DamageType] = []
    vulnerabilities: list[DamageType] = []
    skill_profs: list[ChoiceUnit[Skills]] = []
    tool_profs: list[ChoiceUnit[AllTools]] = []
    armour_profs: list[ChoiceUnit[ArmourTypes]] = []
    weapon_profs: list[ChoiceUnit[WeaponTypes | Weapons]] = []
    traits: list[AllTraits | str | tuple[str, int]]
    languages: list[ChoiceUnit[AllLanguages]] = []

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
    base_height = 
    base_weight = 
    height_mod_range = ()
    weight_range = ()
    speed = 30
    size = Sizes.
    eyes = []
    skin = []
    hair = []
    resistances = []
    immunities = []
    vulnerabilities = []
    skill_profs = []
    tool_profs = []
    armour_profs = []
    weapon_profs = []
    traits = []
    languages = []
    
    def apply_subrace(self, subrace: Any):
        if subrace == :
            self.
'''

class Dwarf(Race):
    name = RaceName.DWARF
    class Subrace(enum.StrEnum):
        HILL = "Hill"
        MOUNTAIN = "Mountain"
    subraces = list(Subrace)
    stat_increases = [
        (Attributes.CON, 2)
    ]
    age_range = (30, 320)
    height_mod_range = (2, 8)
    weight_range = (2, 12)
    speed = 25
    size = Sizes.MEDIUM
    eyes = ["Brown", "Hazel", "Green"]
    skin = ["White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown",\
            "Dark Brown", "Very Dark Brown/Black"]
    hair = ["Bald", "Brown", "Black", "Blond", "Red"]
    resistances = [DamageType.POISON]
    tool_profs = [Choice([ArtisanTools.SMITH, ArtisanTools.BREWER, ArtisanTools.MASON])]
    weapon_profs = [Weapons.BATTLEAXE, Weapons.HANDAXE, Weapons.LIGHT_HAMMER, Weapons.WARHAMMER]
    traits = [Traits.DWARVEN_RESILIENCE, Traits.STONECUNNING, Traits.DARKVISION60]
    languages = [Languages.COMMON, Languages.DWARVISH]
    
    def apply_subrace(self, subrace: Any):
        if subrace == Dwarf.Subrace.HILL:
            self.stat_increases.append((Attributes.WIS, 1))
            self.base_height = 3*12 + 8
            self.base_weight = 115
            self.traits.append(Traits.DWARVEN_TOUGHNESS)
            # TODO add a hill dwarf check to the character for max hp (+1 per level)
        if subrace == Dwarf.Subrace.MOUNTAIN:
            self.stat_increases.append((Attributes.STR, 2))
            self.base_height = 4*12
            self.base_weight = 130
            self.armour_profs.extend([ArmourTypes.LIGHT, ArmourTypes.MEDIUM])

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
    age_range = (20, 700)
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
            self.weapon_profs.extend([Weapons.RAPIER, Weapons.SHORTSWORD, Weapons.HAND_CROSSBOW])
            self.traits.remove(Traits.DARKVISION60)
            self.traits.extend([Traits.DARKVISION120, Traits.DROW_MAGIC, Traits.SUNLIGHT_SENSITIVITY])
            self.base_height = 4*12 + 5
            self.base_weight = 75
            self.height_mod_range = (2, 12)
            self.weight_range = (1, 6)
        elif subrace == Elf.Subrace.HIGH:
            self.stat_increases.append((Attributes.INT, 1))
            self.weapon_profs.extend([Weapons.LONGSWORD, Weapons.SHORTSWORD, Weapons.SHORTBOW, Weapons.LONGBOW])
            self.traits.extend([Traits.CANTRIP])
            self.languages.append(Choice(list(Languages)))
            self.base_height = 4*12 + 6
            self.base_weight = 90
            self.height_mod_range = (2, 20)
            self.weight_range = (1, 4)
        elif subrace == Elf.Subrace.WOOD:
            self.stat_increases.append((Attributes.WIS, 1))
            self.traits.extend([Traits.MASK_OF_THE_WILD])
            self.weapon_profs.extend([Weapons.LONGSWORD, Weapons.SHORTSWORD, Weapons.SHORTBOW, Weapons.LONGBOW])
            self.speed = 35
            self.base_height = 4*12 + 6
            self.base_weight = 100
            self.height_mod_range = (2, 20)
            self.weight_range = (1, 4)

class Halfling(Race):
    name = RaceName.HALFLING
    class Subrace(enum.StrEnum):
        LIGHTFOOT = "Lightfoot"
        STOUT = "Stout"
    subraces = list(Subrace)
    stat_increases = [
        (Attributes.DEX, 2)
    ]
    age_range = (15, 200)
    base_height = 2*12 + 7
    base_weight = 35
    height_mod_range = (2, 8)
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

class Human(Race):
    name = RaceName.HUMAN
    class Subrace(enum.StrEnum):
        NORMAL = "Normal"
        VARIANT = "Variant"
    subraces = list(Subrace)
    age_range = (20, 60)
    base_height = 4*12 + 8
    base_weight = 110
    height_mod_range = (2, 20)
    weight_range = (2, 8)
    speed = 30
    size = Sizes.MEDIUM
    eyes = ["Brown", "Hazel", "Blue", "Green", "Grey", "Amber"]
    skin = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black"]
    hair = ["Black", "Brown", "Blonde", "Red", "White"]
    languages = [Languages.COMMON, Choice(list(Languages))]
    
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
            self.stat_increases.append(Choice([
                (Attributes.STR, 1),
                (Attributes.DEX, 1),
                (Attributes.CON, 1),
                (Attributes.INT, 1),
                (Attributes.WIS, 1),
                (Attributes.CHA, 1)
            ], 2))
            self.skill_profs.append(Choice(list(Skills)))
            self.traits.append(Traits.FEAT)

class Dragonborn(Race):
    name = RaceName.DRAGONBORN
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
    base_height = 5*12 + 6
    base_weight = 175
    height_mod_range = (2, 16)
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
    base_height = 2*12 + 11
    base_weight = 35
    height_mod_range = (2, 8)
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
            self.tool_profs.append(ArtisanTools.TINKER)

class HalfElf(Race):
    name = RaceName.HALF_ELF
    class Subrace(enum.StrEnum):
        DROW = "Drow"
        HIGH = "High"
        WOOD = "Wood"
    subraces = list(Subrace)
    stat_increases = [
        (Attributes.CHA, 2),
        Choice([
                (Attributes.STR, 1),
                (Attributes.DEX, 1),
                (Attributes.CON, 1),
                (Attributes.INT, 1),
                (Attributes.WIS, 1)
            ], 2)
    ] # TODO Double check that this is cool & good
    age_range = (20, 160)
    base_height = 4*12 + 9
    base_weight = 110
    height_mod_range = (2, 16)
    weight_range = (2, 8)
    speed = 30
    size = Sizes.MEDIUM
    eyes = ["Blue", "Violet", "Green"]
    skin = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown"]
    hair = ["Red", "Blond", "Brown", "Black"]
    skill_profs = [Choice(list(Skills), 2)]
    traits = [Traits.DARKVISION60, Traits.FEY_ANCESTRY]
    languages = [Languages.COMMON, Languages.ELVISH, Choice(list(Languages))]

class HalfOrc(Race):
    name = RaceName.HALF_ORC
    stat_increases = [
        (Attributes.STR, 2),
        (Attributes.CON, 1)
    ]
    age_range = (14, 60)
    base_height = 4*12 + 10
    base_weight = 140
    height_mod_range = (2, 20)
    weight_range = (2, 12)
    speed = 30
    size = Sizes.MEDIUM
    eyes = ["Reddish Brown", "Reddish Blue", "Reddish Green", "Reddish Grey"]
    skin = ["Greyish Green"]
    hair = ["Dark Brown", "Bald", "Red"]
    traits = [Traits.DARKVISION60, Traits.RELENTLESS_ENDURANCE, Traits.SAVAGE_ATTACKS]
    skill_profs = [Skills.INTIMIDATION]
    languages = [Languages.COMMON, Languages.ORC]

class Tiefling(Race):
    name = RaceName.TIEFLING
    stat_increases = [
        (Attributes.CHA, 2),
        (Attributes.INT, 1)
    ]
    age_range = (20, 60)
    base_height = 4*12 + 9
    base_weight = 110
    height_mod_range = (2, 16)
    weight_range = (2, 8)
    speed = 30
    size = Sizes.MEDIUM
    eyes = ["Solid Orbs of Red", "Solid Orbs of Black", "Solid Orbs of White", "Solid Orbs of Silver", "Solid Orbs of Gold"]
    skin = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black", "Light Red", "Maroon", "Burgundy", "Dark Red", "Red"]
    hair = ["Red", "Brown", "Black", "Dark Blue", "Purple"]
    resistances = [DamageType.FIRE]
    traits = [Traits.DARKVISION60, Traits.INFERNAL_LEGACY]
    languages = [Languages.COMMON, ExoticLanguages.INFERNAL]