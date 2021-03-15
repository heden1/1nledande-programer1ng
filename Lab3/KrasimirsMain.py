
#Krasimirs main.py
#mabe by Krasimir

# Imports everything from both model and graphics
from gamemodel import *
from gamegraphics import *



def graphicInput(win, game, player):
    angle, vel = player.getAim() # Gets the last entered values for this player
    inputwin = InputDialog(angle, vel, game.getCurrentWind())
    choice = inputwin.interact()
    inputwin.close()
    if choice == "Quit":
        win.close()
        sys.exit()
    return inputwin.getValues()

# Here is a nice little method you get for free
# It fires a shot for the current player and animates it until it stops
def graphicFire(game, angle, vel):
    player = game.getCurrentPlayer()
    # create a shot and track until it hits ground or leaves window
    gproj = player.fire(angle, vel)
    while gproj.isMoving():
        gproj.update(1/50)
        update(50)
    return gproj

def graphicFinishShot(game, proj):
    # The current player
    player = game.getCurrentPlayer()
    # The player opposing the current player
    other = game.getOtherPlayer()

    # Check if we won
    distance = other.projectileDistance(proj) 
    if distance == 0.0:
        player.increaseScore()
        game.newRound()

    # Switch active player
    game.nextPlayer()

def graphicPlay():
    # TODO: This is where you implement the game loop
    # HINT: Creating a GraphicGame is a good start. 
    # HINT: You can look at the text interface for some inspiration
    # Note that this code should not directly work with any drawing or such, all that is done by the methods in the classes
    game = Game(10, 3)
    ggame = GraphicGame(game)
    win = ggame.getWindow()

    while True:
        currentPlayer = ggame.getCurrentPlayer()
        # interact with the user
        angle, vel = graphicInput(win, ggame, currentPlayer)
        gproj = graphicFire(ggame, angle, vel)
        graphicFinishShot(ggame, gproj)


# Run the game with graphical interface
graphicPlay()