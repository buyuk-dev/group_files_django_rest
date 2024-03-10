from collections import defaultdict
import re
from typing import Optional

from .defaults import DELIMITERS


def unify_delimiters(string, delimiters=None):
    delimiters = delimiters or DELIMITERS
    pattern = f"[{re.escape(delimiters)}]"
    return re.sub(pattern, re.escape(delimiters[0]), string)


def calculate_common_prefix(s1, s2, delimiter):
    prefix = []
    for a, b in zip(s1.split(delimiter), s2.split(delimiter)):
        if a == b:
            prefix.append(a)
        else:
            break
    return len(prefix), delimiter.join(prefix)


def group_strings(strings, delimiters=None):
    delimiters = delimiters or DELIMITERS

    groups = []
    if len(strings) == 0: return groups

    # Unify delimiters within strings.
    unified = list(set(unify_delimiters(s) for s in strings))
    delimiter = delimiters[0]

    # Sort to build optimal groups.
    unified.sort()

    # Initialize current group with first item on the list.
    first, strings = unified[0], unified[1:]
    current_group_strings, current_group_name = [first], first
    current_prefix_length = current_group_name.count(delimiter) + 1

    while len(strings) > 0:
        first, strings = strings[0], strings[1:]
    
        # should add first to current group or create new one?
        common_prefix_length, common_prefix = calculate_common_prefix(first, current_group_name, delimiter)

        # add if common prefix length between first and current_group_name is greater than 50%
        if common_prefix_length > 0.5 * current_prefix_length:
            current_group_strings.append(first)
            current_group_name = common_prefix
            current_prefix_length = common_prefix_length

        # otherwise append current group to solution and create new group.
        else:
            groups.append({
                current_group_name: current_group_strings
            })
            current_group_strings = [first]
            current_group_name = first
            current_prefix_length = current_group_name.count(delimiter) + 1

    return groups


if __name__ == '__main__':
    strings = None
    with open("C:\\Users\\buyuk\\Downloads\\names.csv") as data_file:
        strings  = [line.strip() for line in data_file]

    from pprint import pprint
    groups = group_strings(strings, "_")
    for group in groups:
        pprint(group)
