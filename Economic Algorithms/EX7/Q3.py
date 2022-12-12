import doctest
import random


def MaxBenefit(lst):
    """
    Function that find the Maximum benefit og player number one in the tender algorithm

    >>> MaxBenefit([98, 89, 262, 34, 60, 469, 484])
    (485, 213.71428571428572)

    >>> MaxBenefit([198, 235, 75, 234, 376, 200, 366])
    (1, 240.57142857142858)

    >>> MaxBenefit([353, 422, 131, 15, 218, 5, 317])
    (423, 208.71428571428572)

    """
    MaximunValue = 0
    SumOfValues = 0
    for Value in lst:
        if Value == lst[0]:
            SumOfValues += Value
            continue
        SumOfValues += Value
        if MaximunValue < Value:
            MaximunValue = Value
    Benefit = MaximunValue - (SumOfValues/len(lst))
    if Benefit > (SumOfValues/len(lst))-1:
        return MaximunValue+1, (SumOfValues/len(lst))
    else:
        return 1, (SumOfValues/len(lst))

if __name__ == "__main__":
    doctest.testmod()

    ListOfValues = []
    for i in range(0, 7):
        n = random.randint(1, 500)
        ListOfValues.append(n)
    print(f'Our list of values: {ListOfValues}')
    print(f'The value that player one need to change to: {MaxBenefit(ListOfValues)[0]}')
    print(f'The money that split between every player: {MaxBenefit(ListOfValues)[1]}')
    if (MaxBenefit(ListOfValues)[0]-MaxBenefit(ListOfValues)[1]) < 0:
        print(f'The benefit of player one:{MaxBenefit(ListOfValues)[1]-1}')
    else:
        print(f'The benefit of player one: {MaxBenefit(ListOfValues)[0]-MaxBenefit(ListOfValues)[1]}\n')