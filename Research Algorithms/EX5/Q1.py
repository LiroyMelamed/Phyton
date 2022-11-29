class bounded_subsets:
    def __init__(self, List, integer):
        self.List = List
        self.state = List[0]
        self.end = List[len(List)-1]
        self.step = 1
        OurSets =  self.bounded_subsets(List,integer)


    def __iter__(self):
        return self

    def __next__(self):
        if self.state >= self.end:
            raise StopIteration
        res = self.state
        self.state += self.step
        return res

    def bounded_subsets(self, List, integer):
        OurSets = []
