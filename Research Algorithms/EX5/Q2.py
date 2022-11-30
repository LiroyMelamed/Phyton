import networkx as nx
import doctest
from typing import Callable, Any


# The function working as a program and can get 2 different algorithms 2 different type of input and 2 different of output
def FindPath(algorithm: Callable, input: Any, output=str):
    """
    My Function get an algorithmm, an input and output
    The algotithms that my function can get is bfs or dfs
    The input that my function can get is a tuple or a list
    The output that my fuction can get is path or length

    'Creating a graph with networx'
    >>> graph = nx.Graph()
    >>> graph.add_nodes_from(range(1, 9))
    >>> graph.add_edge(1, 2)
    >>> graph.add_edge(2, 3)
    >>> graph.add_edge(3, 4)
    >>> graph.add_edge(4, 5)
    >>> graph.add_edge(5, 6)
    >>> graph.add_edge(6, 7)
    >>> graph.add_edge(7, 8)
    >>> graph.add_edge(1, 3)
    >>> graph.add_edge(1, 6)

    'Checking variet algorithms, input and outputs'
    >>> FindPath(bfs,(1,4,graph), 'path')
    [1, 3, 4]
    >>> FindPath(bfs, [1,5,graph], 'path' )
    [1, 6, 5]
    >>> FindPath(dfs,[1,7,graph], 'path')
    [1, 6, 7]
    >>> FindPath(dfs,[1,8,graph], 'path')
    [1, 6, 7, 8]

    >>> FindPath(bfs,(1,4,graph), 'length')
    3
    >>> FindPath(dfs, (1,5,graph), 'length')
    3
    >>> FindPath(dfs,(1,7,graph), 'length')
    3
    >>> FindPath(bfs,(1,8,graph), 'length')
    4
    """

    # Checking the input type and split use it as needed
    try:
        # input type is tuple
        if isinstance(input, tuple):
            src = input[0]
            dst = input[1]
        # input type is list
        elif isinstance(input, list):
            src = int(input[0])
            dst = int(input[1])
        else:
            raise "Invalid Input"

        # Our graph will be found in the last place after the src and dst
        Graph = input[2]

    except:
        raise "Invalid Input"

    # Checking the output type that was inserted
    try:
        # output str
        if output == "length":
            return len(algorithm(src, dst, Graph.neighbors))
        elif output == "path":
            return algorithm(src, dst, Graph.neighbors)
        else:
            raise "Invalid Input"
    except:
        raise "Invalid Input"


# Both algorithms were taken from the internet and changed
def bfs(start: Any, end: Any, neghibor_function):
    # initalize help lists
    visited = []
    queue = []
    parents = {}

    visited.append(start)
    queue.append(start)
    # while the queue is not empty
    while queue:
        tmp = queue.pop(0)
        # iterate over tmp's neghibors
        for neghibor in neghibor_function(tmp):
            if neghibor == end:
                parents[neghibor] = tmp
                break
            if neghibor not in visited:
                parents[neghibor] = tmp
                visited.append(neghibor)
                queue.append(neghibor)
        # if we found path to "end" during the loop
        if end in parents.keys():
            break
    # if there is no way between start to end
    if end not in parents.keys():
        return []
    # restore the path between start t end
    tmp = end
    path = [end]
    while parents[tmp] != start:
        path.append(parents[tmp])
        tmp = parents[tmp]
    path.append(start)
    return path[::-1]


def dfs(start: Any, end: Any, neghibor_function):
    # initalize help lists
    visited = []
    stack = []
    parents = {}

    visited.append(start)
    stack.append(start)
    # while the queue is not empty
    while stack:
        tmp = stack.pop()
        # iterate over tmp's neghibors
        for neghibor in neghibor_function(tmp):
            if neghibor == end:
                parents[neghibor] = tmp
                break
            if neghibor not in visited:
                parents[neghibor] = tmp
                visited.append(neghibor)
                stack.append(neghibor)
        # if we found path to "end" during the loop
        if end in parents.keys():
            break
    # if there is no way between start to end
    if end not in parents.keys():
        return []
    # restore the path between start t end
    tmp = end
    path = [end]
    while parents[tmp] != start:
        path.append(parents[tmp])
        tmp = parents[tmp]
    path.append(start)
    return path[::-1]


if __name__ == '__main__':
    doctest.testmod()
