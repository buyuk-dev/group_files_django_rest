import re
from .defaults import DELIMITERS


def unify_delimiters(string, delimiters=None):
    delimiters = delimiters or DELIMITERS
    pattern = f"[{''.join(re.escape(d) for d in delimiters)}]"
    return re.sub(pattern, delimiters[0], string)


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
    delimiter = delimiters[0]

    if not strings:
        return {}

    # Unify delimiters within strings and remove duplicates.
    unified = sorted(set(unify_delimiters(s, delimiters) for s in strings))

    groups = {}
    current_group_strings, current_group_name = [unified[0]], unified[0]
    current_prefix_length, _ = calculate_common_prefix(current_group_name, current_group_name, delimiter)

    for s in unified[1:]:
        common_prefix_length, common_prefix = calculate_common_prefix(s, current_group_name, delimiter)

        if common_prefix_length > 0.5 * current_prefix_length:
            current_group_strings.append(s)
            current_group_name = common_prefix
            current_prefix_length = common_prefix_length
        else:
            groups[current_group_name] = current_group_strings
            current_group_strings = [s]
            current_group_name = s
            current_prefix_length, _ = calculate_common_prefix(s, s, delimiter)

    # Don't forget to add the last group to groups
    if current_group_strings:
        groups[current_group_name] = current_group_strings

    return groups


if __name__ == '__main__':

    dataset = "C:\\Users\\buyuk\\Downloads\\names_dup_1000.csv"

    strings = None
    with open(dataset, 'r') as data_file:
        strings = [line.strip() for line in data_file]

    groups = group_strings(strings, "_")

    from pprint import pprint
    pprint(groups)