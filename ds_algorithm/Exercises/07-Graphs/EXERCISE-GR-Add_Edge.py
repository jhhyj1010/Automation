class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    ## WRITE ADD_EDGE METHOD HERE ##
    #                              #
    #                              #
    #                              #
    #                              #
    ################################
    def add_edge(self, value1, value2):
        if value1 not in self.adj_list.keys():
            self.adj_list[value1] = []
        if value2 not in self.adj_list.keys():
            self.adj_list[value2] = []
        self.adj_list[value1].append(value2)
        self.adj_list[value2].append(value1)





my_graph = Graph()

my_graph.add_vertex(1)
my_graph.add_vertex(2)

my_graph.add_edge(1,2)

my_graph.print_graph()



"""
    EXPECTED OUTPUT:
    ----------------
    1 : [2]
    2 : [1]

"""