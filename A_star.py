import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, src, dest, weight):
        if src in self.edges:
            self.edges[src].append((dest, weight))
        else:
            self.edges[src] = [(dest, weight)]

    def astar(self, start, goal, heuristic):
        open_set = [(0, start)]
        came_from = {}
        g_score = {node: float('inf') for node in self.edges}
        g_score[start] = 0

        while open_set:
            current_f, current = heapq.heappop(open_set)

            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return path[::-1]

            for neighbor, weight in self.edges[current]:
                tentative_g_score = g_score[current] + weight
                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score, neighbor))

        return None

def manhattan_distance(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

game_graph = Graph()
game_graph.add_edge((0, 0), (0, 1), 1)
game_graph.add_edge((0, 1), (1, 1), 1)
game_graph.add_edge((1, 1), (1, 2), 1)
game_graph.add_edge((1, 2), (2, 2), 1)
game_graph.add_edge((2, 2), (2, 3), 1)
game_graph.add_edge((2, 3), (3, 3), 1)

start = (0, 0)
goal = (3, 3)

path = game_graph.astar(start, goal, manhattan_distance)
if path:
    print("Path found:", path)
else:
    print("No path found")