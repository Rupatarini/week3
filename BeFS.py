from queue import PriorityQueue
def best_first_search(actual_Src, target, n, graph):
    visited = [False] * n
    pq = PriorityQueue()
    pq.put((0, actual_Src))
    visited[actual_Src] = True
    while not pq.empty():
        u = pq.get()[1]
        print(u, end=" ")
        if u == target:
            print()
            return
        for v, cost in graph[u]:
            if not visited[v]:
                visited[v] = True
                pq.put((cost, v))
    print("Target not reachable from the source.")
def addedge(graph, x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))
v = int(input("Enter the number of vertices: "))
e = int(input("Enter the number of edges: "))
graph = [[] for _ in range(v)]
for _ in range(e):
    x, y, cost = map(int, input("Enter edge (start end cost): ").split())
    addedge(graph, x, y, cost)
source = int(input("Enter the source node: "))
target = int(input("Enter the target node: "))
best_first_search(source, target, v, graph)
