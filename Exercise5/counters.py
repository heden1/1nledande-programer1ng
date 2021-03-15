
class SimpleCounter:
    def __init__(self):
        self.counter=0
        
    def count(self):
        self.counter = self.counter + 1 # TODO: do the counting
    

    def reset(self):
        self.counter = 0
    # TODO: reset the counter back to zero

    def getValue(self):
        return self.counter
        # TODO: return the current count


class BoundedCounter(SimpleCounter):
    def __init__(self,init,modulus):
        self.counter=init
        self.modulus=modulus
        
    def count(self):
        self.counter = (self.counter + 1)%self.modulus # TODO: do the counting
    
    def reset(self):
        super().reset()
    # TODO: reset the counter back to zero
    

    def getValue(self):
        return super().getValue()
        # TODO: return the current count
        



class ChainedCounter(BoundedCounter):
    def __init__(self,init,modulus,next):
        self.counter=init
        self.modulus=modulus
        self.next=next

        
        
    def count(self):
        if self.counter==self.modulus-1:
            self.counter=0
            if next!= None:
                self.next.count()
            return
        self.counter = self.counter + 1 

    

    def reset(self):
        super().reset()

    def getValue(self):
        return super().getValue()