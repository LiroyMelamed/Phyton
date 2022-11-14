import doctest


# Global dictionary to save all the answers
listOfNumbers = {}


# Wrap is our "decorator" function
def lastcall(func):
    """
    "Decorator" function


    >>> f(1)
    The answer is 1


    >>> f(1)
    I already told you that the answer is 1 !

    >>> fun("a")
    The answer is aa

    >>> fun("a")
    I already told you that the answer is aa !

    >>> fu(1,3,5)
    The answer is 3.0

    >>> fu(1,3,5)
    I already told you that the answer is 3.0 !

    """
    # We get the argument that we put in our original function
    def wrapper(*args):
        x = args
        answer = func(*args)
        # If we already answer about this argument
        if x in listOfNumbers:
            print("I already told you that the answer is", listOfNumbers[x], "!")
        # The argument is in the dictionary
        else:
            # Print the answer
            print("The answer is", answer)
            # Adding the answer to the dictionary
            listOfNumbers[x] = answer

    return wrapper


# Function with int
@lastcall
def f(x: int):
    return x ** 2


# Function with str
@lastcall
def fun(x: str):
    return x + "a"


@lastcall
def fu(x: int, y: int, z: int):
    return (x + y + z) / 3


doctest.testmod()

print("- - - - - - - - - - - - - - - - -")
intToCheck = [1, 2, 3, 4, 5]
print("Lets check the int function")
print("- - - - - - - - - - - - - - - - -")
# Checking 1-5 in f function
for x in intToCheck:
    f(x)
    f(x)

print("- - - - - - - - - - - - - - - - -")
# Checking Str or single char
strToCheck = ["a", "b", "c", "d", "abc"]
print("Lets check the str function")
print("- - - - - - - - - - - - - - - - -")
# Checking the strTocheck arguments
for x in strToCheck:
    fun(x)
    fun(x)

print("- - - - - - - - - - - - - - - - -")
print("Lets check the 3 args function")
print("- - - - - - - - - - - - - - - - -")
fu(1, 2, 6)
fu(1, 2, 6)
fu(2, 4, 6)
fu(2, 4, 6)



