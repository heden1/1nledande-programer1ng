from math import sin,cos,radians
import random


""" This is the model of the game"""
class Game:
    """ Create a game with a given size of cannon (length of sides) and projectiles (radius) """
    def __init__(self, cannonSize, ballSize):
        self.currentPlayerIndex =0
        self.currentWind=random.random()*20-10 
        Game.currentWind=self.currentWind
        
        Game.cannonSize= cannonSize
        Game.ballSize= ballSize
        self.players = [Player(False, -90, "blue",Game),Player(True, 90, "red",Game)] 



    """ A list containing both players """
    def getPlayers(self):
        return self.players

    """ The height/width of the cannon """
    def getCannonSize(self):
        return Game.cannonSize

    """ The radius of cannon balls """
    def getBallSize(self):
        return Game.ballSize 

    """ The current player, i.e. the player whose turn it is """
    def getCurrentPlayer(self):
        return self.players[self.currentPlayerIndex]

    """ The opponent of the current player """
    def getOtherPlayer(self):
        return self.players[1-self.currentPlayerIndex] 
    
    """ The number (0 or 1) of the current player. This should be the position of the current player in getPlayers(). """
    def getCurrentPlayerNumber(self):
        return self.currentPlayerIndex
    
    """ Switch active player """
    def nextPlayer(self):
        self.currentPlayerIndex =1 - self.currentPlayerIndex


    """ Set the current wind speed, only used for testing """
    def setCurrentWind(self, wind):
        Game.currentWind=wind
    
    def getCurrentWind(self):
        return Game.currentWind

    """ Start a new round with a random wind value (-10 to +10) """
    def newRound(self):
        Game.currentWind=random.random()*20-10


""" Models a player """
class Player: 
    def __init__(self,isReversed,xPos,color,Game):
        self.score =0
        self.color=color
        self.xPos = xPos
        self.isReversed = isReversed

    """ Create and return a projectile starting at the centre of this players cannon. Replaces any previous projectile for this player. """
    def fire(self, angle, velocity):
        if  self.isReversed:
            angle=180-angle
        self.angle=angle
        self.velocity=velocity
        wind=Game.currentWind
        
        xPos=self.xPos
        yPos= Game.cannonSize/2
        xLower=-110
        xUpper=110

        return Projectile(angle, velocity, wind, xPos, yPos, xLower, xUpper) 

    """ Gives the x-distance from this players cannon to a projectile. If the cannon and the projectile touch (assuming the projectile is on the ground and factoring in both cannon and projectile size) this method should return 0"""
    def projectileDistance(self, proj):
        self.proj=proj
        self.xPlayer=self.proj.getX()

        cannonSize=Game.cannonSize/2 
        ballSize=Game.ballSize
        radiusObjects =cannonSize + ballSize
        ccDistance= self.xPlayer - self.xPos
    
        
        if abs(ccDistance) <= radiusObjects:
            return 0
        distance =ccDistance- ((ccDistance)/abs(ccDistance)*radiusObjects)
        return distance

    """ The current score of this player """
    def getScore(self):
        return self.score  

    """ Increase the score of this player by 1."""
    def increaseScore(self):
        self.score += 1


    """ Returns the color of this player (a string)"""
    def getColor(self):
        return self.color 

    """ The x-position of the centre of this players cannon """
    def getX(self):
        return self.xPos 

    """ The angle and velocity of the last projectile this player fired, initially (45, 40) """
    def getAim(self):
        try:
            if  self.isReversed:
                return 180-self.angle, self.velocity
            return self.angle, self.velocity
        except AttributeError:
            return 0,0




""" Models a projectile (a cannonball, but could be used more generally) """
class Projectile:
    """
        Constructor parameters:
        angle and velocity: the initial angle and velocity of the projectile 
        angle 0 means straight east (positive x-direction) and 90 straight up
        wind: The wind speed value affecting this projectile
        xPos and yPos: The initial position of this projectile
        xLower and xUpper: The lowest and highest x-positions allowed
    """
    def __init__(self, angle, velocity, wind, xPos, yPos, xLower, xUpper):
        self.yPos = yPos
        self.xPos = xPos
        self.xLower = xLower
        self.xUpper = xUpper
        theta = radians(angle)
        self.xvel = velocity*cos(theta)
        self.yvel = velocity*sin(theta)
        self.wind = wind
        

    """ 
        Advance time by a given number of seconds
        (typically, time is less than a second, 
        for large values the projectile may move erratically)
    """
    def update(self, time):
        # Compute new velocity based on acceleration from gravity/wind
        yvel1 = self.yvel - 9.8*time
        xvel1 = self.xvel + self.wind*time
        
        # Move based on the average velocity in the time period 
        self.xPos = self.xPos + time * (self.xvel + xvel1) / 2.0
        self.yPos = self.yPos + time * (self.yvel + yvel1) / 2.0
        
        # make sure yPos >= 0
        self.yPos = max(self.yPos, 0)
        
        # Make sure xLower <= xPos <= mUpper   
        self.xPos = max(self.xPos, self.xLower)
        self.xPos = min(self.xPos, self.xUpper)
        
        # Update velocities
        self.yvel = yvel1
        self.xvel = xvel1
        
    """ A projectile is moving as long as it has not hit the ground or moved outside the xLower and xUpper limits """
    def isMoving(self):
        return 0 < self.getY() and self.xLower < self.getX() < self.xUpper

    def getX(self):
        return self.xPos

    """ The current y-position (height) of the projectile". Should never be below 0. """
    def getY(self):
        return self.yPos

