class Application:
   def __init__(self, name, personalNum, distance):
        self.name        = name
        #print(name,personalNum,distance)
        self.personalNum = personalNum
        self.distance    = distance
   def getName(self): return self.name
   def getPersonalNumber(self): return self.personalNum
   def distanceFromSchool(self): return self.distance
class ApplicationList:
  def __init__(self,nrOfStudents):
    self.nrOf=nrOfStudents
    #print (nrOfStudents)
    self.accepted=[]
  def addApplication(self,app):
    if app.distanceFromSchool()<5 and len(self.accepted)<self.nrOf:
      self.accepted.append([app.getName(),app.getPersonalNumber()])
    
        #self.accepted.append(app)
  def printAccepted(self):
    for i in self.accepted:
      print( i[0] +" " + i[1])
        