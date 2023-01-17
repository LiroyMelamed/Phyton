import matplotlib.pyplot as plt
import networkx as nx
import random as rd

def accurate(G):
    cliques = nx.find_cliques(G)
    max_clique = 0
    for clique in cliques:
        if max_clique < len(clique):
            max_clique = len(clique)
    return max_clique

def approximately(G):
    return len(nx.algorithms.approximation.clique.max_clique(G))

def approximation_ratio(G):
    return accurate(G) / approximately(G)

def draw(n_values, p_values, ratios):
    fig, axs = plt.subplots(len(p_values), 1)
    for i, p in enumerate(p_values):
        axs[i].plot(n_values, ratios[i], label=f"p={p}")
        axs[i].set_xlabel("n")
        axs[i].legend()
    axs[0].set_ylabel("Approximation Ratio")
    plt.show()

def Start():
    n_values = list(range(10, 100))
    p_values = [0.1, 0.2, 0.3, 0.4, 0.5]
    ratios = [[] for _ in range(len(p_values))]
    for n in n_values:
        for i, p in enumerate(p_values):
            G = nx.fast_gnp_random_graph(n, p)
            ratios[i].append(approximation_ratio(G))
    draw(n_values, p_values, ratios)

if __name__ == '__main__':
    Start()