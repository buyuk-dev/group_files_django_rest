from collections import defaultdict
import re
from typing import Optional

from .defaults import DELIMITERS


def get_split_pattern(delimiters=None):
    """
    Combine all delimiter characters into one regex pattern.
    """
    delimiters = delimiters or DELIMITERS

    # '+' to avoid empty groups when multiple delim in sequence.
    pattern = f"[{delimiters}]+"

    return pattern


def split_string(input_string, delimiters=None):
    """
    Split string on each of the delimiters.
    """
    delimiters = delimiters or DELIMITERS
    pattern = get_split_pattern(delimiters)

    # It is possible to get empty parts at the beginning and end
    # when string starts or ends with a sequence of delimiters.
    return filter(lambda x: len(x) > 0, re.split(pattern, input_string))


def vectorize_string(input_string, delimiters=None):
    """
    Assign unique integer to every unique part of the string.
    """
    pass


def compute_groups(strings, delimiters=None):
    """
    Groups strings from the input list into most descriptive groups by common prefixes.
    Returns dict where key is the group prefix and value is a list of strings in the group.
    """
    delimiters = delimiters or DELIMITERS
    groups = defaultdict(list)

    s: str
    for s in strings:
        prefix, _ = s.rsplit(delimiters[1], maxsplit=1)
        groups[prefix].append(s)

    return groups


def group_files(files:'list[str]', delimiters:'Optional[str]' = None) -> 'dict[str, list[str]]':
    """
    Placeholder for goruping algorithm.
    """
    return compute_groups(files, delimiters)
