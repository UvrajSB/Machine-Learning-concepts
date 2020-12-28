import numpy as np
import matplotlib.pyplot as plt


def ELU(x,alpha):
    if (x >= 0).all():
        return np.maximum(0, x)
    else:
        return alpha*(np.exp(x)-1)
    


def generate_graph(x,alpha):
    plt.plot(x, ELU(x,alpha))
    

def main():
    print("Generating graph")
    save_graph = False  # save the graph (true) or show (false)
    alpha= 1
    generate_graph(np.linspace(0, 10, 100),alpha)
    generate_graph(np.linspace(-10, 0, 100),alpha)
    
    if save_graph:
        plt.savefig("ELU.jpg")
    else:
        plt.show()



if __name__ == "__main__":
    main()
