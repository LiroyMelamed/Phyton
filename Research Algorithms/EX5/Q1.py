import copy
import doctest


class bounded_subsets:
    '''
    >>> for s in bounded_subsets([1,2,3], 4): print(s)
    [[], [1], [2], [3], [1, 2], [1, 3]]
    >>> for s in bounded_subsets(range(50,150), 103): print(s)
    [[], [50], [51], [52], [53], [54], [55], [56], [57], [58], [59], [60], [61], [62], [63], [64], [65], [66], [67], [68], [69], [70], [71], [72], [73], [74], [75], [76], [77], [78], [79], [80], [81], [82], [83], [84], [85], [86], [87], [88], [89], [90], [91], [92], [93], [94], [95], [96], [97], [98], [99], [100], [101], [102], [103], [50, 51], [50, 52], [50, 53], [51, 52]]
    '''

    # Constructor Of an Iterator
    def __init__(self, OurList, Max):
        # List of all the numbers that smaller or equal then Max
        self.List = []
        # Integer to print only one time
        self.state = 0
        # List of Lists that we will return
        self.OurSets = [[]]
        # For Loop to put in OurSets and List the correct number
        for Number in OurList:
            # Condition to put only the number that smaller then Max
            if Number <= Max:
                self.OurSets.append([Number])
                self.List.append(Number)
        # Function that creates all the subsets
        self.AllSubsets(self.OurSets, Max)

    def __iter__(self):
        return self

    def __next__(self):
        # Increase the state to print only once
        self.state += 1
        if self.state <= 1:
            # Returning OurSets after putting all the subsets
            return self.OurSets
        raise StopIteration

    # Function that find all the subsets
    def AllSubsets(self, OurSets, Max):
        # New Set
        CurrSet = []
        # For all of subsets that is found in the current set
        for SubSet in OurSets:
            # Sum of the current subset
            CurrSum = sum(SubSet)
            # Condition to check if the sum is bigger then the max and if it is - continue to the next subset
            if CurrSum >= Max:
                continue
            # For loop of every single number in our list of suitable number
            for SingleNum in self.List:
                # Condition that checks if the sum plus the suitable number is still smaller or equal to max
                if CurrSum + SingleNum <= Max and SingleNum not in SubSet: # and if the number not in the current subset
                    # NewSet = SubSet
                    NewSet = copy.deepcopy(SubSet)
                    # Putting the number in the new subset
                    NewSet.append(SingleNum)
                    # Ordinary sort
                    NewSet.sort()
                    if NewSet not in self.OurSets:
                        CurrSet.append(NewSet)
                        self.OurSets.append(NewSet)
            if len(CurrSet) != 0:
                # Recursion to the Set that we found
                self.AllSubsets(CurrSet, Max)


if __name__ == '__main__':
    doctest.testmod()
    for s in bounded_subsets([1, 2, 3], 4):
        print(s, end=" ")  # prints: [], [1], [2], [3], [1,2], [1,3].
    print()
    for s in bounded_subsets(range(50, 150), 103):
        print(s, end=" ")  # prints: [], [50], [51],..., [103], [50, 51], [50, 52], [50, 53], [51, 52]
    print()
