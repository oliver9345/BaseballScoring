class Game:
    def __init__(self) -> None:
        #Each base is a member of class Base
        bases = [ Base() , Base() , Base()]
        outs = 0
        balls = 0
        strikes = 0
        inning = 1
        topOfInning = True
        score = [0, 0]          #visiting score first
        homeTeam = "Home Team"
        homeLineUp = ["hPlayer1", "hPlayer2", "hPlayer3", "hPlayer4", "hPlayer5", "hPlayer6", "hPlayer7", "hPlayer8", "hPlayer9"]
        spotInOrder = [0, 0]    #Moves from 0 to 8 before resetting
        visitingTeam = "Visiting Team"
        visitingLineUp = ["vPlayer1", "vPlayer2", "vPlayer3", "vPlayer4", "vPlayer5", "vPlayer6", "vPlayer7", "vPlayer8", "vPlayer9"]
        atBat = visitingLineUp[0]


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
            self.newInning()


    #Should make the next hitter in the batting order atBat
    def nextHitter(self):
        if self.topOfInning:
            self.spotInOrder[0] += 1
            if self.spotInOrder[0] >= 9:
                self.spotInOrder[0] = 0
            self.atBat = self.visitingLineUp[self.spotInOrder[0]]
        else:
            self.spotInOrder[1] += 1
            if self.spotInOrder[1] >= 9:
                self.spotInOrder[1] = 0
            self.atBat = self.homeLineUp[self.spotInOrder[1]]

    #TODO
    #Should clear bases, reset counts, etc. 
    def newInning(self):
        if self.topOfInning:
            self.topOfInning = False
        else:
            self.topOfInning = True
            self.inning += 1
        self.outs = 0
        self.balls = 0
        self.strikes = 0
        for i in self.bases:
            i.emptyBase()
        self.checkGameEnd()

    #Should check for end of game, then end it if necessary. 
    def checkGameEnd(self):
        if self.inning < 9:
            return
        elif self.inning == 9 & self.topOfInning:
            return
        elif self.topOfInning & self.score[0] != self.score[1]:
            self.gameOver = True
            return
        elif self.score[1] > self.score[0]:
            self.gameOver = True
            return
        else:
            return

    #TODO
    def endGame(self):
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
        onBase = "Empty"

    #Doesn't check for baserunner movement yet. 
    def newBaseRunner(self, player):
        self.isOccupied = True
        self.onBase = player

    def emptyBase(self):
        self.isOccuppied = False
        self.onBase = "Empty"