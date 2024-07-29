import heapq
def a_star_search(graph, start, end, h):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {node: float('inf') for node in range(len(graph))}
    g_score[start] = 0
    f_score = {node: float('inf') for node in range(len(graph))}
    f_score[start] = h(start, end)
    while open_set:
        current = heapq.heappop(open_set)[1]
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  
        for neighbor, cost in graph[current]:
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + h(neighbor, end)
                if neighbor not in [i[1] for i in open_set]:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    return None 
def heuristic(node, target):
    return abs(node - target)
def add_edge(graph, x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))
v = int(input("Enter the number of vertices: "))
e = int(input("Enter the number of edges: "))
graph = [[] for _ in range(v)]
for _ in range(e):
    x, y, cost = map(int, input("Enter edge (start end cost): ").split())
    add_edge(graph, x, y, cost)
source = int(input("Enter the source node: "))
target = int(input("Enter the target node: "))
path = a_star_search(graph, source, target, heuristic)
if path:
    print("Path found:", path)
else:
    print("No path found from source to target.")
