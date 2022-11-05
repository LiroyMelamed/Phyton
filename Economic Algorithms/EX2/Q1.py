# Creating class of agent with set function and get value function
class Agent:
    def __init__(self):
        self.options = {}
        self.options

    # Setting the value of a given option
    def set_option(self, option: int, value: int):
        self.options[option] = value

    # Getting the value of a given option
    def value(self, option: int) -> float:
        return self.options[option]


# Function that checks if option1 in a pareto improvement of option2.
def isParetoImprovement(agents: list[Agent], option1: int, option2: int) -> bool:
    bol = True

    # For every agent we will check if value option1 is smaller than the value of option2
    for agent in agents:
        if agent.value(option1) < agent.value(option2):
            # One of the value is smaller so option1 isn't a pareto improvement of option2.
            bol = False

    return bol

# Function that checks if option1 in a pareto optimal with the isParetoImprovement function.
def isParetoOptimal(agents: list[Agent], option: int, allOptions: list[int]) -> bool:
    bol = False
    # For every option we will check if it is a pareto improvement of the given option except itself.
    for i in allOptions:
        if i != option:
            bol = isParetoImprovement(agents, i, option)
            # if option number i is a pareto improvement of the given option so the given option is not pareto optimal.
            if bol:
                return False

    return True


# Setting the agents
liroy = Agent()
barak = Agent()
roi = Agent()

# Setting value to option number 1
liroy.set_option(1, 1)
barak.set_option(1, 3)
roi.set_option(1, 3)

# Setting value to option number 2
liroy.set_option(2, 2)
barak.set_option(2, 1)
roi.set_option(2, 5)

# Setting value to option number 3
liroy.set_option(3, 3)
barak.set_option(3, 2)
roi.set_option(3, 5)

# Setting a list to send to the function
a = [liroy, barak, roi]

# Setting a list of all options available
allOptions = [1, 2, 3]

# Title
print("")
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("Lets check which option is pareto improvement of which")
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - -")

# Loop to check every possible iteration of options
for i in allOptions:
    for j in allOptions:
        if i != j:
            pareto = isParetoImprovement(a, i, j)
            if pareto:
                print("Option number:", i, "is pareto improvement of option number: ", j)
            else:
                print("Option number:", i, "isn't pareto improvement of option number: ", j)

# Example           options - - - - 1 - - - - 2 - - - - 3 - - - -
#                   liroy   - - - - 1 - - - - 2 - - - - 3 - - - -
#                   barak   - - - - 3 - - - - 1 - - - - 2 - - - -
#                   roi     - - - - 3 - - - - 3 - - - - 5 - - - -

# Option number 3 is pareto improvement of option number 2.

# Title
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("    Lets check if the options are pareto optimal")
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - -")


for i in allOptions:
    paretoOpt = isParetoOptimal(a, i, allOptions)
    if paretoOpt:
        print("Option number:", i, "is pareto Optimal")
    else:
        print("Option number:", i, "isn't pareto Optimal")
