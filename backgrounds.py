import enum

from typing import Any

from common import *
from choices import Choice, ChoiceUnit

class BackgroundName(enum.StrEnum):
    ACOLYTE = "Acolyte"
    CHARLATAN = "Charlatan"
    CRIMINAL = "Criminal"
    ENTERTAINER = "Entertainer"
    FOLK_HERO = "Folk Hero"
    GUILD_ARTISAN = "Guild Artisan"
    HERMIT = "Hermit"
    NOBLE = "Noble"
    OUTLANDER = "Outlander"
    SAGE = "Sage"
    SAILOR = "Sailor"
    SOLDIER = "Soldier"
    URCHIN = "Urchin"

class Background:
    name: BackgroundName
    sub_backrounds: list[str] = []
    skill_profs: list[Skills] = []
    tool_profs: list[ChoiceUnit[AllTools]] = []
    armour_profs: list[ChoiceUnit[ArmourTypes]] = []
    weapon_profs: list[ChoiceUnit[WeaponTypes | Weapons]] = []
    traits: list[AllTraits | str | tuple[str, int]] = []
    languages: list[ChoiceUnit[AllLanguages]] = []
    combat_gear: list[ChoiceUnit[CombatGear]] = []
    gear: list[ChoiceUnit[AllGear] | str] = [] # TODO either write up more gear in the common_defs or allow strings
    gp: int


    def apply_subbackground(self, subbackground: Any):
        pass

    def __init__(self, level: int, interactive: bool):
        pass

class Acolyte(Background):
    name = BackgroundName.ACOLYTE
    skill_profs = [Skills.INSIGHT, Skills.RELIGION]
    languages = [Choice(list(Languages), 2)]
    traits = [BackgroundTrait.SHELTER_OF_THE_FAITHFUL]
    gear = [Choice(list(HolySymbols)), Gear.CLOTHES_COMMON, Gear.POUCH] # Choice(["Prayer Book", "Prayer Wheel"]), Stick of incense*5, vestments
    gp = 15

class Charlatan(Background):
    name = BackgroundName.CHARLATAN
    skill_profs = [Skills.DECEPTION, Skills.SLEIGHT_OF_HAND]
    tool_profs = [Tools.DISGUISE, Tools.FORGERY]
    traits = [BackgroundTrait.FALSE_IDENTITY]
    gear = [Gear.CLOTHES_FINE, Tools.DISGUISE, Gear.POUCH] # Choice(["Ten Stoppered Bottles Filled with Coloured Liquid", "Set of Weighted Dice", "Deck of Marked Cards", "Signet Ring of an Imaginary Duke"])
    gp = 15 

class Criminal(Background):
    name = BackgroundName.CRIMINAL
    sub_backrounds = ["Blackmailer", "Burglar", "Enforcer", "Fence", "Highway Robber", "Hired Killer", "Pickpocket",
                       "Smuggler", "Spy"] # TODO make it so subbackground gets added to display name for Background. Ex. Criminal Fence or Criminal (Fence)
    skill_profs = [Skills.DECEPTION, Skills.STEALTH]
    tool_profs = [Choice(list(GamingSets)), Tools.THIEF]
    traits = [BackgroundTrait.CRIMINAL_CONTACT]
    gear = [Gear.CROWBAR, Gear.CLOTHES_COMMON, Gear.POUCH]
    gp = 15
       
class Entertainer(Background):
    name = BackgroundName.ENTERTAINER
    sub_backrounds = ["Actor", "Dancer", "Fire-Eater", "Gladiator", "Jester", "Juggler", "Instrumentalist",
                      "Poet", "Singer", "Storyteller", "Tumbler"] # TODO every entertainer gets 1-3 routines they're good at
    skill_profs = [Skills.ACROBATICS, Skills.PERFORMANCE]
    tool_profs = [Tools.DISGUISE, Choice(list(MusicalInstruments))]
    traits = [BackgroundTrait.BY_POPULAR_DEMAND]
    gear = [Gear.CLOTHES_COSTUME, Gear.POUCH] # TODO Whichver musical instrument proficiency picks
    gp = 15 # random.choice(["Love Letter from an Admirer", "Lock of Hair from an Admirer", "Trinket from an Admirer"])
  
class FolkHero(Background):
    name = BackgroundName.FOLK_HERO
    skill_profs = [Skills.ANIMAL_HANDLING, Skills.SURVIVAL]
    tool_profs = [Choice(list(ArtisanTools)), Tools.LAND_VEHICLES]
    traits = [BackgroundTrait.RUSTIC_HOSPITALITY]
    gear = [Gear.SHOVEL, Gear.POT, Gear.CLOTHES_COMMON, Gear.POUCH] # TODO Proficient artisan tool
    gp = 10

class GuildArtisan(Background):
    name = BackgroundName.GUILD_ARTISAN
    sub_backrounds = ["Alchemists, Apothecaries", "Armorours, Locksmiths, Finesmiths", "Brewers, Distillers, Vintners", "Calligraphers, Scribes, Scriveners",
                      "Carpenters, Roofers, Pasterers", "Cobblers, Shoemakers", "Cooks, Bakers", "Glassblowers, Glaziers", "Jewelers, Gemcutters",
                      "Leatherworkers, Skinners, Tanners", "Masons, Stonecutters", "Painters, Limners, Sign-Makers", "Potters, Tile-Makers", "Merchants",
                      "Shipwrights, Sailmakers", "Smiths, Metal-Forgers", "Tinkers, Pewterers, Casters", "Weavers, Dryers", "Woodcarvers, Coopers, Bowyers"]
    skill_profs = [Skills.INSIGHT, Skills.PERSUASION]
    tool_profs = [Choice(list(ArtisanTools))]
    traits = [BackgroundTrait.GUILD_MEMBERSHIP]
    gear = [Gear.CLOTHES_TRAVELER, Gear.POUCH] # TODO proficient artisan tool
    gp = 15 # Letter of Introduction from your guild
    # TODO If Merchant: no artisan tools, instead either language or navigator's tools. Also Mule & Cart instead of artisan tool for gear

class Hermit(Background):
    name = BackgroundName.HERMIT
    skill_profs = [Skills.MEDICINE, Skills.RELIGION]
    tool_profs = [Tools.HERBALIST]
    languages = [Choice(list(Languages))]
    gear = [Gear.BLANKET, Gear.CLOTHES_COMMON, Tools.HERBALIST]
    gp = 5 # "Scroll Case Stuffed Full of Notes from Your " + random.choice(["Prayers", "Studies"])

class Noble(Background):
    name = BackgroundName.NOBLE
    class SubBackground(enum.StrEnum):
        ARISTOCRAT = "Aristocrat"
        KNIGHT = "Knight"
    sub_backrounds = ["Aristocrat", "Knight"]
    skill_profs = [Skills.HISTORY, Skills.PERSUASION]
    tool_profs = [Choice(list(GamingSets))]
    languages = [Choice(list(Languages))]
    gear = [Gear.CLOTHES_FINE, Gear.SIGNET_RING, Gear.PURSE]
    gp = 25 # ["Scroll of Pedigree"]

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
    tool_profs = [Choice(list(MusicalInstruments))]
    languages = [Choice(list(Languages))]
    traits = [BackgroundTrait.WANDERER]
    gear = [Choice([ArcaneFocus.STAFF, DruidicFocus.WOODEN_STAFF]), Gear.HUNTING_TRAP, Gear.CLOTHES_TRAVELER, Gear.POUCH] 
    gp = 10 #["Trophy from an Animal You Killed"]

class Sage(Background):
    name = BackgroundName.SAGE
    sub_backgrounds = ["Alchemist", "Astronomer", "Discredited Academic", "Librarian", "Professor",
                       "Researcher", "Wizard's Apprentice", "Scribe"]
    skill_profs = [Skills.ARCANA, Skills.HISTORY]
    languages = [Choice(list(Languages), 2)]
    traits = [BackgroundTrait.RESEARCHER]
    gear = [Gear.INK, Gear.INK_PEN, Gear.CLOTHES_COMMON, Gear.POUCH]
    combat_gear = [Weapons.DAGGER]
    gp = 10 #["Letter from a Dead Colleague Posing a Question You Cannot yet Answer"]

class Sailor(Background):
    name = BackgroundName.SAILOR
    class SubBackground(enum.StrEnum):
        SAILOR = "Sailor"
        PIRATE = "Pirate"
    sub_backgrounds = ["Sailor", "Pirate"]
    skill_profs = [Skills.ATHLETICS, Skills.PERCEPTION]
    tool_profs = [Tools.NAVIGATOR, Tools.WATER_VEHICLES]
    gear = [Gear.ROPE_SILK, Gear.CLOTHES_COMMON, Gear.POUCH] #["Lucky Charm (Trinket)"]
    combat_gear = [Weapons.CLUB]
    gp = 10

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
    tool_profs = [Choice(list(GamingSets)), Tools.LAND_VEHICLES]
    traits = [BackgroundTrait.MILITARY_RANK]
    gear = [Choice([GamingSets.DICE, GamingSets.PLAYING_CARDS]), Gear.CLOTHES_COMMON, Gear.POUCH]
    gp = 10 # ["Insignia of Rank", "Trophy Taken from a Fallen Enemy"

class Urchin(Background):
    name = BackgroundName.URCHIN
    skill_profs = [Skills.SLEIGHT_OF_HAND, Skills.STEALTH]
    tool_profs = [Tools.DISGUISE, Tools.THIEF]
    traits = [BackgroundTrait.CITY_SECRETS]
    gear = [Gear.CLOTHES_COMMON] 
    combat_gear = [Weapons.DAGGER]
    gp = 10 #["Map of Your Home City", "Pet Mouse", "Token to Remember Your Parents"]

all_backgrounds: dict[BackgroundName, type[Background]] = {
    BackgroundName.ACOLYTE: Acolyte,
    BackgroundName.CHARLATAN: Charlatan,
    BackgroundName.CRIMINAL: Criminal,
    BackgroundName.ENTERTAINER: Entertainer,
    BackgroundName.FOLK_HERO: FolkHero,
    BackgroundName.GUILD_ARTISAN: GuildArtisan,
    BackgroundName.HERMIT: Hermit,
    BackgroundName.NOBLE: Noble,
    BackgroundName.OUTLANDER: Outlander,
    BackgroundName.SAGE: Sage,
    BackgroundName.SAILOR: Sailor,
    BackgroundName.SOLDIER: Soldier,
    BackgroundName.URCHIN: Urchin
}
