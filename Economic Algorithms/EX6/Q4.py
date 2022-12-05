import math
import doctest

import networkx as nx
from matplotlib import pyplot as plt
from networkx import NetworkXNoCycle


def FindSmallCircle(G) -> list[int]:
    """
    Function to find all the circles with multiplying weights smaller than 1

    The way it works:
    Our Function transforming all the weights of the edges to its log
    and then finds a negative circle and returning it or if not found return []

    >>> G = nx.DiGraph()
    >>> G.add_weighted_edges_from([(0, 1, 9), (1, 2, 10), (2, 0, 0.1), (1, 4, 0.5), (4, 0, 0.00001)])
    >>> print(FindSmallCircle(G))
    [4, 0, 1, 4]

    >>> G = nx.DiGraph()
    >>> G.add_weighted_edges_from([(0, 1, 0.1), (1, 2, 10), (2, 0, 1), (2, 3, 10), (3, 4, 0.1), (4, 0, 0.00001)])
    >>> print(FindSmallCircle(G))
    [4, 0, 1, 2, 3, 4]

    >>> G = nx.DiGraph()
    >>> G.add_weighted_edges_from([(0, 1, 0.1), (1, 2, 10), (2, 0, 10), (1, 4, 10), (4, 0, 10)])
    >>> print(FindSmallCircle(G))
    []

    >>> G = nx.DiGraph()
    >>> G.add_weighted_edges_from([(0, 1, 10), (1, 2, 0.1), (2, 3, 10), (1, 4, 10), (4, 0, 10)])
    >>> print(FindSmallCircle(G))
    []


    """

    # Loop to transform the weights
    for u, v, weight in G.edges(data='weight'):
        G[u][v]['weight'] = math.log10(weight)

    # Trying to find negative cycle with builtin function *that I changed in order to cancel the raise exception
    try:
        return nx.find_negative_cycle(G, 0)
    except NetworkXNoCycle:
        return []


if __name__ == "__main__":
    # Creating a graph to demonstrate how it works example 1
    G = nx.DiGraph()
    G.add_weighted_edges_from([(0, 1, 9), (1, 2, 10), (2, 0, 0.1), (1, 4, 0.5), (4, 0, 0.00001)])

    # A lot of setting in order
    pos = {0: (0, 0), 1: (-1, 0.3), 2: (2, 0.17), 4: (7, 0.2)}
    options = {
        "font_size": 20,
        "node_size": 1500,
        "node_color": "white",
        "edgecolors": "blue",
        "linewidths": 2,
        "width": 5,
    }
    nx.draw_networkx(G, pos, **options)
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)

    # Set margins for the axes so that nodes aren't clipped
    ax = plt.gca()
    ax.margins(0.1)
    plt.axis("off")
    plt.show()

    # Example 2
    G = nx.DiGraph()
    G.add_weighted_edges_from([(0, 1, 0.1), (1, 2, 10), (2, 0, 1), (2, 3, 10), (3, 4, 0.1), (4, 0, 0.01)])
    pos = {0: (0, 0), 1: (-1, 0.3), 2: (2, 0.17), 3: (5, 0.5), 4: (7, 0.2)}

    nx.draw_networkx(G, pos, **options)
    nx.draw_networkx_edge_labels(G, pos, edge_labels)

    # Set margins for the axes so that nodes aren't clipped
    ax = plt.gca()
    ax.margins(0.1)
    plt.axis("off")
    plt.show()

    doctest.testmod()
