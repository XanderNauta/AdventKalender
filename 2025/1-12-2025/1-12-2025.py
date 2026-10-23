from pathlib import Path

script_dir = Path(__file__).parent
bestand_pad = script_dir / "1-12-2025.txt"

lijst = []
absolute_position = 50
code = 0

def get_list():
    global lijst
    with open(bestand_pad, "r") as bestand:
        for line in bestand:
            cleaned = line.strip()
            if cleaned:
                lijst.append(cleaned) 
    print("list loaded:", len(lijst), "items")

def process_first_item():
    global absolute_position, code
    if not lijst:
        return
    
    item = lijst.pop(0)
    
    direction = item[0] 
    try:
        rotation = int(item[1:])
    except ValueError:
        rotation = 0

    old_position = absolute_position

    if direction == "R":
        absolute_position += rotation
        crossings = absolute_position // 100 - old_position // 100
    elif direction == "L":
        absolute_position -= rotation
        crossings = (old_position - 1) // 100 - (absolute_position - 1) // 100
        
    code += crossings

if __name__ == "__main__":
    get_list()
    while lijst:
        process_first_item()
    print("Final password", code)