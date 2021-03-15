class Card:
  def __init__(self,rank,suit):
    self.rank=rank
    self.suit=suit
    
  def getRank(self):
    return self.rank
  
  def getSuit(self):
    return self.suit
  
  def value(self):
    if self.rank==1:
      return "Ace"
    elif self.rank==11:
      return "Jack"
    elif self.rank==11:
      return "Queen"
    elif self.rank==11:
      return "King"
    return self.suit
  
  def __str__(self):
    return (self.value() + " of " + self.getSuit() ) #change to ace of spades....
  
  