import random

possible_fields = {1: "char c", 2: "short s", 4: "int value", 8: "struct node *n", 16: "int *array"}

def generate_problem():
    problem = "typedef struct node {\n"
    num_fields = random.randint(3,7)
    sizes = []
    for i in range(num_fields):
        size = int(2**random.randrange(5))
        sizes.append(size)
        problem += f'\t{possible_fields[size]}_{i}'
        if size == 16:
            problem += "[2]"
        problem += ";\n"
    problem += "} node_t, *nptr_t;\n"
    return problem, sizes

def generate_solution(sizes):
    alignment = min(max(sizes), 8)
    total_size = 0
    padding = 0
    for size in sizes:
        pad = -total_size % min(size, 8)
        padding += pad
        total_size += size + pad
    padding += -total_size % alignment
    total_size += -total_size % alignment
    third_offset = sizes[0] + sizes[1] + -(sizes[0] + sizes[1]) % sizes[2]

    min_size = 0
    min_padding = 0
    sizes.sort()
    sizes.reverse()
    for size in sizes:
        pad = -min_size % min(size, 8)
        min_padding += pad
        min_size += size + pad
        
    min_padding += -min_size % alignment
    min_size += -min_size % alignment
    
    return f'{alignment}\n{total_size}\n{third_offset}\n{padding}\n{min_size}\n{min_padding}\n'

if __name__ == '__main__':
    problem, field_sizes = generate_problem()
    solution = generate_solution(field_sizes)

    with open("generated_problem/struct_ex.h", 'w+') as f:
        f.write(problem)

    with open("generated_problem/answer.txt", 'w+') as f:
        f.write(solution)