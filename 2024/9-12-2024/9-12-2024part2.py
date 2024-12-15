file_path = './2024/9-12-2024/echte_data.txt'
disk_data = ""

with open(file_path, "r") as file:
    for line in file:
        disk_data = line.strip()

def convert_to_block(disk_data):
    block = []
    file_id = 0 

    for idx, data in enumerate(disk_data):
        if idx % 2 == 0:
            for _ in range(int(data))   :
                block.append(file_id)
        
            file_id += 1
        if idx % 2 == 1:
            for _ in range(int(data))   :
                block.append("")
    return block

def find_empty(block):
    for idx, cell in enumerate(block):
        if cell == "":
            return idx

def get_file_size(block , current_file):
    return len([e for e in block if e == current_file])

def get_file_index(block , current_file):
    return block.index(current_file)

def find_blan_section(block, file_size):
    idx = 0
    current_gap = 0
    while idx < len(block):

        cell = block[idx]

        if cell == "":
            current_gap += 1
            idx += 1

            if current_gap == file_size:
                return idx - current_gap

            continue

        idx += 1
        current_gap = 0
def reverbised_whole_files(block):

    current_file = block[-1]

    while current_file > 0:
        print("file_steps away", current_file)

        if block[-1] == "":
            block.pop()
            continue
        
        file_size = get_file_size(block , current_file)

        file_index = get_file_index(block , current_file)

        blank_section = find_blan_section(block, file_size)

        if blank_section is None or blank_section > file_index:
            current_file -= 1
            continue

        block[blank_section: blank_section + file_size] = [current_file] * file_size
        block[file_index: file_index + file_size] = [""] * file_size
        current_file -= 1
    return block

def calculate_number(referbised_block):
    # print(referbised_block)
    counter = 0

    for idx, getal in enumerate(referbised_block):
        if getal != "":
            value = int(idx) * int(getal)
            counter += value
    return counter


block = convert_to_block(disk_data)

referbised_block = reverbised_whole_files(block)

ans = calculate_number(referbised_block)

print(ans)


# 5683949361 v
# 