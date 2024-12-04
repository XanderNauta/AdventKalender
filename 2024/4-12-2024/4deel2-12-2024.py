def count_xmas(word_search):
    rows = len(word_search)
    cols = len(word_search[0])
    xmas_count = 0

    # Traverse through the grid, ignoring the border as we need space for the X pattern
    for r in range(1, rows - 1):  # We start from row 1 because the X needs space
        for c in range(1, cols - 1):  # Same for columns, starting at index 1
            # Check if the center is 'A' and the surrounding cells form a valid "X-MAS"
            if word_search[r][c] == 'A':
                # Check the four diagonals for 'M'
                if (word_search[r-1][c-1] == 'M' and  # Top-left
                    word_search[r-1][c+1] == 'M' and  # Top-right
                    word_search[r+1][c-1] == 'S' and  # Bottom-left
                    word_search[r+1][c+1] == 'S') or (word_search[r-1][c-1] == 'S' and  # Top-left
                    word_search[r-1][c+1] == 'S' and  # Top-right
                    word_search[r+1][c-1] == 'M' and  # Bottom-left
                    word_search[r+1][c+1] == 'M')or (word_search[r-1][c-1] == 'M' and  # Top-left
                    word_search[r-1][c+1] == 'S' and  # Top-right
                    word_search[r+1][c-1] == 'M' and  # Bottom-left
                    word_search[r+1][c+1] == 'S')or (word_search[r-1][c-1] == 'S' and  # Top-left
                    word_search[r-1][c+1] == 'M' and  # Top-right
                    word_search[r+1][c-1] == 'S' and  # Bottom-left
                    word_search[r+1][c+1] == 'M'): # Bottom-right
                    # If all conditions are met, we found an "X-MAS"
                    xmas_count += 1

    return xmas_count

# Example word search
def get_data():
    with open("./2024/4-12-2024/4-12-2024.txt", 'r') as bestand:
            data = [line.strip() for line in bestand.readlines()]    
    return data

grid = get_data()

# Count the X-MAS patterns
result = count_xmas(grid)
print(f"The number of X-MAS patterns is: {result}")
