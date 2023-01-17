import copy
import doctest


class bounded_subsets:
    '''
    >>> subsets = bounded_subsets(range(50,150), 103)
    >>> print(", ".join(str(s) for s in subsets))
    [], [103], [102], [101], [100], [99], [98], [97], [96], [95], [94], [93], [92], [91], [90], [89], [88], [87], [86], [85], [84], [83], [82], [81], [80], [79], [78], [77], [76], [75], [74], [73], [72], [71], [70], [69], [68], [67], [66], [65], [64], [63], [62], [61], [60], [59], [58], [57], [56], [55], [54], [53], [52], [51], [51, 52], [50], [50, 53], [50, 52], [50, 51]
    '''

    # Constructor Of an Iterator
    def __init__(self, OurList, Max):
        self.OurList = OurList
        self.Max = Max
        self.OurSets = []
        self.generate_subsets(0, [])

    def generate_subsets(self, index, subset):
        if sum(subset) > self.Max:
            return
        if index == len(self.OurList):
            self.OurSets.append(subset)
            return
        self.generate_subsets(index + 1, subset)
        self.generate_subsets(index + 1, subset + [self.OurList[index]])

    def __iter__(self):
        self.iter_index = -1
        return self

    def __next__(self):
        self.iter_index += 1
        if self.iter_index < len(self.OurSets):
            return self.OurSets[self.iter_index]
        raise StopIteration


if __name__ == '__main__':
    doctest.testmod()
