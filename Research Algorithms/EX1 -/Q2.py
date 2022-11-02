from math import degrees


def four_neighbor_function(node: any) -> list:
    (x, y) = node
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


def breadth_first_search(start, end, neighbor_function) -> list:
    x = start
    y = [x]
    words = []
    while x != end:
        neighbor = neighbor_function(x)
        for neigh in neighbor:
            #For example from (0,0) -> (0,1) --  y0<y1 the x is equal in both points
            if end[0] == start[0] and end[1] > start[1]:
                if x[0] == neigh[0] and x[1] < neigh[1] <= end[1]:
                    if neigh == end:
                        x=neigh
                        y.append(x)
                        words.append("Up")
                        break

                    x=neigh
                    y.append(x)
                    words.append("Up")
            
            #For example from (0,0) -> (1,0) --  x0<x1 the y is equal in both points
            if end[0] > start[0] and end[1] == start[1]:
                if neigh[0] > x[0] and neigh[1] == x[1]:
                    if neigh == end:
                        x = neigh
                        y.append(x)
                        words.append("Right")
                        break
                    x = neigh
                    y.append(x)
                    words.append("Right")

            #For example from (0,0) -> (1,1) --  y0>y1 the x is equal in both points
            if end[0] > start[0] and end[1] > start[1]:
                if x[0] < neigh[0] <= end[0] and neigh[1] == x[1]:
                    x = neigh
                    y.append(x)
                    words.append("Right")
                if x[0] == end[0] and x[1] < end[1]:
                    if x[1] < neigh[1] <= end[1] and neigh[0] == x[0]:
                        if neigh == end:
                            x = neigh
                            y.append(x)
                            words.append("Up")
                            break
                        x = neigh
                        y.append(x)
                        words.append("Up")

            #For example from (0,1) -> (0,0) --  y0>y1 the x is equal in both points
            if end[0] == start[0] and end[1] < start[1]:
                if x[0] == neigh[0] and x[1] > neigh[1] >= end[1]:
                    if neigh == end:
                        x=neigh
                        y.append(x)
                        words.append("Down")
                        break

                    x=neigh
                    y.append(x)
                    words.append("Down")

            #For example from (0,1) -> (1,0) --  y1>y0 && x1<x0
            if end[0] > start[0] and end[1] < start[1]:
                if x[0] < neigh[0] <= end[0] and neigh[1] == x[1]:
                    x = neigh
                    y.append(x)
                    words.append("Up")
                if x[0] == end[0] and x[1] > end[1]:
                    if neigh[1] < x[1] and neigh[0] == x[0] and neigh[1] <= end[1]:
                        if neigh == end:
                            x = neigh
                            y.append(x)
                            words.append("Left")
                            break
                        x = neigh
                        y.append(x)
                        words.append("Left")

            #For example from (1,0) -> (0,0) -- x1>x0 and the y is equal in both points
            if end[0] < start[0] and end[1] == start[1]:
                if x[0] > neigh[0] >= end[0] and neigh[1] == x[1]:
                    if neigh == end:
                        x = neigh
                        y.append(x)
                        break
                    x = neigh
                    y.append(x)
                    words.append("Down")

            #For example from (1,0) -> (0,1) --  y1<y0 && x1>x0
            if end[0] < start[0] and end[1] > start[1]:
                if neigh[0] == x[0] and x[1] < neigh[1] <= end[1]:
                    if neigh == end:
                        x = neigh
                        y.append(x)
                        words.append("Up")
                        break
                    x = neigh
                    y.append(x)
                    words.append("Up")

                if x[1] == neigh[1] and x[0] > neigh[0] >= end[0]:
                    x = neigh
                    y.append(x)
                    words.append("Left")

            #For example from (1,1) -> (0,0) --  y1>y0 && x1>x0
            if end[0] < start[0] and end[1] < start[1]:
                if x[0] > neigh[0] >= end[0] and neigh[1] == x[1]:
                    x = neigh
                    y.append(x)
                    words.append("Down")
                if x[0] == neigh[0] and x[1] > neigh[1] >= end[1]:
                    if neigh == end:
                        x = neigh
                        y.append(x)
                        words.append("Left")
                        break
                    x = neigh
                    y.append(x)
                    words.append("Left")

    print(words)
    return y


def main():
    Ex1 = breadth_first_search(start=(0, 0), end=(-1, 0), neighbor_function=four_neighbor_function)
    print(Ex1)
    for points in Ex1:
        print(points, end=" ")
        if points == Ex1[len(Ex1)-1]:
            print("")
        else:
            print("->", end=" ")


if __name__ == '__main__':
    main()
