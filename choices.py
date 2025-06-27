from dataclasses import dataclass
from itertools import chain
from random import sample
from typing import Generic, Iterable, List, TypeVar, Union

T = TypeVar('T')


class Options(Generic[T]):
    """Representation of a number of choices, and a list of given guarantees
    
    Attributes:
        choices     list of items to pick from
        priors      list of guaranteed items, default nothing
        num_choices number of choices from the choices list, default 1
    """
    def __init__(self, choices: list[T], priors: list[T] = [], num_choices: int = 1):
        self.priors = priors
        self.choices = [choice for choice in choices if choice not in priors]
        self.num_choices = num_choices

    
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
    if remaining_num_choices == len(choices):
        picks.extend(options.choices)
        return picks
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

def resolve_old(options: Options | list[Options], interactive = False) -> list[T]:
    def flatten(to_flatten: list) -> list:
        res = []
        for item in to_flatten:
            if isinstance(item, list):
                res.extend(flatten(item))
            else:
                res.append(item)
        return res
    picks: list[T] = []

    if isinstance(options, list):
        for option in options:
            picks.extend(resolve_old(option, interactive=interactive))
    else:
        for i, choice in enumerate(options.choices):
            if isinstance(choice, Options):
                options.choices[i] = resolve_old(choice, interactive=interactive)
        options.choices = flatten(options.choices)
        if interactive:
            return _interactive_resolve(options)
        picks.extend(sample(options.choices, options.num_choices))
        picks.extend(options.priors)
    return picks

ChoiceUnit = Union[T,  tuple[T], 'Choice[T]']

@dataclass
class Choice(Generic[T]):
    options: List[ChoiceUnit]
    count: int = 1

def resolve(items: List[ChoiceUnit]) -> List[T]:
    result: List[T] = []

    for item in items:
        if isinstance(item, Choice):
            if item.count >= len(item.options):
                chosen = item.options
            else:
                chosen = sample(item.options, item.count)
            result.extend(resolve(chosen))
        elif isinstance(item, tuple):
            result.extend(resolve(list(item)))
        else:
            result.append(item)

    return result

def resolve_no_duplicates(items: List[ChoiceUnit]) -> List[T]: # CANNOT HANDLE CHOICE OF CHOICES
    result: List[T] = []
    all_options: List = []
    picks: int = 0
    for item in items:
        if not isinstance(item, Choice):
            if item not in result:
                result.extend(item)
        else:
            all_options.extend(item.options)
            picks += item.count
    all_options = list(set(all_options))
    for thing in result:
        if thing in all_options:
            all_options.remove(thing)
    result.extend(sample(all_options, picks))
    
    return result

if __name__ == "__main__":
    a = "a"
    b = "b"
    c = "c"
    d = "d"
    e = "e"
    f = "f"
    
    tests: dict[str, list[ChoiceUnit]] = {
        "test_simple": [a], # pass [a]
        "test_easy": [a, b, a], # pass [a, b]
        "test_regular": [a, Choice([a, b, c, d, e, f], 3)], # pass [a, 3of(b,c,d,e,f)]
        "test_complex": [a, Choice([(b, c), d])], # pass [a, 1of[(b,c), d]]
        "test_googleplex": [a, Choice([b, Choice([c, d, e], 2)])], # pass [a, either{b, 2of(c,d,e)}]
        "test_mutually_exclusive": [a, Choice([b, c]), Choice([a, b]), Choice([f])] # pass [a, b, c, f]
    }
    funcs = [resolve, resolve_no_duplicates]

    for name, test in tests.items():
        print(f"Test: {name}")
        for func in funcs:
            if name == "test_googleplex" and func.__name__ == "resolve_no_duplicates": continue
            try:
                print(f"{func.__name__}: ", func(test))
            except:
                print(f"{func.__name__} failed on {name}!")
        print("====================================")