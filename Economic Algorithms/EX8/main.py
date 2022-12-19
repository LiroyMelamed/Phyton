class Person:
    # Person class to store all the important things
    def __init__(self, name: str, value: dict):
        self.name = name # name of player
        self.values = value # values of the player for each option
        self.valueWithOut = 0 # init the value of the option without the player
        self.payment = 0 # init the payment of the player

    ###### getter ######
    def get_value(self, key):
        return self.values.get(key)

    def get_dict(self):
        return self.values

    def get_name(self):
        return self.name

    def get_valueWithOut(self):
        return self.valueWithOut

    def get_payment(self):
        return self.payment

    ###### setter ######
    def set_valueWithOut(self, sub):
        self.valueWithOut = sub

    def set_payment(self, payment):
        self.payment = payment

# Function to find the max sum of the options
def find_max(people: list, options: list):
    max = 0
    current_option = [""]
    # loop of each option
    for option in options:
        temp = 0
        # loop for each person
        for person in people:
            # temp is the sum of all person value of the current option
            temp += person.get_value(option)
        # Checks if the sum of the currect option is the max
        if temp > max:
            max = temp
            current_option[0] = option
    # returning the option with the max sum and the sum
    return (current_option[0], max)

# Function to find the value of the max option without the player value
def find_max_without(person, option, sum_of_option):
    sub_option = sum_of_option - person.get_value(option)
    person.set_valueWithOut(sub_option)

# Function to find the paymnt of the player
def find_payment(people: list , index_of_person):
    new_list = []
    # Putting in the list the players without the current player
    for i in range(0, len(people)):
        if i != index_of_person:
            new_list.append(people[i])
    # returning the max option without the current player value
    max_opt_without = find_max(new_list, new_list[0].values)
    return max_opt_without[1]

#Function to start the auction
def auction(people: list):
    # Finding the option with the max sum
    max_option = find_max(people, people[0].values)
    # loop of person
    for person in people:
        # Finding the value of max option without that person
        find_max_without(person, max_option[0], max_option[1])
        # index to know the person index in the people list
        index = people.index(person)
        # Finding the payment of this player
        max_without = find_payment(people, index)
        payment = max_without - person.get_valueWithOut()
        person.set_payment(payment)
    return max_option[0]


if __name__ == '__main__':
    liroy = Person("Liroy", {'a': 8 , 'b': 4 , 'c': 3})
    Barak = Person("Barak", {'a': 5, 'b': 8, 'c': 1})
    Lishai = Person("Lishai", {'a': 3, 'b': 5, 'c': 3})
    people= [liroy, Barak, Lishai]
    max_option = auction(people)
    print("The chocen option is "+max_option[0])

    for person in people:
        benefit = person.get_dict().get(max_option[0]) - person.payment
        print(person.get_name() + " need to pay " + str(person.get_payment())+ " and his benefit is " + str(benefit))
