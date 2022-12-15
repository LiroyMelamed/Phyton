import matplotlib.pyplot as plt
import networkx as nx
import random as rd


def accurate(G):
    # In this function we find the max cliques in the graph
    cliques = nx.find_cliques(G)
    max_clique = 0
    for clique in cliques:
        # accurate as we are getting every clique and check it len
        if max_clique < len(clique):
            max_clique = len(clique)
    # Returning the clique with the max len
    return max_clique


def approximately(G):
    # Approximatly algorithms that we get from networkx
    return len(nx.algorithms.approximation.clique.max_clique(G))


def draw(size, comp):
    plt.plot(size, comp)
    plt.ylabel('comp')
    plt.xlabel('size')
    plt.show()


def Start():
    size = []
    comp = []
    for n in range(10, 100):
        size.append(n)
        v = rd.randint(0, n)
        G = nx.fast_gnp_random_graph(n, v)  # Return random graph
        comp.append(accurate(G) / approximately(G))
    # Drawing the Graph
    draw(size, comp)


if __name__ == '__main__':
    Start()
