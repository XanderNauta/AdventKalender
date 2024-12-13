from collections import deque


def read_and_process_file(file_path):
    processed_data = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(":")
            processed_data.append((int(parts[0]), list(map(int, parts[1].strip().split(" ")))))
    return processed_data

def generate_all_binar_numbers(eqn):
    return [bin(idx)[2:].zfill(eqn) for idx in range( 2 ** eqn)]

def generate_all_possible_equations(eqn):
    all_binair_numbers = generate_all_binar_numbers(len(eqn) - 1)

    equations = deque()

    for bin in all_binair_numbers:
        equation = deque()
        for idx in range(len(bin)):
            equation.append(eqn[idx])

            if bin[idx] == '0':
                equation.append("+")
            elif bin[idx] == '1':
                equation.append("*")
        equation.append(eqn[-1])
        equations.append(equation)
    return equations

def evaluate(deque):

    if (len(deque) ==  1):
        return int(deque[0])
    
    n1 = deque.popleft()
    operator = deque.popleft()
    n2 = deque.popleft()
    
    if operator == "+":
        plus = n1 + n2
        deque.appendleft(plus)
        return evaluate(deque)
    if operator == "*":
        keer = n1 * n2
        deque.appendleft(keer)
        return evaluate(deque)
    

file_path = "./2024/7-12-2024/7-12-2024.txt"
data = read_and_process_file(file_path)
counter = 0
attainable_counter = set()

for line in data: 
    answer = line[0]
    equetion_matiral = line[1]

    alle_possible_equetions = generate_all_possible_equations(equetion_matiral)

    for eqn in alle_possible_equetions:
        if answer == evaluate(eqn):
            attainable_counter.add(answer)
            counter+= answer
            break

print(sum(attainable_counter))
print(counter)

#3312271364788 to low
#