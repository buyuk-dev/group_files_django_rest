MUL = [1, 10, 100, 1000]


def read_strings(filename):
    """
    """
    strings = None
    with open(filename) as data_file:
        strings  = [line.strip() for line in data_file]
    return strings


def generate(base_file_path:str, mul, strings):
    """
    """
    filename, extension = base_file_path.rsplit(".", maxsplit=1)
    with open(f"{filename}_{mul}.{extension}", "w") as data_file:
        for s in strings:
            for i in range(mul):
                line = f"{s}_{i}\n"
                data_file.write(line)


base_file_path = "C:\\Users\\buyuk\\Downloads\\names.csv"
strings = read_strings(base_file_path)
for m in MUL:
    generate(base_file_path, m, strings)
