MUL = [1, 10, 100, 1000]


def read_strings(filename):
    """
    Read dataset from input file.
    """
    strings = None
    with open(filename) as data_file:
        strings  = [line.strip() for line in data_file]
    return strings


def generate(base_file_path:str, mul, strings):
    """
    Create new file and write mul copies of each input string into it with index suffix.
    """
    filename, extension = base_file_path.rsplit(".", maxsplit=1)
    with open(f"{filename}_{mul}.{extension}", "w") as data_file:
        for s in strings:
            for i in range(mul):
                line = f"{s}_{i}\n"
                data_file.write(line)


base_file_path = "datasets/names.csv"
strings = read_strings(base_file_path)
for m in MUL:
    generate(base_file_path, m, strings)
