from collections import OrderedDict
from unittest.util import sorted_list_difference


def sort_dic(x):
    list_to_sort = {}
    for y in x:
        for val in y:
            if isinstance(y[val], int):
                list_to_sort[val] = y[val]

            elif isinstance(y[val], list):
                y[val].sort()
                list_to_sort[val] = y[val]

            elif isinstance(y[val], str):
                str_list = sorted(y[val])
                new_str = ''.join(str_list)
                list_to_sort[val] = new_str

            elif isinstance(y[val], set):
                str_list = sorted(y[val])
                list_to_sort[val] = str_list

            elif isinstance(y[val], dict):
                new_dic = [y[val]]
                dic = sort_dic(new_dic)
                list_to_sort[val] = dic

    sorted_list = {}
    for key in sorted(list_to_sort):
        sorted_list[key] = list_to_sort[key]

    return sorted_list

def print_sorted(x) -> dict:
    dictionary = x
    list_to_sort = {}
    for y in dictionary:
        if isinstance(x[y],int):
            list_to_sort[y] = x[y]

        elif isinstance(x[y], list):
            x[y].sort()
            list_to_sort[y] = x[y]

        elif isinstance(x[y], str):
            str_list = sorted(x[y])
            new_str = ''.join(str_list)
            list_to_sort[y] = new_str

        elif isinstance(x[y], set):
            str_list = sorted(x[y])
            list_to_sort[y] = str_list
        
        elif isinstance(x[y], dict):
            new_dic = [x[y]]
            dic = sort_dic(new_dic)
            list_to_sort[y] = dic

    sorted_list = {}
    for key in sorted(list_to_sort):
        sorted_list[key] = list_to_sort[key]
        
    print(sorted_list)




def main():
    x = {"a": 5, "c": 6, "b": [1, 3, 2, 4], "d": "acbd", "f":{"a": 5, "c": 6,"b":{"apple", "banana", "cherry"}, "d": "acbd"}}
    print_sorted(x)

if __name__ == '__main__':
    main()