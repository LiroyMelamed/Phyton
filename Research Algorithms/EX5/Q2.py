import networkx as nx
import doctest
from typing import Callable, Any


def FindPath(algorithm: Callable, input: Any, output=str):
    """
    algorithm = bfs or dfs
    output = 'length' or path
    inp = tuple or list:
        tuple = tuple of two ints represents src and dst and the graph
        list = list of two strings represents the integers of src and dst and the graph
    >>> g = nx.Graph()
    >>> g.add_nodes_from(range(1, 11))
    >>> g.add_edge(1, 2)
    >>> g.add_edge(2, 3)
    >>> g.add_edge(3, 4)
    >>> g.add_edge(4, 5)
    >>> g.add_edge(5, 6)
    >>> g.add_edge(6, 7)
    >>> g.add_edge(7, 8)
    >>> g.add_edge(8, 9)
    >>> g.add_edge(9, 10)
    >>> g.add_edge(1, 5)
    >>> g.add_edge(1, 2)

    >>> FindPath(bfs, [1,4,g], 'path' )
    [1, 5, 4]
    >>> g.add_edge(1, 4)
    >>> FindPath(bfs,[1,4,g], 'path')
    [1, 4]
    >>> FindPath(bfs,[1,10,g], 'path')
    [1, 5, 6, 7, 8, 9, 10]
    >>> g.remove_edge(1,4)
    >>> FindPath(dfs, [1,4,g], 'path')
    [1, 5, 4]
    >>> g.add_edge(1, 4)
    >>> FindPath(dfs, [1,4,g], 'path')
    [1, 4]
    >>> FindPath(dfs,[1,10,g], 'path')
    [1, 5, 6, 7, 8, 9, 10]
    >>> g.remove_edge(1,4)
    >>> FindPath(bfs, (1,4,g), 'length')
    3
    >>> g.add_edge(1, 4)
    >>> FindPath(bfs,(1,4,g), 'length')
    2
    >>> FindPath(bfs,(1,10,g), 'length')
    7
    >>> g.remove_edge(1,4)
    >>> FindPath(dfs,(1,4,g), 'length')
    3
    >>> g.add_edge(1, 4)
    >>> FindPath(dfs, (1,4,g), 'length')
    2
    >>> FindPath(dfs, (1,10,g), 'length')
    7
    """
    try:
        if isinstance(input, tuple):
            src = input[0]
            dst = input[1]
        elif isinstance(input, list):
            src = int(input[0])
            dst = int(input[1])
        else:
            raise "Invalid Input"

        G = input[2]

    except:
        raise "Invalid Input"

    try:
        if output == "length":
            return len(algorithm(src, dst, G.neighbors))
        elif output == "path":
            return algorithm(src, dst, G.neighbors)
        else:
            raise "Invalid Input"
    except:
        raise "Invalid Input"

def bfs(start:Any,end:Any,neghibor_function):
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
        #if we found path to "end" during the loop
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




def dfs(start:Any,end:Any,neghibor_function):
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
        #if we found path to "end" during the loop
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