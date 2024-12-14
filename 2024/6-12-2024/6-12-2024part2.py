world_map = []
world_map_width = 0
world_map_height = 0
file_path = './2024/6-12-2024/echte6-12-2024.txt'
guard_start = ()
directions = ["NORTH", "EAST", "SOUTH", "WEST"]
world_counter = []

# Read the world map and determine guard's starting position
with open(file_path, "r") as file:
    world_map = [line.strip() for line in file]
    world_map_width = len(world_map[0])
    world_map_height = len(world_map)

    for idx_y in range(world_map_height):
        if "^" in world_map[idx_y]:
            idx_x = world_map[idx_y].index("^")
            world_map[idx_y] = world_map[idx_y].replace("^", ".")
            guard_start = (idx_y, idx_x)

# Define a function to compute the next position based on the current direction
def get_next_guard_pos(cur_pos, dir):
    match dir:
        case "NORTH":
            return (cur_pos[0] - 1, cur_pos[1])
        case "EAST":
            return (cur_pos[0], cur_pos[1] + 1)
        case "SOUTH":
            return (cur_pos[0] + 1, cur_pos[1])
        case "WEST":
            return (cur_pos[0], cur_pos[1] - 1)

# Check if the guard is trapped
def guard_cannot_escape(world_map):
    current_pos = guard_start
    direction = "NORTH"
    visited_states = set()

    while True:
        # Record the current position and direction
        visited_states.add((current_pos, direction))
        next_pos = get_next_guard_pos(current_pos, direction)

        # If revisiting a previous state, the guard is trapped
        if (next_pos, direction) in visited_states:
            world_counter.append(1)
            return True, visited_states

        # Check if the next position is out of bounds (escape)
        if (next_pos[0] < 0 or next_pos[1] < 0 or 
            next_pos[0] >= world_map_height or next_pos[1] >= world_map_width):
            return False, visited_states

        # Determine the object at the next position
        object_infront = world_map[next_pos[0]][next_pos[1]]

        if object_infront == "#":
            # Rotate clockwise if there's a wall in front
            current_idx = directions.index(direction)
            next_direction_idx = (current_idx + 1) % len(directions)
            direction = directions[next_direction_idx]
        elif object_infront == ".":
            # Move forward if the path is clear
            current_pos = next_pos

# Modify the world map to trap the guard and count such configurations
def part2():
    _, visited_positions = guard_cannot_escape(world_map)
    maps_that_trap_guard = set()
    counter = 0

    for i, (position, _) in enumerate(visited_positions):
        idx_y, idx_x = position

        # Skip the starting position
        if position == guard_start:
            continue

        # Create a modified map with a wall at the current position
        modified_world_map = world_map[:]
        modified_row = modified_world_map[idx_y][:idx_x] + "#" + modified_world_map[idx_y][idx_x + 1:]
        modified_world_map[idx_y] = modified_row

        # Check if the modification traps the guard
        if guard_cannot_escape(modified_world_map)[0]:
            maps_that_trap_guard.add(position)
            counter += 1

    return maps_that_trap_guard, counter

# Run the simulation
ans, counter = part2()
print(f"Number of positions that trap the guard: {len(ans)}")
print(f"Counter value: {counter}")
print(f"World counter: {len(world_counter)}")
# 637 to low
# 1897 to high