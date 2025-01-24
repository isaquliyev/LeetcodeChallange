class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        from collections import deque

        n = len(graph)
        reverse_graph = [[] for _ in range(n)]
        in_degree = [0] * n
    
        for i, neighbors in enumerate(graph):
            for neighbor in neighbors:
                reverse_graph[neighbor].append(i)
                in_degree[i] += 1
    
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        safe_nodes = []
    
        while queue:
            node = queue.popleft()
            safe_nodes.append(node)
            for neighbor in reverse_graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
    
        return sorted(safe_nodes)
