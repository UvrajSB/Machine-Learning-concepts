#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
alpha=0.4

def pReLU(x,alpha):
    if x>0:
        return x
    else:
        return alpha*x

Vectorization = np.vectorize(pReLU)

def generate_graph(x,alpha, save_graph=False):
    plt.plot(x, Vectorization(x,alpha))
    if save_graph:
        plt.savefig("pReLU.jpg")
    else:
        plt.show()


def main():
    print("Generating graph")
    save_graph = False  # save the graph (true) or show (false)
    generate_graph(np.linspace(-10, 10, 100),alpha, save_graph=save_graph)


if __name__ == "__main__":
    main()

