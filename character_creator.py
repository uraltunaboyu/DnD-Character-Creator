"""
Originally created on Tuesday April 30, 2019 | Major overhaul on July 7, 2025

@authors: maxbotsis & uraltunaboyu
"""

# =============================================================================
# This script is allows for the creation of a random character from the (Legacy) D&D 5e Player's Handbook
# It should print a nicely formatted series of lines that include all features of character creation at a given level
# Not all Skin/Hair/Eye colours may be correct, I just put some in quickly. Adjust as you like
#
# Known Gaps in the character creator:
#
# 1) Does not account for the level 4, 8, 12, and 16 ability score increases or feat choices if making a higher level character -> May be fixed with the overhaul
# 2) Does not account for Personality Traits, Ideals, or Bonds because that would make the script too bulky (bulkier than it already is)
# 3) In a non-interactive generation AND only for proficiencies, the script will combine various Choice() objects together before picking to help prevent duplicate
# and wasted picks. However, this is not completely accurate to the rules.
# Ex. Athletics guaranteed + 1-of-[Athletics, Acrobatics] + 1-of-[Acrobatics, Stealth, Deception] could yield [Athletics, Stealth, Deception]
# This method prevents the first pick from being wasted if the second happened upon acrobatics, but allows the above example against the rules
# For my purposes, this is fine since time cost to design an algorithm to perfectly match the rules is beyond the benefit of the accuracy.
# 
# TODO:
# Bringing it all together in the Character class
# Allow for different modules to be loaded in so you could generate a character with (as an example) PHB + Volo's Guide as potential options
# =============================================================================

import collections # May not be needed anymore
import enum # May not be needed here
import random # May not be needed here
from typing import Any # May not be needed here

from choices import resolve, Choice, ChoiceUnit
from common import *

from PHB.backgrounds import *
from PHB.classes import *
from PHB.races import *

# def normal(min:int, max:int) -> int: # Not exactly sure how this one is working, but it gives a more realistic result for age, height and weight
#     r: int = round(random.triangular(low = min, high = max))# Round gives us a whole number for a character's age
#     return r

# def hitpoints(max_dice:int) -> int:
#     n: int = 1
#     hitpoints: int = 0
    
#     if level == 1:
#         hitpoints = max_dice + con_mod
#         if hitpoints <= max_dice:  # This makes it so that the minimum HP is your HP die but you can start stronger if it "rolls well"
#             hitpoints = max_dice
#         return hitpoints
#     else:
#         hitpoints = max_dice + level * con_mod
#         while n < level:
#             hitpoints = hitpoints + random.randint(1, max_dice)
#             n = n + 1
#     if hitpoints <= max_dice + (level - 1):  # This makes it so the minimum HP increase is 1, I don't like to play with weakening characters
#         hitpoints = max_dice + (level - 1)
#     return hitpoints

# def stat_increase(stat:int, num_increase:int) -> int:
#     if stat <= 20 - num_increase:
#         stat = stat + num_increase
#     else:
#         stat = 20
#     return stat
        
# def stat_decrease(stat:int, num_decrease:int) -> int:
#     if stat >= 1 + num_decrease:
#         stat = stat - num_decrease
#     else:
#         stat = 1
#     return stat
        
# def stat_mod(stat:int) -> int:
#     return (stat - 10) // 2
    
# def remove_duplicates(input:list[str]) -> list[str]:
#     return list(set(input))

# level = 3  # This is where you change Character Level

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