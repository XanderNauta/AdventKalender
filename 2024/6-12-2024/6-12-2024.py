def count_rows_and_columns(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return [list(line) for line in content.splitlines()]

def write_grid_to_file(grid, file_path):
    with open(file_path, 'w') as file:
        for row in grid:
            file.write(''.join(row) + '\n')

def rotate_character(character):
    directions = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    return directions.get(character, character)

def get_direction(character):
    return {
        '^': "up",
        'v': "down",
        '<': "left",
        '>': "right"
    }.get(character, None)

def move_from_position(grid, start_row, start_col, direction, file_path):
    character = grid[start_row][start_col]

    if direction == "up":
        new_row, new_col = start_row - 1, start_col
    elif direction == "down":
        new_row, new_col = start_row + 1, start_col
    elif direction == "left":
        new_row, new_col = start_row, start_col - 1
    elif direction == "right":
        new_row, new_col = start_row, start_col + 1
    else:
        return start_row, start_col  # Geen geldige richting

    if grid[new_row][new_col] == "#":  # Obstakel
        grid[start_row][start_col] = rotate_character(character)  # Draai het karakter 90 graden
    else:
        grid[new_row][new_col] = character
        grid[start_row][start_col] = 'x'

    write_grid_to_file(grid, file_path)  # Sla wijzigingen op in het bestand
    return new_row, new_col

def loop_through(rows, characters, file_path):
    while True:
        for character in characters:
            location_hook = find_hook(rows, character)
            if location_hook is None:
                print(f"Karakter '{character}' niet gevonden. Overslaan.")
                continue
            direction = get_direction(character)
            if direction:
                move_from_position(rows, location_hook[0], location_hook[1], direction, file_path)

def find_hook(rows, character):
    for row_index, row in enumerate(rows):
        if character in row:
            col_index = row.index(character)
            return [row_index, col_index]
    return None  # Geen karakter gevonden

def count_character_in_file(file_path, character):
    with open(file_path, 'r') as file:
        content = file.read()
    # Count occurrences of the character in the file
    count = content.count(character)
    return count

# Bestand inlezen
file_path = './2024/6-12-2024/6-12-2024.txt'
data = count_rows_and_columns(file_path)
if data:
    loop_through(data, ["^", ">", "v", "<"], file_path)

x_count = count_character_in_file(file_path, 'x')

# print(f"Data (rows and columns): {data}")
print(f"Count of 'x': {x_count}")