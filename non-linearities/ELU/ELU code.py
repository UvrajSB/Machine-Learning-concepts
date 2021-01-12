#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import math



def ELU(x,alpha):
    if x <= 0:
        return alpha*(np.exp(x)-1)
    else:
        return x
    
Vectorization= np.vectorize(ELU)   

def generate_graph(alpha, x, save_graph=False):
    plt.plot(x, Vectorization(x,alpha))
    if save_graph:
        plt.savefig("ELU.jpg")
    else:
        plt.show()


def main():
    print("Generating graph")
    save_graph = False  # save the graph (true) or show (false)
    alpha = 0.2
    generate_graph(alpha,np.linspace(-10, 10, 100), save_graph=save_graph)



if __name__ == "__main__":
    main()


# In[ ]:




