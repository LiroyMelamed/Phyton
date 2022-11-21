import math
from matplotlib import pyplot as plt


class Player:
    def __init__(self):
        self.Work = []

    def value(self):
        total = 0
        for work in self.Work:
            total += work
        return total

    def put(self, integer):
        self.Work.append(integer)


def GreedyAlgo(Players, Works):
    for Singlework in Works:
        MinPlayer = getMinPlayer(Players)
        MinPlayer.put(Singlework)

def getMinPlayer(Players):
    MinPlayer = Players[0]
    for SinglePlayer in Players:
        if SinglePlayer.value() < MinPlayer.value():
            MinPlayer = SinglePlayer
    return MinPlayer

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("############ Part A ############", "\n")
    print("Lets take 4 players and 8 objects")
    Liroy = Player()
    Raz = Player()
    Lishai = Player()
    Barak = Player()
    Work = [8, 7, 6, 6, 5, 2, 2, 2]
    Best1 = 10
    Players = [Liroy, Raz, Lishai, Barak]
    GreedyAlgo(Players, Work)
    print(Liroy.Work, "=", Liroy.value())
    print(Raz.Work, "=", Raz.value())
    print(Lishai.Work, "=", Lishai.value())
    print(Barak.Work, "=", Barak.value())
    print("The approximation ratio", Lishai.value() / Best1, "\n")
    print("Lets take 2 players and 7 objects")
    Work2 = [7, 6, 5, 4, 3, 3, 2]
    Liroy = Player()
    Raz = Player()
    Best2 = 15
    Players2 = [Liroy, Raz]
    GreedyAlgo(Players2, Work2)
    print(Liroy.Work, "=", Liroy.value())
    print(Raz.Work, "=", Raz.value())
    print("The approximation ratio", Liroy.value() / Best2, "\n")

    print("Lets take 2 players and 5 objects")
    Work3 = [7, 6, 5, 4, 5]
    Liroy = Player()
    Raz = Player()
    Best3 = 14
    Players3 = [Liroy, Raz]
    GreedyAlgo(Players3, Work3)
    print(Liroy.Work, "=", Liroy.value())
    print(Raz.Work, "=", Raz.value())
    print("The approximation ratio", Liroy.value() / Best3, "\n")




    print("############ Part B ############", "\n")
    print("Lets take 4 players and 4 objects")
    Liroy = Player()
    Raz = Player()
    Lishai = Player()
    Barak = Player()
    Work1 = [7,7,6,6]
    Best = 7
    Players1 = [Liroy, Raz, Lishai, Barak]
    GreedyAlgo(Players1, Work1)
    print("The approximation ratio", Liroy.value()/Best, "\n")

    print("Lets take 4 players and 5 objects")
    Liroy = Player()
    Raz = Player()
    Lishai = Player()
    Barak = Player()
    Work1 = [7,7,6,6,5]
    Best1 = 11
    Players1 = [Liroy, Raz, Lishai, Barak]
    GreedyAlgo(Players1, Work1)
    print("The approximation ratio", Lishai.value()/Best1, "\n")

    print("Lets take 4 players and 6 objects")
    Liroy = Player()
    Raz = Player()
    Lishai = Player()
    Barak = Player()
    Work1 = [7,7,6,6,5,5]
    Best1 = 11
    Players1 = [Liroy, Raz, Lishai, Barak]
    GreedyAlgo(Players1, Work1)
    print("The approximation ratio", Barak.value()/Best1, "\n")

    print("Lets take 4 players and 7 objects")
    Liroy = Player()
    Raz = Player()
    Lishai = Player()
    Barak = Player()
    Work1 = [7,7,6,6,5,5,4]
    Best1 = 11
    Players1 = [Liroy, Raz, Lishai, Barak]
    GreedyAlgo(Players1, Work1)
    print("The approximation ratio", Liroy.value()/Best1, "\n")

    print("Lets take 4 players and 8 objects")
    Liroy = Player()
    Raz = Player()
    Lishai = Player()
    Barak = Player()
    Work1 = [7,7,6,6,5,5,4,4]
    Best1 = sum(Work1)/4
    Players1 = [Liroy, Raz, Lishai, Barak]
    GreedyAlgo(Players1, Work1)
    print("The approximation ratio", Liroy.value()/Best1, "\n")

    print("Lets take 4 players and 9 objects")
    Liroy = Player()
    Raz = Player()
    Lishai = Player()
    Barak = Player()
    Work1 = [7,7,6,6,5,5,4,4,4]
    Best1 = sum(Work1)/4
    Players1 = [Liroy, Raz, Lishai, Barak]
    GreedyAlgo(Players1, Work1)
    print("The approximation ratio", Liroy.value()/math.ceil(Best1), "\n")

    print("Lets take 4 players and 10 objects")
    Liroy = Player()
    Raz = Player()
    Lishai = Player()
    Barak = Player()
    Work1 = [7,7,6,6,5,5,4,4,4,3]
    Best1 = sum(Work1)/4
    Players1 = [Liroy, Raz, Lishai, Barak]
    GreedyAlgo(Players1, Work1)
    print("The approximation ratio", Liroy.value()/math.ceil(Best1), "\n")

    print("Lets take 4 players and 11 objects")
    Liroy = Player()
    Raz = Player()
    Lishai = Player()
    Barak = Player()
    Work1 = [7,7,6,6,5,5,4,4,4,3,3]
    Best1 = sum(Work1)/4
    Players1 = [Liroy, Raz, Lishai, Barak]
    GreedyAlgo(Players1, Work1)
    print("The approximation ratio", Liroy.value()/math.ceil(Best1), "\n")

    print("Lets take 4 players and 12 objects")
    Liroy = Player()
    Raz = Player()
    Lishai = Player()
    Barak = Player()
    Work1 = [7,7,6,6,5,5,4,4,4,3,3,2]
    Best1 = sum(Work1)/4
    Players1 = [Liroy, Raz, Lishai, Barak]
    GreedyAlgo(Players1, Work1)
    print("The approximation ratio", Liroy.value()/math.ceil(Best1), "\n")

    print("Lets take 4 players and 13 objects")
    Liroy = Player()
    Raz = Player()
    Lishai = Player()
    Barak = Player()
    Work1 = [7,7,6,6,5,5,4,4,4,3,3,2,2]
    Best1 = sum(Work1)/4
    Players1 = [Liroy, Raz, Lishai, Barak]
    GreedyAlgo(Players1, Work1)
    print("The approximation ratio", Liroy.value()/math.ceil(Best1), "\n")

    print("Lets take 4 players and 14 objects")
    Liroy = Player()
    Raz = Player()
    Lishai = Player()
    Barak = Player()
    Work1 = [7,7,6,6,5,5,4,4,4,3,3,2,2,2]
    Best1 = sum(Work1)/4
    Players1 = [Liroy, Raz, Lishai, Barak]
    GreedyAlgo(Players1, Work1)
    print("The approximation ratio", Raz.value()/Best1, "\n")

    print("Lets take 4 players and 15 objects")
    Liroy = Player()
    Raz = Player()
    Lishai = Player()
    Barak = Player()
    Work1 = [7,7,6,6,5,5,4,4,4,3,3,2,2,2,2]
    Best1 = sum(Work1)/4
    Players1 = [Liroy, Raz, Lishai, Barak]
    GreedyAlgo(Players1, Work1)
    print("The approximation ratio", Raz.value()/Best1, "\n")


    plt.scatter(4,1.0)
    plt.scatter(5,1.0)
    plt.scatter(6,1.0)
    plt.scatter(7,1.0)
    plt.scatter(8,1.0)
    plt.scatter(9,1.25)
    plt.scatter(10,1.15)
    plt.scatter(11,1.08)
    plt.scatter(12,1.07)
    plt.scatter(13,1.067)
    plt.scatter(14,1.06)
    plt.scatter(15,1.03)

    plt.xlabel('Number of Objects')
    plt.show()















