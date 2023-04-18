import math
from itertools import permutations

def tsp(matrix):
    n = len(matrix)
    min_cost, best_path = math.inf, []
    for perm in permutations(range(n)):
        cost = sum(matrix[perm[i]][perm[i + 1]] for i in range(n - 1)) + matrix[perm[n - 1]][perm[0]]
        if cost < min_cost:
            min_cost, best_path = cost, perm
    return min_cost, best_path

with open('matrix3.txt') as f:
    matrix = [list(map(int, line.split())) for line in f]

t = tsp(matrix)
print(t)