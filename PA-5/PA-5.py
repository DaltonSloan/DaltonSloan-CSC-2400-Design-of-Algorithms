import time
from collections import deque

def read_graphs(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    graphs = []
    graph = {}
    for line in lines:
        if line.strip() == "":
            graphs.append(graph)
            graph = {}
        else:
            parts = line.split(":")
            vertex = int(parts[0]) - 1
            neighbors = list(map(lambda x: int(x) - 1, parts[1].split()))
            graph[vertex] = neighbors
    if graph:  # Add the last graph if file doesn't end with a blank line
        graphs.append(graph)
    return graphs

def DFS_R_Components(E, n):
    visited = [False] * n
    component_count = 0

    def dfs_helper(vertex):
        visited[vertex] = True
        for neighbor in E.get(vertex, []):
            if not visited[neighbor]:
                dfs_helper(neighbor)

    for i in range(n):
        if not visited[i]:
            dfs_helper(i)
            component_count += 1

    return component_count

def DFS_Components(E, n):
    visited = [False] * n
    component_count = 0

    for i in range(n):
        if not visited[i]:
            stack = [i]
            while stack:
                vertex = stack.pop()
                if not visited[vertex]:
                    visited[vertex] = True
                    for neighbor in E.get(vertex, []):
                        if not visited[neighbor]:
                            stack.append(neighbor)
            component_count += 1

    return component_count

def BFS_Components(E, n):
    visited = [False] * n
    component_count = 0

    for i in range(n):
        if not visited[i]:
            queue = deque([i])
            while queue:
                vertex = queue.popleft()
                if not visited[vertex]:
                    visited[vertex] = True
                    for neighbor in E.get(vertex, []):
                        if not visited[neighbor]:
                            queue.append(neighbor)
            component_count += 1

    return component_count

def measure_time(func, E, n):
    start = time.time()
    result = func(E, n)
    end = time.time()
    return result, (end - start) * 1e6  # Time in microseconds

def main():
    graphs = read_graphs("random_graphs.txt")
    n = 50  # Each graph has 50 vertices

    dfs_rec_outputs = []
    dfs_stack_outputs = []
    bfs_outputs = []
    runtimes = []

    for graph in graphs:
        # DFS (Recursive)
        result, time_dfs_rec = measure_time(DFS_R_Components, graph, n)
        dfs_rec_outputs.append(result)

        # DFS (Stack-Based)
        result, time_dfs_stack = measure_time(DFS_Components, graph, n)
        dfs_stack_outputs.append(result)

        # BFS (Queue-Based)
        result, time_bfs = measure_time(BFS_Components, graph, n)
        bfs_outputs.append(result)

        # Record runtimes
        runtimes.append((time_dfs_rec, time_dfs_stack, time_bfs))

    # Write results to files
    with open("DFSRecOutputs.txt", "w") as file:
        file.write("\n".join(map(str, dfs_rec_outputs)))

    with open("DFSStackOutputs.txt", "w") as file:
        file.write("\n".join(map(str, dfs_stack_outputs)))

    with open("BFSOutputs.txt", "w") as file:
        file.write("\n".join(map(str, bfs_outputs)))

    with open("runtimes.txt", "w") as file:
        file.write("\n".join(f"{t[0]} {t[1]} {t[2]}" for t in runtimes))

if __name__ == "__main__":
    main()