class StellarObject:
    def __init__(self, name, constellation,ascension, declination, magnitude):
        self.name          = name
        self.constellation = constellation
        self.ascension     = ascension
        self.declination   = declination
        self.magnitude     = magnitude

    def getName(self): return self.name
    def getConstellation(self): return self.constellation
    def getAscension(self): return self.ascension
    def getDeclination(self): return self.declination
    def getMagnitude(self): return self.magnitude

class StellarMap1:
    def __init__(self):
        self.list = []

    def addObject(self, stellar_object):
        if self.findObject(stellar_object.getName()) != None:
            return False
        self.list.append(stellar_object)
        return True

    def findObject(self, name):
        for stellar_object in self.list:
            if stellar_object.getName() == name:
                return stellar_object
        return None

    def brightestInConstelation(self, constellation, n):
        results = []
        for stellar_object in sorted(self.list, key=lambda obj: obj.getMagnitude()):
            if stellar_object.getConstellation() == constellation:
                results.append(stellar_object)
                if len(results) >= n:
                    break
        return results



class StellarMap2:
    def __init__(self):
        self.dict = {}

    def addObject(self, stellar_object):
        if stellar_object.getName() in self.dict:
            return False
        self.dict[stellar_object.getName()] = stellar_object
        return True

    def findObject(self, name):
        return self.dict.get(name)

    def brightestInConstelation(self, constellation, n):
        results = []
        for name,stellar_object in sorted(self.dict.items(), key=lambda pair: pair[1].getMagnitude()):
            if stellar_object.getConstellation() == constellation:
                results.append(stellar_object)
                if len(results) >= n:
                    break
        return results


class StellarMap3:
    def __init__(self):
        self.dict = {}
        self.dictByConstelation = {}

    def addObject(self, stellar_object):
        if stellar_object.getName() in self.dict:
            return False
        self.dict[stellar_object.getName()] = stellar_object
        self.dictByConstelation.setdefault(stellar_object.getConstellation(),[]).append(stellar_object)
        return True

    def findObject(self, name):
        return self.dict.get(name)

    def brightestInConstelation(self, constellation, n):
        return sorted(self.dictByConstelation.get(constellation,[]), key=lambda obj: obj.getMagnitude())[:n]



smap = StellarMap3()

smap.addObject(StellarObject("Sirius", "Canis Major", "06h 45m 09.25s", "−16° 42′ 47.3″", -1.46))
smap.addObject(StellarObject("δ CMa",  "Canis Major", "07h 08m 23.49s", "−26° 23′ 35.5″", 1.83))
smap.addObject(StellarObject("ε CMa",  "Canis Major", "06h 58m 37.55s", "−28° 58′ 19.5″", 1.50))

smap.addObject(StellarObject("Alnilam",   "Orion", "05h 36m 12.81s", "−01° 12′ 06.9″", 1.69))
smap.addObject(StellarObject("Alnitak",   "Orion", "05h 40m 45.52s", "−01° 56′ 33.3″", 1.88))
smap.addObject(StellarObject("Betelgeuse","Orion", "05h 55m 10.29s", "+07° 24′ 25.3″", 0.42))
smap.addObject(StellarObject("Bellatrix", "Orion", "05h 25m 07.87s", "+06° 20′ 59.0″", 1.64))
smap.addObject(StellarObject("Rigel",     "Orion", "05h 14m 32.27s", "−08° 12′ 05.9″", 0.18))
smap.addObject(StellarObject("Saiph",     "Orion", "05h 47m 45.39s", "−09° 40′ 10.6″", 2.07))
smap.addObject(StellarObject("Mintaka",   "Orion", "05h 32m 00.40s", "−00° 17′ 56.7″", 2.20))

for obj in smap.brightestInConstelation("Canis Major", 2):
    print(obj.getName())
