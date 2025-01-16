from collections import defaultdict
import math

def solution(A, B):
    def dfs(node, parent):
        nonlocal fuel_consumption
        passengers = 1  # The current node represents one passenger.

        for neighbor in graph[node]:
            if neighbor != parent:  # Avoid revisiting the parent node.
                # Recursive DFS call to calculate passengers from children.
                child_passengers = dfs(neighbor, node)

                # Calculate fuel needed to move these passengers to the current node.
                fuel_consumption += math.ceil(child_passengers / 5)  # One car can carry 5 passengers.
                passengers += child_passengers

        return passengers

    # Step 1: Build the graph as an adjacency list.
    graph = defaultdict(list)
    for a, b in zip(A, B):
        graph[a].append(b)
        graph[b].append(a)

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
