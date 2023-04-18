import heapq

def prim(graph_file):
    # зчитування матриці суміжності з файлу
    with open(graph_file) as f:
        lines = f.readlines()
        n = int(lines[0].strip())
        graph = [[int(x) for x in line.strip().split()] for line in lines[1:]]

    visited = [0]
    mst = []

    possible_edges = [(graph[0][j], 0, j) for j in range(1, n)]

    # застосування алгоритму Прима
    while len(mst) < n-1:
        # знаходження краю з найменшою вагою
        min_weight, u, v = heapq.heappop(possible_edges)
        if v not in visited:
            visited.append(v)
            mst.append((u, v, min_weight))
            # додавання можливих країв для нової вершини
            for j in range(n):
                if graph[v][j] != 0 and j not in visited:
                    heapq.heappush(possible_edges, (graph[v][j], v, j))

    print("Minimum Spanning Tree:")
    for edge in mst:
        print(edge[0], "-", edge[1], ":", edge[2])

prim("graph.txt")