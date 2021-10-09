

class Game:
    def __init__(self) -> None:
        #Each base is a member of class Base
        self.bases = [ Base() , Base() , Base()]
        self.outs = 0
        self.balls = 0
        self.strikes = 0
        self.inning = 1
        self.topOfInning = True
        self.score = [0, 0]          #visiting score first
        self.homeTeam = "Home Team"
        self.homeLineUp = ["hPlayer1", "hPlayer2", "hPlayer3", "hPlayer4", "hPlayer5", "hPlayer6", "hPlayer7", "hPlayer8", "hPlayer9"]
        self.spotInOrder = [0, 0]    #Moves from 0 to 8 before resetting
        self.visitingTeam = "Visiting Team"
        self.visitingLineUp = ["vPlayer1", "vPlayer2", "vPlayer3", "vPlayer4", "vPlayer5", "vPlayer6", "vPlayer7", "vPlayer8", "vPlayer9"]
        self.atBat = self.visitingLineUp[0]


    def update(self):
        if self.balls >= 4:
            self.force()
            self.balls = 0
            self.strikes = 0
            self.nextHitter()
        if self.strikes >= 3:
            self.outs += 1
            self.balls = 0
            self.strikes = 0
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

    
    #Should clear bases, reset counts, etc. 
    def newInning(self):
        if self.topOfInning:
            self.topOfInning = False
            self.atBat = self.homeLineUp[self.spotInOrder[1]]
        else:
            self.topOfInning = True
            self.inning += 1
            self.atBat = self.visitingLineUp[self.spotInOrder[0]]
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
            if i.isOccuppied:
                forced += 1
            else:
                #print("Forced is: ", forced)
                return forced
        return forced

    #Moves batter to first, moves up any forces runners
    def force(self):
        forced = self.checkForce()
        if forced > 0:
            for i in range(0, forced):
                self.moveRunner(forced-i, forced-i+1)
                #print("Forcing R", forced-i+1)
        self.bases[0].newBaseRunner(self.atBat)

    def getBalls(self):
        return self.balls

    def getStrikes(self):
        return self.strikes

    def getOuts(self):
        return self.outs

    def getBases(self):
        report = []
        for i in self.bases:
            if i.isOccuppied:
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
        else:
            return

    #Gets currentBase & newBase in range(1,5)
    def moveRunner(self, currentBase, newBase):
        assert currentBase <= newBase, "Can't move runner backwards."
        if newBase != 4:
            assert not self.bases[newBase-1].isOccuppied, "New base is occupied already"
        assert 0 <= currentBase and currentBase < 5 and newBase > 0 and newBase < 5, "Invalid inputs for moveRunner"
        if newBase == 4:
            self.score[0 if self.topOfInning else 1] += 1
        else:
            if currentBase == 0:
                self.bases[newBase-1].newBaseRunner(self.atBat)
            else:
                self.bases[newBase-1].newBaseRunner(self.bases[currentBase-1].onBase)
        if currentBase != 0:
            self.bases[currentBase-1].emptyBase()
        else:
            self.nextHitter()

    def inputMoveRunner(self, base):
        if base != -1:
            if not self.bases[base].isOccuppied:
                print("There's not runner at base", base)
                return
        runnerMove = 5
        while not runnerMove <= 4 or not runnerMove >= base+1:
            if base == -1:
                runnerMove = input("Where does the batter go? (enter 1-4 or o): ")
            else:
                runnerMove = input("Where does runner on "+ str(base+1) +" go? (enter 1-4 or o): ")
            if runnerMove == "o":
                self.outs += 1
                if base != -1:
                    self.bases[base].emptyBase()
                else:
                    self.nextHitter()
                return
            runnerMove = int(runnerMove)
            if runnerMove < base+1:
                print("Runners can't move backwards.")
            if runnerMove == base+1 or runnerMove == 4:
                break
            if self.bases[runnerMove-1].isOccuppied:
                print("That base is occupied")
                runnerMove = 5
        if runnerMove != base+1 and type(runnerMove) == int:
            self.moveRunner(base+1, runnerMove)

    
    def startGame(self):
        while(True):
            self.displayState()
            play = input("Next play: ")
            #Make switch
            if play == "b":
                self.pitch(False, False)
            elif play == "s":
                self.pitch(True, False)
            elif play == "h":
                self.pitch(True, True)
                for i in range(0,3):
                    if self.bases[2-i].isOccuppied:
                        #TODO: make whileloop its own function and copy to the batter
                        self.inputMoveRunner(2-i)
                self.inputMoveRunner(-1)
                self.update()

                            
            self.update()

    #Prints the current game state to the terminal
    def displayState(self):
        print(self.visitingTeam, self.score, self.homeTeam, "   ", "top" if self.topOfInning else "bottom", self.inning,)
        print(self.balls, "-", self.strikes, " , ", self.outs, " Outs")
        print("At Bat: ", self.atBat, "     ", 1 if self.bases[0].isOccuppied else 0, 1 if self.bases[1].isOccuppied else 0, 1 if self.bases[2].isOccuppied else 0)


        
#Has a boolean isOccuppied for checks based on that, and also stores the Player on base
class Base:
    def __init__(self) -> None:
        self.isOccuppied = False
        self.onBase = "Empty"

    #Doesn't check for baserunner movement yet. 
    def newBaseRunner(self, player):
        self.isOccuppied = True
        self.onBase = player

    def emptyBase(self):
        self.isOccuppied = False
        self.onBase = "Empty"




