
#Placeholder
class Player:
    def __init__(self, firstName, lastName, inputTeam):
        name = [firstName, lastName]
        spotInOrder = -1
        fieldingPosition = -1
        team = inputTeam
        plate_appearences = 0


    def getTeam(self):
        return self.team

    def setTeam(self, newTeam):
        self.team = newTeam

    def setPosition(self, newPosition):
        self.fieldingPosition = newPosition

    def setSpotInOrder(self, newSpot):
        self.spotInOrder = newSpot

    def gameInit(self, position, battingOrder):
        self.setPosition(position)
        self.setSpotInOrder(battingOrder)