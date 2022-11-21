class Player(str):
    def __init__(self):
        self.total = 0
        self.Work = []
        self.value()
        self.put()

    def value(self):
        for work in self.Work:
            self.total += work

    def put(self, integer):
        self.Work.append(integer)


def GreedyAlgo(Players, Works):
    MinPlayer = Players[0]
    for Singlework in Works:
        for SinglePlayer in Players:
           if SinglePlayer.value() < MinPlayer.value:
               MinPlayer = SinglePlayer
    MinPlayer.put(Singlework)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Liroy = Player
