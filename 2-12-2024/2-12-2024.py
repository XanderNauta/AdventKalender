def getList(file_path):
    with open(file_path, 'r') as bestand:
        return [list(map(int, line.split())) for line in bestand]

def is_strictly_increasing(line):
    return all(line[i] < line[i + 1] for i in range(len(line) - 1))

def is_strictly_decreasing(line):
    return all(line[i] > line[i + 1] for i in range(len(line) - 1))

def has_valid_steps(line):
    return all(1 <= abs(line[i] - line[i + 1]) <= 3 for i in range(len(line) - 1))

if __name__ == "__main__":
    file_path = './2-12-2024/2-12-2024.txt'
    data_list = getList(file_path)
    valid_lines = []
    invalid_lines = []

    for line in data_list:
        is_increasing = is_strictly_increasing(line)
        is_decreasing = is_strictly_decreasing(line)
        if (is_increasing or is_decreasing) and has_valid_steps(line):
            valid_lines.append(line)
        else:
            invalid_lines.append(line)

    print(valid_lines)
    print(f"Valid lines count: {len(valid_lines)}")
    print(f"Invalid lines count: {len(invalid_lines)}")
    print(f"Total lines processed: {len(valid_lines) + len(invalid_lines)}")
