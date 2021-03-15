class StellarObject:
    def __init__(self,name,constellation,ascension, declination, magnitude):
        self.name          = name        
        self.constellation = constellation        
        self.ascension     = ascension        
        self.declination   = declination        
        self.magnitude     = magnitude
        
    def getName(self): 
        return self.name    
    def getConstellation(self): 
        return self.constellation    
    def getAscension(self): 
        return self.ascension    
    def getDeclination(self): 
        return self.declination    
    def getMagnitude(self): 
        return self.magnitude
    def __repr__(self):
        return self.getName(),self.getConstellation(),self.getAscension(),self.getDeclination(),self.getMagnitude()
    
class StellarMap:
    def __init__(self):
        self.map={} #or empty dictonary
    def addObject(self,stellar_object):
        self.stellar_object=stellar_object
        if self.map.get(self.stellar_object.getName(),[])==[]:
            #print(self.stellar_object.__repr__())
            self.map[self.stellar_object.getName()]=[self.stellar_object.getMagnitude(),self.stellar_object.getName(),self.stellar_object.getConstellation()]#self.stellar_object.__repr__()
            #print(self.stellar_object.getName())
            return True
        return False
        #stellar_object is the previous class
        # # add stellar object to self.map
        #return true if it worked and
    def findObject(self,name):
        #print(self.map)
        if self.map.get(name,[]) != []:
            #print (self.map.get(name,[]))
            return self.map.get(name,[])
        return None
    def brightestInConstelation(self, constellation, n):
        #print(self.map)
        thisCon=[]
        for k in self.map.keys():
            if self.map[k][2]==constellation:
                thisCon.append (self.map[k])
        thisCon.sort()
        
        h=0
        while h<n:
            print(thisCon[h][1])
            h=h+1


smap = StellarMap()
smap.addObject(StellarObject("Sirius", "Canis Major", "06h45m 09.25s", "−16° 42′ 47.3′′", -1.46))
smap.addObject(StellarObject("Sirius", "Canis Major", "06h45m 09.25s", "−16° 42′ 47.3′′", -1.46))
smap.addObject(StellarObject("Sirius", "Canis Major", "06h45m 09.25s", "−16° 42′ 47.3′′", -1.46))
smap.addObject(StellarObject("δ CMa",  "Canis Major", "07h08m 23.49s", "−26° 23′ 35.5′′", 1.83))
smap.addObject(StellarObject("ε CMa",  "Canis Major", "06h58m 37.55s", "−28° 58′ 19.5′′", 1.50))
smap.addObject(StellarObject("Alnilam",   "Orion", "05h 36m12.81s", "−01° 12′ 06.9′′", 1.69))
smap.addObject(StellarObject("Alnitak",   "Orion", "05h 40m45.52s", "−01° 56′ 33.3′′", 1.88))
smap.addObject(StellarObject("Betelgeuse","Orion", "05h 55m10.29s", "+07° 24′ 25.3′′", 0.42))
smap.addObject(StellarObject("Bellatrix", "Orion", "05h 25m07.87s", "+06° 20′ 59.0′′", 1.64))
smap.addObject(StellarObject("Rigel",     "Orion", "05h 14m32.27s", "−08° 12′ 05.9′′", 0.18))
smap.addObject(StellarObject("Saiph",     "Orion", "05h 47m45.39s", "−09° 40′ 10.6′′", 2.07))
smap.addObject(StellarObject("Mintaka",   "Orion", "05h 32m00.40s", "−00° 17′ 56.7′′", 2.20))
smap.addObject(StellarObject("Alnilam",   "Orion", "05h 36m12.81s", "−01° 12′ 06.9′′", 1.69))
smap.addObject(StellarObject("Alnitak",   "Orion", "05h 40m45.52s", "−01° 56′ 33.3′′", 1.88))
smap.addObject(StellarObject("Betelgeuse","Orion", "05h 55m10.29s", "+07° 24′ 25.3′′", 0.42))
smap.addObject(StellarObject("Bellatrix", "Orion", "05h 25m07.87s", "+06° 20′ 59.0′′", 1.64))
smap.addObject(StellarObject("Rigel",     "Orion", "05h 14m32.27s", "−08° 12′ 05.9′′", 0.18))
smap.addObject(StellarObject("Saiph",     "Orion", "05h 47m45.39s", "−09° 40′ 10.6′′", 2.07))
smap.addObject(StellarObject("Mintaka",   "Orion", "05h 32m00.40s", "−00° 17′ 56.7′′", 2.20))

print(smap.findObject("Rigel"))
smap.brightestInConstelation("Orion",3)
#smap.brightestInConstelation("Canis Major",3)
