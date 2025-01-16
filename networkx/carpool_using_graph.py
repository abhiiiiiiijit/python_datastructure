from collections import defaultdict
import math

def solution(A, B):
    class Graph:
        def __init__(self, n):
            self.adj_list = defaultdict(list)

        def add_edge(self, u, v):
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)

    def dfs(node, parent):
        nonlocal fuel_consumption
        passengers = 1  # Each house contributes one passenger.

        for neighbor in graph.adj_list[node]:
            if neighbor != parent:  # Avoid revisiting the parent node.
                # Calculate passengers from the subtree.
                child_passengers = dfs(neighbor, node)

                # Calculate the fuel needed to transport these passengers to the current node.
                fuel_consumption += math.ceil(child_passengers / 5)
                passengers += child_passengers

        return passengers

    # Step 1: Build the graph using the Graph class.
    n = len(A) + 1  # Number of junctions is N + 1.
    graph = Graph(n)

    for a, b in zip(A, B):
        graph.add_edge(a, b)

    # Step 2: Initialize fuel consumption and start DFS from the office (node 0).
    fuel_consumption = 0
    dfs(0, -1)

    return fuel_consumption

# Examples
A1 = [0, 1, 1]
B1 = [1, 2, 3]
print(solution(A1, B1))  # Output: 3

A2 = [1, 1, 1, 9, 9, 9, 9, 7, 8]
B2 = [2, 0, 3, 1, 6, 5, 4, 0, 0]
print(solution(A2, B2))  # Output: 10

A3 = [1, 1, 1, 9, 9, 9, 9, 7, 8, 10, 11, 12, 13]
B3 = [2, 0, 3, 1, 6, 5, 4, 0, 0, 4, 4, 4, 4]
print(solution(A3, B3))  # Output: 10
