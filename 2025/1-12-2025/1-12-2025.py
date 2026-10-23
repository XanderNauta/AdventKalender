from pathlib import Path

script_dir = Path(__file__).parent
bestand_pad = script_dir / "1-12-2025.txt"

lijst = []
current_nummber = 50
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
    global current_nummber, code
    if not lijst:
        return
    
    item = lijst.pop(0)
    
    direction = item[0]
    try:
        rotation = int(item[1:])
    except ValueError:
        rotation = 0

    if direction == "R":
        current_nummber = (current_nummber + rotation) % 100
    elif direction == "L":
        current_nummber = (current_nummber - rotation) % 100
        
    if current_nummber == 0:
        code += 1

if __name__ == "__main__":
    get_list()
    while lijst:
        process_first_item()
    print("Final code value:", code)