import game

def test_base():
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



test_base()