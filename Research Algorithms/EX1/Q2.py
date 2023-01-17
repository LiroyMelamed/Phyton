from collections import deque
import doctest


def four_neighbor_function(node: any) -> list:
    (x, y) = node
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

def three_dimensional_neighbor_function(node: any) -> list:
    (x, y, z) = node
    return [(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)]


def breadth_first_search(start, end, neighbor_function):
    '''
    >>> breadth_first_search(start=(0, 0), end=(-1, 0), neighbor_function=four_neighbor_function)
    [(0, 0), (-1, 0)]
    >>> breadth_first_search(start=(0, 0, 0), end=(-1, 0, 0), neighbor_function=three_dimensional_neighbor_function)
    [(0, 0, 0), (-1, 0, 0)]
    >>> breadth_first_search(start=(0, 0, 0), end=(-2, 0, 1), neighbor_function=three_dimensional_neighbor_function)
    [(0, 0, 0), (-1, 0, 0), (-2, 0, 0), (-2, 0, 1)]
    '''
    queue = deque()
    queue.append(start)
    visited = set()
    visited.add(start)
    parent = {start: None}
    while queue:
        node = queue.popleft()
        if node == end:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]
        for neighbor in neighbor_function(node):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)

if __name__ == '__main__':
    doctest.testmod()

