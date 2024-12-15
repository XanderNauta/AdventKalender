# Bestanden lezen en wereldkaart initialiseren
file_path = './2024/8-12-2024/echte_data.txt'

with open(file_path, "r") as file:
    world_map = [line.strip() for line in file]

world_map_width = len(world_map[0])
world_map_height = len(world_map)

def pak_alle_letters(world_map):
    """Verzamelt alle unieke niet-punt karakters uit de wereldkaart."""
    return {j for i in world_map for j in i if j != "."}

def zoek_locaties_letters(world_map, letter):
    """Zoekt alle locaties van een specifieke letter in de wereldkaart."""
    return {
        (x, y)
        for y in range(len(world_map))
        for x in range(len(world_map[y]))
        if world_map[y][x] == letter
    }

def bereken_mogelijke_coordinaten(main_locatie, other_locatie, world_map):
    """Berekent mogelijke coördinaten op basis van main en other locatie."""
    verschil_x = main_locatie[0] - other_locatie[0]
    verschil_y = main_locatie[1] - other_locatie[1]

    # Bereken waar de derde locatie zou kunnen liggen
    mogelijke_x = main_locatie[0] + verschil_x
    mogelijke_y = main_locatie[1] + verschil_y

    # Controleer of de coördinaten binnen de wereldkaart liggen
    if 0 <= mogelijke_x < len(world_map[0]) and 0 <= mogelijke_y < len(world_map):
        return mogelijke_x, mogelijke_y
    return None

# Verwerk de letters en bereken verschillen
letters = pak_alle_letters(world_map)
aantal_unieke_locaties = set()

for letter in letters:
    locaties = zoek_locaties_letters(world_map, letter)
    for main_locatie in locaties:
        for other_locatie in locaties:
            if main_locatie != other_locatie:
                verschil_x = main_locatie[0] - other_locatie[0]
                verschil_y = main_locatie[1] - other_locatie[1]
                # print(f"Verschillen: ({verschil_x}, {verschil_y})")

                mogelijke_locatie = bereken_mogelijke_coordinaten(main_locatie, other_locatie, world_map)
                if mogelijke_locatie:
                    aantal_unieke_locaties.add((mogelijke_locatie))
                else:
                    print("Mogelijke locatie valt buiten de kaart.")
        
                
print(len(aantal_unieke_locaties))