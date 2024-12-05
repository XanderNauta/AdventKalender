from functools import cmp_to_key
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
pages_list = read_list()
count = 0
 
order = {}
for x, y in rules:
    order.setdefault(y, set()).add(x)
def ordering(x, y):
    if x in order.get(y, set()):
        return -1 # x should go before y
    if y in order.get(x, set()):
        return 1 # x should go after y
    return 0 # ordering does not matter
 
for pages in pages_list:
    is_valid = True
    for rule in rules:
        if rule[0] in pages:
            if rule[1] in pages:
                if pages.index(rule[0]) > pages.index(rule[1]):
                    is_valid = False
    if not is_valid:
        print(pages)
        sorted_pages = sorted(pages, key=cmp_to_key(ordering))
        middle_index = len(pages)//2
        count += sorted_pages[middle_index]
print(count)