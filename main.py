from collections import deque


def bfs_distances(graph, start):
    """
    Compute shortest distances (in edges) from start to all reachable nodes
    in an unweighted graph.

    graph: dict mapping stage name (string) to list of neighbor stage names.
    start: starting stage name (string).

    Returns:
        A dict dist where:
            - dist[node] = minimum number of edges from start to node
            - dist[start] = 0
            - Only includes reachable nodes
        If start not in graph → return {}
    """

    # If start not in the graph, nothing to compute
    if start not in graph:
        return {}

    # Distance dictionary (answer)
    dist = {start: 0}

    # BFS queue
    queue = deque([start])

    # BFS traversal
    while queue:
        node = queue.popleft()
        current_distance = dist[node]

        # Explore neighbors
        for neighbor in graph.get(node, []):
            if neighbor not in dist:  # not visited
                dist[neighbor] = current_distance + 1
                queue.append(neighbor)

    return dist


if __name__ == "__main__":
    # Optional simple check
    sample_graph = {
        "Gate": ["Stage1", "Stage2"],
        "Stage1": ["Gate", "Stage3"],
        "Stage2": ["Gate"],
        "Stage3": ["Stage1"],
    }
    d = bfs_distances(sample_graph, "Gate")
    print("Distances from Gate:", d)
