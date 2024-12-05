def read_rules():
    with open("./2024/5-12-2024/5-12-2024.txt", 'r') as bestand:
            data = bestand.read().splitlines()    
    data = [list(map(int, line.split("|"))) for line in data]
    return data

def read_list():
    with open("./2024/5-12-2024/ListOfNumbers.txt", 'r') as bestand:
            data = bestand.read().splitlines()     
    data = [list(map(int, line.split(","))) for line in data]
    return data

rules = read_rules()
list_numbers = read_list()
count = 0

for row in list_numbers:
    isValid = True
    for rule in rules:
        print(rule)
        if rule[0] in row:
             if rule[1] in row:
                  if row.index(rule[0]) > row.index(rule[1]): 
                    isValid = False
    if isValid:
         count += int(row[len(row)//2])

print(count)
