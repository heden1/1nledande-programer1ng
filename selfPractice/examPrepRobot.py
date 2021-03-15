class Robot:
  def __init__(self):
    self.cordinates=[0,0]
    self.direction=0
  def turnLeft(self):
    self.direction=(self.direction-3)%12
  def turnRight(self):
    self.direction=(self.direction+3)%12
  def forward(self,n):
    if self.direction==0:
      self.cordinates[1]=self.cordinates[1]+n
    elif self.direction ==6:
      self.cordinates[1]=self.cordinates[1]-n
    elif self.direction ==3:
      self.cordinates[0]=self.cordinates[0]+n
    elif self.direction ==9:
      self.cordinates[0]=self.cordinates[0]-n
  def getPosition(self):
    #return "("+str(",".join(self.cordinates))+")"
    return (self.cordinates[0]),(self.cordinates[1])
  def getDirection(self):
    if self.direction==0:
      return "NORTH"
    elif self.direction ==6:
      return "SOUTH"
    elif self.direction ==3:
      return "EAST"
    elif self.direction ==9:
      return "WEST"
    return self.direction