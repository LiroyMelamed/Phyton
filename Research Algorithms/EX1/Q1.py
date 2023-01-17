from typing import get_type_hints
import doctest

def f(x: int, y: float, z):
    return x + y + z

def safe_call(func, args: dict):
    '''
    >>> args = {"x": 5, "y": 3.14, "z": 2}
    >>> print(safe_call(f, args))
    10.14
    >>> args = {"x": 2, "y": 1.5, "z": 2.5}
    >>> print(safe_call(f, args))
    6.0
    '''
    hints = get_type_hints(func)
    for arg, value in args.items():
        if arg not in hints:
            continue
        if not isinstance(value, hints[arg]):
            raise Exception(f"Argument {arg} should be of type {hints[arg]}")
    return func(**args)


if __name__ == '__main__':
    doctest.testmod()