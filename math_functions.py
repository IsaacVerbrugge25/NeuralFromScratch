import math

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

if __name__ == "__main__":
    ...
