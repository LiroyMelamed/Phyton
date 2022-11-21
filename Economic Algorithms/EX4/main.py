import matplotlib.pyplot as plt

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
    print("Lets take 6 players and 9 objects")
    Liroy = Player()
    Raz = Player()
    Lishai = Player()
    Barak = Player()
    Roi = Player()
    Daniel = Player()
    Players4 = [Liroy, Raz, Lishai, Barak, Roi, Daniel]
    Work4 = [9,9,7,7,6,6,5,5,4,4,4]
    GreedyAlgo(Players4, Work4)
    Best4 = 12
    print("The approximation ratio", Liroy.value()/Best4, "\n")

    print("Lets take 5 players and 9 objects")
    Liroy = Player()
    Raz = Player()
    Lishai = Player()
    Barak = Player()
    Roi = Player()
    Players = [Liroy, Raz, Lishai, Barak, Roi]
    Work = [9,9,7,7,6,6,5,5,4,4,4]
    Best = 14
    GreedyAlgo(Players, Work)
    print("The approximation ratio", Lishai.value()/Best, "\n")

    print("Lets take 4 players and 9 objects")
    Liroy = Player()
    Raz = Player()
    Lishai = Player()
    Barak = Player()
    Work1 = [9,9,7,7,6,6,5,5,4,4]
    Best1 = 17
    Players1 = [Liroy, Raz, Lishai, Barak]
    GreedyAlgo(Players1, Work1)
    print(Liroy.Work, "=", Liroy.value())
    print(Raz.Work, "=", Raz.value())
    print(Lishai.Work, "=", Lishai.value())
    print(Barak.Work, "=", Barak.value())
    print("The approximation ratio", Liroy.value()/Best1, "\n")

    print("Lets take 3 players and 9 objects")
    Work2 = [9,9,7,7,6,6,5,5,4,4,4]
    Liroy = Player()
    Raz = Player()
    Lishai = Player()
    Best2 = sum(Work2)/3
    Players2 = [Liroy, Raz, Lishai]
    GreedyAlgo(Players2, Work2)
    print("The approximation ratio", Lishai.value()/Best2, "\n")

    print("Lets take 2 players and 9 objects")
    Work3 = [9,9,7,7,6,6,5,5,4,4,4]
    Liroy = Player()
    Raz = Player()
    Best3 = sum(Work3)/2
    Players3 = [Liroy, Raz]
    GreedyAlgo(Players3, Work3)
    print("The approximation ratio", Liroy.value()/Best3, "\n")

    plt.scatter(1,1)
    plt.scatter(2,1.08)
    plt.scatter(3,1)
    plt.scatter(4,1.25)
    plt.scatter(5,1.1)
    plt.scatter(6,1)

    plt.xlabel('Number of Players')
    plt.ylabel('Number of Objects')
    plt.show()















