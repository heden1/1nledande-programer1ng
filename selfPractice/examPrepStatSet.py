class StatSet:
  def __init__(self):
    self.statSet=[]
  def addNumber(self,x):
    self.statSet.append(x)
  def mean(self):
    sum =0
    for i in self.statSet:
      sum=sum+i
    return int(sum)/len(self.statSet)
  def median(self):
    self.statSet.sort()
    if len(self.statSet)%2==1:
      return self.statSet[len(self.statSet)//2-1]
    return (self.statSet[len(self.statSet)//2-1]+self.statSet[len(self.statSet)//2-2])/2
  def stDev2(self):
    pass
  def count(self):
    return len(self.statSet)
  def min (self):
    min=self.statSet[0]
    for i in self.statSet:
      if i < min:
        min=i
    return min 
  def max (self):
    max=self.statSet[0]
    for i in self.statSet:
      if i >max:
        max=i
    return max
  
  

set = StatSet()
set.addNumber(10)
set.addNumber(20)
set.addNumber(30)
return set.mean()