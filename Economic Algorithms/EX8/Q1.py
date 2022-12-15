class Person:
    def __init__(self, name: str, value: dict):
        self.name = name
        self.values = value

    def get_value(self, key):
        return self.values.get(key)

    def get_dict(self):
        return self.values

    def get_name(self):
        return self.name




def find_max(people: list, item):
    max = 0
    max_person = [""]
    for person in people:
        value = person.get_value(item)
        if person.get_value(item) > max:
            max = person.get_value(item)
            max_person[0] = person
    return max_person[0]

def auction(people: list):
    for item in people[0].values:
        max_person_for_item = find_max(people, item)
        index = people.index(max_person_for_item)
        people.pop(index)
        print(max_person_for_item.get_name() +" Gets item "+ item)


if __name__ == '__main__':
    liroy = Person("Liroy", {'a': 8 , 'b': 2 , 'c': 6})
    Barak = Person("Barak", {'a': 5, 'b': 3, 'c': 7})
    Lishai = Person("Lishai", {'a': 7, 'b': 5, 'c': 3})
    people= [liroy, Barak, Lishai]
    auction(people)
