import game

def test_base():
    print('')
    print("Base(): ", end='\n')
    base = game.Base()
    print("Init test: ", end='')
    assert not base.isOccuppied
    assert base.onBase == "Empty"
    print("Passed")
    base.newBaseRunner("Player")
    print("New Baserunner: ", end= '')
    assert base.isOccuppied
    assert base.onBase == ("Player")
    print("Passed")
    base.emptyBase()
    print("Empty base: ", end= '')
    assert not base.isOccuppied
    assert base.onBase == "Empty"
    print("Passed")

def test_game():
    print('')
    print("Game(): ")
    

    #test nextHitter
    testGame = game.Game()
    print("nextHitter(): ", end='')
    assert testGame.atBat == 'vPlayer1'
    testGame.nextHitter()
    assert testGame.atBat == 'vPlayer2'
    for i in range(0,8):
        testGame.nextHitter()
    assert testGame.atBat == 'vPlayer1'
    print("Passed")

    #test newInning
    testGame = game.Game()
    print("newInning(): ", end='')
    assert testGame.topOfInning
    testGame.newInning()
    assert not testGame.topOfInning
    assert testGame.atBat == 'hPlayer1'
    testGame.nextHitter()
    assert testGame.atBat == 'hPlayer2'
    for i in range(0,8):
        testGame.nextHitter()
    assert testGame.atBat == 'hPlayer1'
    testGame.newInning()
    assert testGame.topOfInning
    assert testGame.inning == 2
    assert testGame.atBat == 'vPlayer1'
    for i in testGame.bases:
        assert not i.isOccuppied
    print("Passed")

    #test checkForce & force
    print("force() and checkForce(): ", end='')
    testGame = game.Game()
    assert testGame.checkForce() == 0
    testGame.force()
    assert testGame.checkForce() == 1
    testGame.force()
    assert testGame.checkForce() == 2
    testGame.force()
    assert testGame.checkForce() == 3
    testGame.force()
    assert testGame.checkForce() == 3
    assert testGame.score[0] == 1
    print('Passed') 

    #test getBases
    print("getBases(): ", end='')
    testGame = game.Game()
    for i in range(0,3):
        testGame.force()
        testGame.nextHitter()
    getBases = testGame.getBases()
    assert getBases[0] == 'vPlayer3'
    assert getBases[1] == 'vPlayer2'
    assert getBases[2] == 'vPlayer1'
    print("Passed")

    #test pitch
    print("pitch(): ", end='')
    testGame = game.Game()
    assert testGame.balls == 0
    assert testGame.strikes == 0
    testGame.pitch(True, False)
    assert testGame.strikes == 1
    testGame.pitch(False, False)
    assert testGame.balls == 1
    print("Passed")

    #test update

    #test checkGameEnd


test_base()
test_game()