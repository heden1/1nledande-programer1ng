
        
class DiceStats:
    def __init__(self):
        self.rolls=[0,0,0,0,0,0]
    def addRoll(self,roll):
        self.rolls[roll-1]=self.rolls[roll-1]+1
    def getFrequences(self):
        sum=0
        for count in self.rolls:
            sum=sum+count
        freq=[]
        for count in self.rolls:
            freq.append(count/sum)
        return freq
    def isFair(self,epsilon):
        freq=self.getFrequences()
        for freq in self.getFrequences():
            if not 1/6-epsilon<freq<1/6+epsilon:
                return False
            return True
    
    
stats = DiceStats()
stats.addRoll(1)
stats.addRoll(5)
stats.addRoll(2)
stats.addRoll(5)
print(stats.getFrequences())