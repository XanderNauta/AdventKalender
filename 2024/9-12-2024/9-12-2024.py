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

def reverbised(block):

    while '' in block:
        print('blank space left', block.count(""))
        element = block.pop()

        if element == '':
            continue

        empty = find_empty(block)

        block[empty] = element

    return block

def calculate_number(referbised_block):
    # print(referbised_block)
    counter = 0

    for idx, getal in enumerate(referbised_block):
        value = idx * getal
        counter += value
    return counter


block = convert_to_block(disk_data)

referbised_block = reverbised(block)

ans = calculate_number(referbised_block)

print(ans)


# 5683949361 v
# 