import copy
import doctest


class bounded_subsets:
    '''
    >>> subsets = bounded_subsets([1,2,3], 4)
    >>> print(", ".join(str(s) for s in subsets))
    [], [1], [2], [3], [1, 2], [1, 3]
    >>> subsets = bounded_subsets(range(50,150), 103)
    >>> print(", ".join(str(s) for s in subsets))
    [], [50], [51], [52], [53], [54], [55], [56], [57], [58], [59], [60], [61], [62], [63], [64], [65], [66], [67], [68], [69], [70], [71], [72], [73], [74], [75], [76], [77], [78], [79], [80], [81], [82], [83], [84], [85], [86], [87], [88], [89], [90], [91], [92], [93], [94], [95], [96], [97], [98], [99], [100], [101], [102], [103], [50, 51], [50, 52], [50, 53]
    >>> subsets = zip(range(5), bounded_subsets(range(100), 1000000000000))
    >>> print(", ".join(str(s) for s in subsets))
    (0, []), (1, [0]), (2, [1]), (3, [2]), (4, [3])
    '''

    # Constructor Of an Iterator
    def __init__(self, OurList, Max):
        self.List = []
        self.OurSets = [[]]
        for Number in OurList:
            if Number <= Max:
                self.List.append(Number)
        self.AllSubsets(self.OurSets, Max)
        self.iter_index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.iter_index += 1
        if self.iter_index < len(self.OurSets):
            return self.OurSets[self.iter_index]
        raise StopIteration

    # Function that find all the subsets
    def AllSubsets(self, OurSets, Max):
        # New Set
        CurrSet = []
        # For all the subsets that is found in the current set
        for SubSet in OurSets:
            # Sum of the current subset
            CurrSum = sum(SubSet)
            # Condition to check if the sum is bigger then the max and if it is - continue to the next subset
            if CurrSum >= Max:
                continue
            # For loop of every single number in our list of suitable number
            for SingleNum in self.List:
                # Condition that checks if the sum plus the suitable number is still smaller or equal to max
                if CurrSum + SingleNum <= Max and SingleNum not in SubSet:  # and if the number not in the current subset
                    # NewSet = SubSet
                    NewSet = copy.deepcopy(SubSet)
                    # Putting the number in the new subset
                    NewSet.append(SingleNum)
                    # Ordinary sort
                    NewSet.sort()
                    if NewSet not in self.OurSets:
                        CurrSet.append(NewSet)
                        self.OurSets.append(NewSet)
            if not CurrSet:
                return
            # Recursion to the Set that we found
            current_length = len(self.OurSets)
            self.AllSubsets(CurrSet, Max)
            if current_length == len(self.OurSets):
                return


if __name__ == '__main__':
    doctest.testmod()
