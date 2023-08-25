import math
import matplotlib

class Graph:
    def __init__(self, name):
        self.name = name
        self.nodes = []
        
    def add_node(self, name):
        self.nodes.append(name)

class Node:
    def __init__(self, name):
        self.name = name
        self.connections = []
    def new_connection(self, name, destination, weight):
        name = Connection(name, destination, weight)
        self.connections.append(name)

        
class Connection:
    def __init__(self, origin, destination, weight):
        self.origin = origin
        self.destination = destination
        self.weight = weight
    def set_weight(newWeight):
        weight = newWeight
    def return_name(self):
        return(str(self.origin.name + " to " + self.destination.name))

# testing info:
# mygraph = Graph("mygraph")
# HI = Node("HI")
# CA = Node("CA")

# mygraph.add_node(HI.name)
# mygraph.add_node(CA.name)

# HI.new_connection(HI, CA, 0.2)

# print(f"Hawaii's connections: ")
# for connection in HI.connections:
#     print(connection.return_name(), sep=", ", end="")
# print("\n")

# print(f"Nodes in graph: {mygraph.nodes}")
