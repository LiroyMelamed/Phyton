

class List(list):
    def __getitem__(self, index):
        if not isinstance(index, int):
            output = list(self)
        else:
            return list(self)[index]
        for key in index:
            output = output[key]
        return output

# Example from the class
mylist = List([[[1,2,3,33],[4,5,6,66]],[[7,8,9,99],[10,11,12,122]],[[13,14,15,155],[16,17,18,188]]])
# Should print 66
print(f"Checking number in a selected row")
print(mylist[0, 1, 3], "\n")
# Should print [[1, 2, 3, 33], [4, 5, 6, 66]]
print(f"Checking specific row")
print(mylist[0], "\n")
# Should print [[[1, 2, 3, 33], [4, 5, 6, 66]], [[7, 8, 9, 99], [10, 11, 12, 122]], [[13, 14, 15, 155], [16, 17, 18, 188]]]
print(f"Checking the whole list")
print(mylist)
