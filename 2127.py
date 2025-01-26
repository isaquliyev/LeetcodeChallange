class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        def bfs(start: int, visited_set: set, reverse_graph: List[List[int]]) -> int:
            queue = deque([(start, 0)])
            max_length = 0
            while queue:
                current, distance = queue.popleft()
                for neighbor in reverse_graph[current]:
                    if neighbor in visited_set:
                        continue
                    visited_set.add(neighbor)
                    queue.append((neighbor, distance + 1))
                    max_length = max(max_length, distance + 1)
            return max_length

        n = len(favorite)
        reverse_graph = [[] for _ in range(n)]
        for person, admirer in enumerate(favorite):
            reverse_graph[admirer].append(person)

        longest_cycle = 0
        mutual_pairs_invitations = 0
        visited = [False] * n

        for person in range(n):
            if not visited[person]:
                visited_nodes = {}
                current = person
                distance = 0

                while True:
                    if visited[current]:
                        break
                    visited[current] = True
                    visited_nodes[current] = distance
                    distance += 1
                    next_person = favorite[current]

                    if next_person in visited_nodes:
                        cycle_length = distance - visited_nodes[next_person]
                        longest_cycle = max(longest_cycle, cycle_length)

                        if cycle_length == 2:
                            person1, person2 = current, next_person
                            mutual_pair_visited = {person1, person2}
                            mutual_pairs_invitations += (
                                2
                                + bfs(person1, mutual_pair_visited, reverse_graph)
                                + bfs(person2, mutual_pair_visited, reverse_graph)
                            )
                        break
                    current = next_person
        return max(longest_cycle, mutual_pairs_invitations)
