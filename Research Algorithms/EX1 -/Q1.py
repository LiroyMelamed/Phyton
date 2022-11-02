from inspect import signature

def arguments(all_arg):
    all_args_to_string = str(all_arg)
    splited_args = all_args_to_string[1:-1]
    return splited_args


def f(x:int,y:float,z):
    return x+y+z


def safe_call(*args):
    sig = signature(args[0])
    arguments=str(sig)
    arguments = arguments[1:-1]
    arguments = arguments.split(",")
    arguments_count = len(arguments)
    if arguments_count != (len(args)-1): #Not the same number of variables
        raise Exception("Unfitable arguments.")
    else:
        # Fitable arguments
        counter = 1
        for parameter in parm:
            print(parameter)
            temp = parameter.split(":")
            if len(temp) == 2:
                type1 = temp[1].strip()
                check = str(type(args[counter]))
                check=check[1:-1]
                check=check.split(" ")
                check1 = check[1]
                check1=check1[1:-1]

                #Checking if every argument is the same as the function.
                if type1 != check1:
                    raise Exception("Unfitable arguments.")
            counter = counter + 1

    #Returning The function
    only_args = args[1:]
    return f(*only_args)

def main():
    print(safe_call(f,5,7.0,6))


if __name__ == '__main__':
    main()