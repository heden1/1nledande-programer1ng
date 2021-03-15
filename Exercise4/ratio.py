class Ratio:
    def __init__(self,nom,denom):
        self.nom=nom
        self.denom=denom
        self.__repr__()    
    
    def __repr__(self):
        self.nom=self.nom
        self.denom=self.denom
        i=2
        while i<=self.nom and i<=self.denom:
            while self.nom/i ==self.nom//i and self.denom/i ==self.denom//i:
                self.nom=self.nom//i
                self.denom=self.denom//i
            i=i+1
            
        string1="Ratio({},{})".format(self.nom, self.denom)
        return string1
    
    def __add__(self,other): 
        nom=(self.nom*other.denom)+ (other.nom*self.denom)
        denom= self.denom * other.denom
        return Ratio(nom,denom) 
    def __mul__(self, other):
        nom=self.nom * other.nom
        denom =self.denom * other.denom
        return Ratio(nom , denom)
    def __eq__(self, other):
        if self.__repr__()==other.__repr__():
            return True
        else:
            return False
        
        
        
## TEST        
    
#print(Ratio(400554,4284))


#x=Ratio(6,8)
#y=Ratio(3,4)

#print(x.__add__(y))
#print(Ratio(6,8).__add__(Ratio(3,4)))

#print(x.__mul__(y))

#print(x.__eq__(y))



