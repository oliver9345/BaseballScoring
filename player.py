
#Placeholder
class Player:
    def __init__(self, firstName, lastName, inputTeam):
        name = [firstName, lastName]
        spotInOrder = -1
        fieldingPosition = -1
        team = inputTeam

    def getTeam(self):
        return self.team

    def setTeam(self, newTeam):
        self.team = newTeam

    def setPosition(self, newPosition):
        self.fieldingPosition = newPosition