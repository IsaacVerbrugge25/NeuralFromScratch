import math
import matplotlib

# Variables in camelCase
# Classes Uppercase Letters
# functions_underscored

learningRate = 0.1

def RelU(input): #Rectified linear activation function
    if input > 0:
        return input
    else:
        return 0

def calculate(incoming_energy, weight, bias=0): # simple calculate function to find the activation energy of a new node given a connection and an incoming energy
    return(incoming_energy * weight + bias)

# def in_out(polynomial): # takes a polynomial (hopefully we can graph the neural network's guesses as y with a given input as x) and calculates y for x
#         sum = 0
#         for i in range(len(polynomial.powers)):
#             sum += polynomial.coefficients[i] * (x_one ** function.powers[i])
#         return sum

def SSR(observedDataSetCurveFormula, actualDataSet): # sum of squared values function
    sum = 0
    for value in actualDataSet:
        # sum += ( in_out(observedDataSetCurveFormula, value)  - value ) ** 2 # for each x value
        ...


def new_value(oldWeight): # gradient descent function for a given connection's weight.
    # take derivitive of sum of squared values with respect to w4:
    # TODO
    derivitive = ...

    # returns next weight or bias the connection should have
    return oldWeight - (derivitive * learningRate)

class Graph:
    def __init__(self, name):
        self.name = name
        self.nodes = []
        
    def add_node(self, name):
        self.nodes.append(name)

class Node:
    def __init__(self, name, energy=0):
        self.name = name
        self.activationEnergy = energy
        self.connections = []
    def new_connection(self, name, destination, weight, bias):
        name = Connection(name, destination, weight, bias)
        self.connections.append(name)

        
class Connection:
    def __init__(self, origin, destination, weight, bias):
        self.origin = origin
        self.destination = destination
        self.weight = weight
        self.bias = bias

    def return_name(self):
        return str(self.origin.name + " to " + self.destination.name)

## testing info:
mygraph = Graph("mygraph")
HI = Node("HI")
CA = Node("CA")

mygraph.add_node(HI.name)
mygraph.add_node(CA.name)

HI.new_connection(HI, CA, 0.2, 0)

print(f"Hawaii's connections: ")
for connection in HI.connections:
    print(connection.return_name(), sep=", ", end="")
print("\n")

print(f"Nodes in graph: {mygraph.nodes}")

if __name__ == "__main__":
    ...
