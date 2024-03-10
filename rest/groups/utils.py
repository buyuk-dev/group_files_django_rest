from collections import defaultdict


def group_files(files:'list[str]', delimiters:str = "") -> 'dict[str, list[str]]':
    """
    Placeholder for goruping algorithm.
    """
    grouped_files = defaultdict(list)

    for path in files:
        key = path[0] if not delimiters else path.split(delimiters[0])[0]
        grouped_files[key] = path

    return grouped_files
