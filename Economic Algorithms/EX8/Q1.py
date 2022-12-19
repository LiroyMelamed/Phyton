class Person:
    def __init__(self, name: str, value: dict):
        self.name = name
        self.values = value
        self.valueWithOut = 0

    def get_value(self, key):
        return self.values.get(key)

    def get_dict(self):
        return self.values

    def get_name(self):
        return self.name

    def set_valueWithOut(self, sub):
        self.valueWithOut = sub


def find_max(people: list, options: list):
    max = 0
    current_option = [""]
    for option in options:
        temp = 0
        for person in people:
            temp += person.get_value(option)
        if temp > max:
            current_option[0] = option
    return (current_option[0], max)

def find_max_without(person, option, sum_of_option):
    sub_option = sum_of_option - person.get_value(option)
    person.set_valueWithOut(sub_option)

# def find_payment():


def auction(people: list):
    max_option = find_max(people, people[0].values)
    for person in people:
        find_max_without(person, max_option[0], max_option[1])
    print(max_option)


if __name__ == '__main__':
    liroy = Person("Liroy", {'a': 8 , 'b': 2 , 'c': 6})
    Barak = Person("Barak", {'a': 7, 'b': 6, 'c': 7})
    Lishai = Person("Lishai", {'a': 7, 'b': 5, 'c': 3})
    people= [liroy, Barak, Lishai]
    auction(people)
