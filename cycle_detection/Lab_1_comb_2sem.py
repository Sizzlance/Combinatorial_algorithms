import heapq


def build_a_graph(filename):
    with open(filename, 'r') as file:
        arr_size = int(file.readline().strip())

        numbers = []
        while len(numbers) < arr_size:
            line = file.readline()
            if not line:
                break
            numbers.extend(map(int, line.split()))

        pointers = []
        i = 0
        while i < len(numbers) and numbers[i] != arr_size and numbers[i] != 32767:
            pointers.append(numbers[i])
            i += 1

        num_vertices = len(pointers)
        graph = {}

        for vertex in range(1, num_vertices + 1):
            start_index = pointers[vertex - 1] - 1
            if vertex < num_vertices:
                end_index = pointers[vertex] - 1
            else:
                end_index = arr_size - 1

            neighbors = []
            j = start_index
            while j < end_index and j < len(numbers) and numbers[j] != 32767:
                neighbor = numbers[j]
                if neighbor == 0:
                    break
                if j + 1 >= len(numbers) or numbers[j + 1] == 32767:
                    break
                weight = numbers[j + 1]
                neighbors.append((neighbor, weight))
                j += 2

            graph[vertex] = neighbors

        return graph, num_vertices


def prim(graph, n):
    used = set()
    min_heap = []
    start_vertex = 1
    heapq.heappush(min_heap, (0, start_vertex, -1))

    MST_edges = []

    while min_heap and len(used) < n:
        weight, current, from_vertex = heapq.heappop(min_heap)

        if current in used:
            continue

        used.add(current)
        if from_vertex != -1:
            MST_edges.append((from_vertex, current, weight))

        for neighbor, edge_weight in graph[current]:
            if neighbor not in used:
                heapq.heappush(min_heap, (edge_weight, neighbor, current))

    return MST_edges


def main():
    graph, n = build_a_graph('in.txt')
    MST_edges = prim(graph, n)

    ostov_graph = {}
    for i in range(1, n + 1):
        ostov_graph[i] = []

    total_weight = 0
    for a, b, w in MST_edges:
        ostov_graph[a].append(b)
        ostov_graph[b].append(a)
        total_weight += w


    for vertex in ostov_graph:
        ostov_graph[vertex].sort()

    with open('out.txt', 'w') as f:
        for vertex in sorted(ostov_graph.keys()):
            if ostov_graph[vertex]:
                f.write(' '.join(map(str, ostov_graph[vertex])) + ' ')
            f.write('0\n')
        f.write(str(total_weight))


if __name__ == "__main__":
    main()
