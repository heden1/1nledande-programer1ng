class Resistor:
    def __init__(self,resistance):
        self.resistance = resistance
    def getRestance(self):
        return self.resistance

    
    
    
    
class SequentialResistors:
    def __init__(self,resistance):
        self.resistance=0
        for i in range(len(resistance)):
            self.resistance=self.resistance+resistance[i].getRestance()
        
    def getRestance(self):
        return self.resistance
    
class ParallelResistors:
    def __init__(self,resistance):
        one7Resistance=0
        for i in range(len(resistance)):
            one7Resistance = one7Resistance+1/resistance[i].getRestance() 
        self.resistance=1/one7Resistance
    def getRestance(self):
        return self.resistance
    
    
    
circuit = SequentialResistors([Resistor(1),ParallelResistors([Resistor(2),Resistor(3)])])

print(circuit.getRestance())