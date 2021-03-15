class Pixels:
    def __init__(self,m,n,color):
        self.rows=[]
        for i in range(m):
            row=[]
            for j in range (n):
                row.append(color)
            self.rows.append(row)
        
        
        
        
    def printImage(self):
        for row in self.rows:
            print("".join(row))
    def drawPixel(self,x,y,color):
        if 0<=y<len(self.rows)and 0<=x<len(self.rows[0]):
            self.rows[x][y] = color
            
    def fillCircles(self,x,y,radius,color):
        for i in range(x-radius,x+radius+1):
            for j in range(y-radius,y+radius+1):
                if (x-i)**2+(y-j)**2<=radius*radius:
                    self.drawPixel(i,j,color)
            
pixels=Pixels(20,20,' ')

#pixels.drawPixel(10,15,'r')
pixels.fillCircles(10,10,3,'r')
pixels.fillCircles(6,15,2,'g')

pixels.printImage()