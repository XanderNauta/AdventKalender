from collections import deque

def parse_grid(grid):
    """Parse the input grid into a 2D list."""
    return [list(row) for row in grid]

def find_start_position(grid):
    """Find the starting position of the guard (marked as '^')."""
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == '^':
                return r, c, 'up'
    return None

def turn_right(direction):
    """Turn the guard 90 degrees to the right."""
    turns = {
        'up': 'right',
        'right': 'down',
        'down': 'left',
        'left': 'up'
    }
    return turns[direction]

def move_forward(r, c, direction):
    """Move one step forward based on the direction."""
    moves = {
        'up': (-1, 0),
        'right': (0, 1),
        'down': (1, 0),
        'left': (0, -1)
    }
    dr, dc = moves[direction]
    return r + dr, c + dc

def simulate_patrol(grid, start):
    """Simulate the guard's patrol route and record visited positions."""
    visited = set()
    r, c, direction = start

    while 0 <= r < len(grid) and 0 <= c < len(grid[0]):
        if (r, c) not in visited:
            visited.add((r, c))

        # Check the cell in front of the guard
        nr, nc = move_forward(r, c, direction)

        if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])) or grid[nr][nc] == '#':
            # Turn right if there's an obstacle
            direction = turn_right(direction)
        else:
            # Move forward
            r, c = nr, nc

    return visited

def find_obstruction_positions(grid, patrol_positions, start):
    """Find all positions where an obstruction creates a loop."""
    obstruction_positions = set()

    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if (r, c) not in patrol_positions and cell == '.' and (r, c) != (start[0], start[1]):
                # Temporarily place an obstruction
                grid[r][c] = '#'

                # Simulate patrol with the new obstruction
                new_patrol = simulate_patrol(grid, start)

                # Check if the patrol is stuck in a loop
                if len(new_patrol) < len(patrol_positions):
                    obstruction_positions.add((r, c))

                # Remove the obstruction
                grid[r][c] = '.'

    return obstruction_positions

# Input grid
grid_input = [
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#..."
]

# Parse grid
grid = parse_grid(grid_input)

# Find starting position
start = find_start_position(grid)

# Simulate patrol to find patrol positions
patrol_positions = simulate_patrol(grid, start)

# Find possible obstruction positions
obstruction_positions = find_obstruction_positions(grid, patrol_positions, start)

# Output the result
print("Number of possible obstruction positions:", len(obstruction_positions))
print("Positions:", obstruction_positions)
