
import heapq


def dijkstra(graph, start):
    n = len(graph)
    distances = [float("inf")] * n
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex]:
            if distances[current_vertex] + weight < distances[neighbor]:
                distances[neighbor] = distances[current_vertex] + weight
                heapq.heappush(heap, (distances[neighbor], neighbor))
    return distances


if __name__ == "__main__":
    graph = [
        [(1, 4), (2, 2), (3, 5)],   # Вершина 0
        [(4, 6), (5, 3)],           # Вершина 1
        [(4, 1)],                   # Вершина 2
        [(5, 2)],                   # Вершина 3
        [],                         # Вершина 4
        [(6, 3)],                   # Вершина 5
        []                          # Вершина 6
    ]    
    start_vertex = 0
    shortest_distances = dijkstra(graph, start_vertex)

    print("Найкоротші відстані від вершини", start_vertex)
    for i, distance in enumerate(shortest_distances):
        print(f"До вершини {i}: {distance}")
