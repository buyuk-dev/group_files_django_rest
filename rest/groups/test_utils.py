import pytest
from .utils import group_strings


@pytest.mark.parametrize("dataset", [
    "C:\\Users\\buyuk\\Downloads\\names_dup_1.csv",
    "C:\\Users\\buyuk\\Downloads\\names_dup_10.csv",
    "C:\\Users\\buyuk\\Downloads\\names_dup_100.csv",
    "C:\\Users\\buyuk\\Downloads\\names_dup_1000.csv"
])
def test_example_dataset(dataset):
    strings = None
    with open(dataset, 'r') as data_file:
        strings = [line.strip() for line in data_file]

    groups = group_strings(strings, "_")

    grouped_strings = []
    for group, entries in groups.items():
        grouped_strings.extend(entries)

    # Print the difference between the original and grouped strings
    print(set(strings).difference(set(grouped_strings)))
    assert len(set(grouped_strings)) == len(set(strings))