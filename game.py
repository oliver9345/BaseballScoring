from player import Player
from team import Team

class Game:
    def __init__(self) -> None:
        #Each base is a member of class Base
        bases = [ Base() , Base() , Base()]
        outs = 0
        balls = 0
        strikes = 0
        inning = 1
        topOfInning = True
        score = [0, 0]
        homeTeam = Team()
        visitingTeam = Team()
        atBat = False


    def update(self):
        if self.balls >= 4:
            self.force()
            self.balls = 0
            self.strikes = 0
            self.nextHitter()
        if self.strikes >= 3:
            self.outs += 1
            self.nextHitter()
        if self.outs >= 3:
            if self.topOfInning:
                self.topOfInning = False
            else:
                self.topOfInning = True
                self.inning += 1
            self.outs = 0
            self.balls = 0
            self.strikes = 0


    #TODO: implement batting order
    #Should make the next hitter in the batting order atBat
    def nextHitter():
        pass

    #TODO
    #Should clear bases, reset counts, etc. 
    def newInning():
        pass

    #Returns how many runners are forced
    def checkForce(self):
        forced = 0
        for i in self.bases:
            if i.isOccupied:
                forced += 1
            else:
                return forced

    #Moves batter to first, moves up any forces runners
    def force(self):
        forced = self.checkForce()
        if forced > 0:
            for i in range(forced-2):
                self.bases[forced-1-i].newBaseRunner(self.bases[forced-2-i].onBase)
        self.bases[0].newBaseRunner(self.atBat)
        self.nextHitter()

    def getBalls(self):
        return self.balls

    def getStrikes(self):
        return self.strikes

    def getOuts(self):
        return self.outs

    def getBases(self):
        report = []
        for i in self.bases:
            if i.isOccupied:
                report.append(i.onBase)
            else:
                report.append("Empty")
        return report

    def pitch(self, isStrike, isInPlay):
        if not isInPlay:
            if isStrike:
                self.strikes += 1
            else:
                self.balls += 1
        
#Has a boolean isOccupied for checks based on that, and also stores the Player on base
class Base:
    def __init__(self) -> None:
        isOccupied = False
        onBase = Player()

    #Doesn't check for baserunner movement yet. 
    def newBaseRunner(self, player):
        isOccupied = True
        onBase = player