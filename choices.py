from random import sample
from typing import Generic, TypeVar

T = TypeVar('T')

class Options(Generic[T]):
    def __init__(self, choices: list[T], num_choices: int, priors: list[T] = []):
        self.priors = priors
        self.choices = [choice for choice in choices if choice not in priors]
        self.num_choices = num_choices
    
    """Helper to create a choice for one item"""
    @classmethod
    def one_of(cls, items: list[T], priors: list[T] = []):
        return cls(items, 1, priors)
    
def _interactive_resolve(options: Options) -> list[T]:
    def validate_input(input: str, max_val: int) -> list | None:
        numbers = input.replace(" ", "").split(",")
        res = []
        for n in numbers:
            try:
                val = int(n)
                if val > max_val or val <= 0:
                    raise ValueError
                res.append(int(n))
            except ValueError:
                print(f"{n} is not a valid input!")
                return None
        return res
    picks: list[T] = []
    remaining_num_choices = options.num_choices
    choices = options.choices
    while remaining_num_choices > 0:
        print(f"Choose {remaining_num_choices} from:")
        for i, choice in enumerate(choices):
            print(f"{i + 1}. {choice}")
        user_input = validate_input(input(\
            "Enter a comma separated list of numbers: "\
              if remaining_num_choices > 1 else\
              "Enter a number:"), len(choices))
        if user_input is None: continue
        remaining_choices = []
        for i, choice in enumerate(choices):
            if i + 1 in user_input:
                picks.append(choice)
            else:
                remaining_choices.append(choice)
        choices = remaining_choices
        remaining_num_choices -= len(user_input)
    return picks

def resolve(options: Options | list[Options], interactive = False) -> list[T]:
    if isinstance(options, list):
        picks: list[T] = []
        for option in options:
            if interactive:
                picks.extend(_interactive_resolve(option))
            else:
                picks.extend(resolve(option))
    else:
        if interactive:
            return _interactive_resolve(options)
        picks = sample(options.choices, options.num_choices)
        picks.extend(options.priors)
    return picks

if __name__ == "__main__":
    all_langs = ["Common", "Elvish", "Orc", "Goblin", "Abyssal", "Celestial"]
    basic_weapons = ["Sword", "Bow", "Mace", "Dagger"]
    adv_weapons = ["Twohander", "Morningstar", "Crossbow", "Rapier"]
    stats = Options(["STR", "DEX", "CON", "INT", "WIS"], 2, ["CHA"])
    languages = Options(["Common", "Elvish", "Orc", "Goblin", "Abyssal"], 2, ["Common", "Elvish"])
    complex_options = [Options(basic_weapons, 2, ["Sword"]), Options.one_of(adv_weapons, ["Twohander", "Crossbow"])]
    print(resolve(stats))
    print(resolve(languages, interactive=True))
    print(resolve(complex_options))