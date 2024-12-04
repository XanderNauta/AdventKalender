# Input data as a grid of characters
def get_data():
    with open("./2024/4-12-2024/4-12-2024.txt", 'r') as bestand:
            data = [line.strip() for line in bestand.readlines()]    
    return data

grid = get_data()

# Patterns to search for
patterns = ["XMAS", "SAMX"]

# Function to search for patterns in a string
def find_patterns_in_line(line, patterns):
    positions = []
    for pattern in patterns:
        start = 0
        while (pos := line.find(pattern, start)) != -1:
            positions.append((pos, pattern))
            start = pos + 1  # Move past the last found position
    return positions

# Horizontal search
horizontal_matches = []
for row_idx, line in enumerate(grid):
    matches = find_patterns_in_line(line, patterns)
    for pos, pattern in matches:
        horizontal_matches.append((row_idx, pos, pattern))

# Vertical search
vertical_matches = []
columns = len(grid[0])
for col_idx in range(columns):
    col_string = "".join(row[col_idx] for row in grid)
    matches = find_patterns_in_line(col_string, patterns)
    for pos, pattern in matches:
        vertical_matches.append((pos, col_idx, pattern))

# Diagonal search (top-left to bottom-right and top-right to bottom-left)
def get_diagonals(grid, direction="ltr"):
    diagonals = []
    rows, cols = len(grid), len(grid[0])
    for d in range(-(rows - 1), cols):  # Diagonal indices
        diagonal = []
        for row in range(rows):
            col = row + d if direction == "ltr" else (cols - 1 - row + d)
            if 0 <= col < cols:
                diagonal.append(grid[row][col])
        diagonals.append("".join(diagonal))
    return diagonals

# Search diagonals for matches
diagonal_matches = []
diagonals_ltr = get_diagonals(grid, "ltr")
diagonals_rtl = get_diagonals(grid, "rtl")

# Process diagonals and note their position
for diag_idx, diag in enumerate(diagonals_ltr):
    matches = find_patterns_in_line(diag, patterns)
    for pos, pattern in matches:
        diagonal_matches.append(("ltr", diag_idx, pos, pattern))

for diag_idx, diag in enumerate(diagonals_rtl):
    matches = find_patterns_in_line(diag, patterns)
    for pos, pattern in matches:
        diagonal_matches.append(("rtl", diag_idx, pos, pattern))

print(len(horizontal_matches) + len(vertical_matches) + len(diagonal_matches))