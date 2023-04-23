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
        tree = ShortestPathTree(s)
        tree.add_node(s, 0, None)
        cost = {s:0}
        
        for u in self.graph.keys():
            if u not in cost:
                cost[u] = float('inf')
        
        return tree

class ShortestPathTree:
    def __init__(self, root):
        self.root = root
        self.cost = {} # set containing the cost to each node
        self.parents = {} # set of the direct parent of each node, the root get the value 'None'

    def add_node(self, node, cost, parent):
        if node not in self.cost and node not in self.parents:
            self.cost[node] = cost
            self.parents[node] = parent


def main():
    path = input("Enter a path to a graph: ")
    g = WeightedGraph()
    g.parse_graph_file(path)
    tree = g.get_shortest_path(1)
    print(tree.parents, tree.cost)
main()

