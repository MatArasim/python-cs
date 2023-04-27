import math as m
import matplotlib.pyplot as plt
import numpy as np

def poissonGen(k, lamb):
    k = np.arange(0, k)
    result = []
    for x in k:
        result.append(((lamb**x)*(m.e)**-lamb)/m.factorial(x))

    plt.plot(k, result, marker='o')
    plt.xlabel('k')
    plt.ylabel('Probability')

    plt.show()



poissonGen(23,9)

