from inspect import signature

def arguments(all_arg):
    all_args_to_string = str(all_arg)
    splited_args = all_args_to_string[1:-1]
    return splited_args


def f(x:int,y:float,z):
    return x+y+z


def safe_call(*args):
    sig = signature(args[0])
    parm_count = len(parm)
    print(parm_count)

    if parm_count != (len(args)-1):
        raise Exception("Sorry, the parameters entered do not match the parameters of the function entered ")
    else:
        # the number of parameters are equal
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

                if type1 != check1:
                    raise Exception("Sorry, the parameters entered do not match the parameters of the function entered ")
            counter = counter + 1

    only_args = args[1:]
    return f(*only_args)

def main():
    print(safe_call(f,5,7.0,6))


if __name__ == '__main__':
    main()