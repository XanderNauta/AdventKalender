left_list = []
right_list = []
distance_list = []
simularity_list = []

def getList():
    with open('1-12-2024.txt', 'r') as bestand:
        for line in bestand:
            # Split each line into two parts
            left, right = line.split()  # Adjust the split delimiter if needed
            left = int(left)
            right = int(right)
            left_list.append(left)
            right_list.append(right)
    print("Left list:", left_list)
    print("Right list:", right_list)

def get_lowest_right_list():
    lowest_right = right_list[0]

    for number in right_list:
        if number < lowest_right:
            lowest_right = number

    return int(lowest_right)

def get_lowest_left_list():
    lowest_Left = left_list[0]

    for number in left_list:
        if number < lowest_Left:
            lowest_Left = number

    return int(lowest_Left)


def count_distance():
    lowest_right = get_lowest_right_list()
    lowest_left = get_lowest_left_list()

    distance_lowest_numbers = abs(lowest_right - lowest_left)

    right_list.remove(lowest_right)
    left_list.remove(lowest_left)

    distance_list.append(distance_lowest_numbers)

    print(distance_list)

def count_total_distance():
    distance = 0
    for number in distance_list:
        distance = distance + number
    print(distance)

def count_simularity_score():
    left_number1 = left_list[0]
    count = 0

    for number in right_list:
        if int(number) == int(left_number1):
            count = count + 1
    
    number_to_list = count * left_number1

    simularity_list.append(number_to_list)

    left_list.remove(left_number1) 

def count_all_simularity_scores():
    total_simulatirty = 0

    for number in simularity_list:
        total_simulatirty = total_simulatirty + number

    print(total_simulatirty)

if __name__=="__main__":
    getList()
    boolean = True
    while boolean:
        if len(left_list) != 0: 
            count_simularity_score()
        elif len(left_list) == 0:
            boolean = False
            count_all_simularity_scores()
           