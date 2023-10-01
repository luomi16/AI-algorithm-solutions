from collections import deque


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []

        # 因为是无向图，所以需要在两个方向上都添加边
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex)  # 输出当前访问的顶点
                visited.add(vertex)
                queue.extend(
                    [neighbor for neighbor in self.adj_list[vertex] if neighbor not in visited])


if __name__ == '__main__':
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.bfs(0)
