class WeightedGraph:
    def __init__(self, vertices, edges):
        self.graph = {}
        self.vertices = vertices
        self.edges = edges
        for a, b, weight  in edges:
            if vertices[a] not in self.graph:
                self.graph[vertices[a]] = {}
            
            if vertices[b] not in self.graph[vertices[a]]:
                self.graph[vertices[a]][vertices[b]] = None

            self.graph[vertices[a]][vertices[b]] = weight 

    def getMinimumSpanningTree(self):
        return MinimumSpanningTree(self)

    def get_edges(self):
        edges = []
        for x in self.graph:
            for y in self.graph[x]:
                edges.append([x, y, self.graph[x][y]])
        return edges
    
    def getShortestPath(self, root):
        return ShortestPathTree(self, root)
    


class MinimumSpanningTree:
    def __init__(self, G):
        self.tree = {}
        self.cost = 0
        self.root = next(iter(G.graph))

        sets = [set([v]) for v in G.graph.keys()]

        edges = sorted(G.get_edges(), key=lambda x: x[2])

        for a, b, weight in edges:
            set_of_a = next((s for s in sets if a in s), None)
            set_of_b = next((s for s in sets if b in s), None)

            if set_of_a != set_of_b:
                if a not in self.tree:
                    self.tree[a] = {}

                if b not in self.tree[a]:
                    self.tree[a][b] = weight

                if b not in self.tree:
                    self.tree[b] = {}

                if a not in self.tree[b]:
                    self.tree[b][a] = weight

                self.cost += weight

                sets.remove(set_of_a)
                sets.remove(set_of_b)
                sets.append(set_of_a | set_of_b)


    def getTotalWeight(self):
        return self.cost

    def printTree(self):
        print(self.tree)
        print(f"Root is: {self.root}")
        edges = []
        for k, v in self.tree.items():
            for dest, _ in v.items():
                edges.append((k, dest))

        print("Edges:", " ".join(str(e) for e in edges))

class ShortestPathTree:
    def __init__(self, G, root):
        T = set()
        self.root = root
        self.cost = {} # set containing the cost to each node
        self.parents = {} # set of the direct parent of each node, the root get the value 'None'

        for a in G.graph:
            self.cost[a] = float("inf")

        self.cost[root] = 0
        self.parents[root] = None
        T.add(root)

        while len(T) < len(G.graph):
            min_cost = float('inf')
            for a in T:
                for b in G.graph[a]:
                    if b not in T:
                        if self.cost[a] + G.graph[a][b] < min_cost:
                            min_cost = self.cost[a] + G.graph[a][b]
                            self.parents[b] = a
                            curr_node = b
            T.add(curr_node)
            self.cost[curr_node] = min_cost

    def printAllPaths(self):
        print(f"All shortest paths from {self.root} are:")
        for a in self.parents:
            if a is not None:
                print(f"A path from {self.root} to {a}: ", end="")
                
                path = []
                while a is not None:
                    path.append(a)
                    a = self.parents[a]
                path.reverse()
                print(" ".join(path), end=" ")
                print(f"(cost: {self.cost[path[-1]]})")

                


def main():
    # Create vertices
    vertices = ["Seattle", "San Francisco", "Los Angeles",
          "Denver", "Kansas City", "Chicago", "Boston", "New York",
          "Atlanta", "Miami", "Dallas", "Houston"]

    # Create edges
    edges = [
          [0, 1, 807], [0, 3, 1331], [0, 5, 2097],
          [1, 0, 807], [1, 2, 381], [1, 3, 1267],
          [2, 1, 381], [2, 3, 1015], [2, 4, 1663], [2, 10, 1435],
          [3, 0, 1331], [3, 1, 1267], [3, 2, 1015], [3, 4, 599],
            [3, 5, 1003],
          [4, 2, 1663], [4, 3, 599], [4, 5, 533], [4, 7, 1260],
            [4, 8, 864], [4, 10, 496],
          [5, 0, 2097], [5, 3, 1003], [5, 4, 533],
            [5, 6, 983], [5, 7, 787],
          [6, 5, 983], [6, 7, 214],
          [7, 4, 1260], [7, 5, 787], [7, 6, 214], [7, 8, 888],
          [8, 4, 864], [8, 7, 888], [8, 9, 661],
            [8, 10, 781], [8, 11, 810],
          [9, 8, 661], [9, 11, 1187],
          [10, 2, 1435], [10, 4, 496], [10, 8, 781], [10, 11, 239],
          [11, 8, 810], [11, 9, 1187], [11, 10, 239]
        ]

    # Create a graph
    graph1 = WeightedGraph(vertices, edges)

    # Obtain a minimum spanning tree
    tree1 = graph1.getMinimumSpanningTree()
    print("tree1: Total weight is " + str(tree1.getTotalWeight()))
    tree1.printTree()

    tree2 = graph1.getShortestPath("Chicago")
    tree2.printAllPaths()

main()