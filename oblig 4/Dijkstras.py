class WeightedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = {}
        self.graph[node1][node2] = weight
        
        if node2 not in self.graph:
            self.graph[node2] = {}
        self.graph[node2][node1] = weight

    def parse_graph_file(self, file):
        with open(file, "r") as f:
            number_of_vertecies = int(f.readline().strip())
            for _ in range(number_of_vertecies):
                line = f.readline().strip().split("|")
                for x in line:
                    [u, v, w] = x.split(",")
                    self.add_edge(int(u), int(v), int(w))
        
    def __str__(self):
        return str(self.graph)

    
    def get_shortest_path(self, s):
        T = set()
        cost = {}
        parent = {}
        
        for u in self.graph.keys():
            cost[u] = float('inf')

        cost[s] = 0
        parent[s] = None
        T.add(s)
        
        while len(T) < len(self.graph):
            min_cost = float('inf')
            for u in T:
                for v in self.graph[u]:
                    if v not in T:
                        if cost[u] + self.graph[u][v] < min_cost:
                            min_cost = cost[u] + self.graph[u][v]
                            parent[v] = u
                            curr_node = v
            T.add(curr_node)
            cost[curr_node] = min_cost


        return ShortestPathTree(s, cost, parent)

class ShortestPathTree:
    def __init__(self, root, cost, parent):
        self.root = root
        self.cost = cost # set containing the cost to each node
        self.parents = parent # set of the direct parent of each node, the root get the value 'None'

    def __str__(self) -> str:
        return f"root: {self.root}\nparent: {self.parents}\ncost: {self.cost}"

def main():
    path = input("Enter a path to a graph: ")
    g = WeightedGraph()
    g.parse_graph_file(path)
    tree = g.get_shortest_path(1)
    print(tree)
main()

