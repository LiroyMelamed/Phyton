from collections import OrderedDict
from unittest.util import sorted_list_difference



def print_sorted(x):
    list_to_sort = {}
    for y in x:
        if isinstance(x[y],int):
            list_to_sort[y] = x[y]

        elif isinstance(x[y], list):
            x[y].sort()
            list_to_sort[y] = x[y]

        elif isinstance(x[y], str):
            str_list = sorted(x[y])
            new_str = ''.join(str_list)
            list_to_sort[y] = new_str

    sorted_list = {}
    for key in sorted(list_to_sort):
        sorted_list[key] = list_to_sort[key]
        
    print(sorted_list)




def main():
    x = {"a": 5, "c": 6, "b": [1, 3, 2, 4], "d": "acbd"}
    print_sorted(x)

if __name__ == '__main__':
    main()