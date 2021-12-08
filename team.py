from player import Player
#Placeholder
class Team:
    def __init__(self, name) -> None:
        self.name = name
        self.playerList = []
        self.lineUp = []
        self.defense = ["","","","","","","","",""]

    def printPlayerList(self):
        j=0
        for i in self.playerList:
            print(j, r". ", i.name[0], r", ", i.name[1])
            j += 1

    def inputPlayer(self, question):
            self.printPlayerList()
            return input(question)

    #TODO
    def initgame(self, game):
        while len(self.lineUp) < 9:
            nextPlayer = self.inputPlayer("Which player is batting in spot ", len(self.lineUp)+1, "?")
            if nextPlayer == "new":
                newPlayer = Player() #TODO

            if nextPlayer <= len(self.playerList):
                self.lineUp.append(self.playerList[nextPlayer])
                self.lineUp[-1].setSpotInOrder(len(self.lineUp))
            playerPlaced = False
            while not playerPlaced:
                position = input("Which position does this player play? (1-9 or dh): ")
                if type(self.defense[position-1]) == Player:
                    print("There's already a player there.")
                else:
                    self.defense[position-1] = self.playerList[nextPlayer]
                    self.defense[position-1].setPosition(position-1)
                if position == "dh":
                    self.dh = self.playerList[nextPlayer]
                    pitch = self.inputPlayer("Who's pitching?")
                    self.defense[0] = self.playerList[pitch]
                    playerPlaced = True

    #TODO
    def setPlayerPosition(self, player, position):
        pass

    def endGame(self, game):
        self.lineUp = []
        self.defense = ["","","","","","","","",""]
