class Graph:
    def __init__(self):
        self.adj_list={}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ";", self.adj_list[vertex])
    
    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex]=[]
            return True
        return False
    def add_edge(self, v1, v2):
        if v1 and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        
    def remove_edge(self, v1, v2):
        if v1 and v2 in self.adj_list:
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True

    
my_graph=Graph()
my_graph.add_vertex('a')
my_graph.add_vertex('b')
my_graph.print_graph()
my_graph.add_edge('a','b')
my_graph.print_graph()
my_graph.remove_edge('a','b')


