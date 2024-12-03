def get_info():
    with open("./3-12-2024/3-12-2024.txt", 'r') as bestand:
            data = bestand.readlines()    
    return data

import re

def extract_how_patterns(data):
    data = str(data)
    # Regular expression om patronen zoals how(x, y) te vinden
    pattern = r"mul\(\d+,\d+\)|(?:don't|do)\(\)"
    matches = re.findall(pattern, data)
    return matches

def count_everyThing(result):
    total_count = 0
    enebeld = True
    for item in result:
            item = str(item)
            if item == "do()":
               enebeld = True
            elif item == "don't()":
                enebeld = False
            elif enebeld: 
                item = item.strip("mul(").rstrip("()").rstrip("()")
                item = item.split(",")
                getal1 = item[0]
                getal2 = item[1]
                count = int(getal1) * int(getal2)
                total_count += count

    print(total_count)

if __name__ == "__main__":
    data = get_info()
    result = extract_how_patterns(data)
    # print(result)
    count_everyThing(result)