class TrainSeats:
  def __init__(self,nrOfSeats):
    self.nrOfSeats = nrOfSeats
    self.seats=[0]*self.nrOfSeats
  def pick(self,seatNum):
    if self.seats[seatNum]==0:
      self.seats[seatNum]=1
      return True
    else:
      return False
    
  def book(self,n):
    nr=0
    i=0
    while nr<n and i<self.nrOfSeats:
      print(i)
      if self.seats[i]==0:
        self.seats[i]=1
        nr=nr+1
      i=i+1
