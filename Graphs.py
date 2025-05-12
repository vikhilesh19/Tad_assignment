import heapq
graph ={'A': [('B', 1), ('C', 4)],'B': [('A', 1), ('D', 2)],'C': [('A', 4), ('D', 5)],'D': [('B', 2), ('C', 5), ('E', 1)],'E': [('D', 1)]}
def bfs(start):
    visited = set()
    queue = [start]
    print("\nBFS Traversal:")
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(f"Visited: {node}")
            visited.add(node)
            for neighbor, _ in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

def dfs(start, visited=None):
    if visited is None:
        visited = set()
        print("\nDFS Traversal:")
    visited.add(start)
    print(f"Visited: {start}")
    for neighbor, _ in graph[start]:
        if neighbor not in visited:
            dfs(neighbor, visited)

def dijkstra(start):
    print("\nDijkstra's Shortest Path:")
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        curr_dist, node = heapq.heappop(pq)
        print(f"Visiting: {node} with current distance: {curr_dist}")
        for neighbor, weight in graph[node]:
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    print("Shortest Distances:", distances)


class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        if root1 != root2:
            self.parent[root2] = root1

def kruskal():
    print("\nKruskal’s MST:")
    edges = []
    for node in graph:
        for neighbor, weight in graph[node]:
            if (neighbor, node, weight) not in edges: 
                edges.append((node, neighbor, weight))
    edges.sort(key=lambda x: x[2])

    ds = DisjointSet(graph.keys())
    mst = []

    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))
            print(f"Edge added: {u} - {v} ({weight})")
    print("MST:", mst)

def prim(start):
    print("\nPrim’s MST:")
    visited = set()
    pq = [(0, start, None)]
    mst = []

    while pq:
        weight, node, parent = heapq.heappop(pq)
        if node not in visited:
            visited.add(node)
            if parent:
                mst.append((parent, node, weight))
                print(f"Edge added: {parent} - {node} ({weight})")
            for neighbor, w in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (w, neighbor, node))
    print("MST:", mst)

bfs('A')
dfs('A')
dijkstra('A')
kruskal()
prim('A')