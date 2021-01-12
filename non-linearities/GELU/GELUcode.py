#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import math

def GELU(x):
    return 1/2*x*(1+(math.erf(x/(2**1/2))))

Vectorization= np.vectorize(GELU)

def generate_graph(x, save_graph=False):
    plt.plot(x, Vectorization(x))
    if save_graph:
        plt.savefig("GELU.jpg")
    else:
        plt.show()


def main():
    print("Generating graph")
    save_graph = False  # save the graph (true) or show (false)
    generate_graph(np.linspace(-10, 10, 100), save_graph=save_graph)


if __name__ == "__main__":
    main()

