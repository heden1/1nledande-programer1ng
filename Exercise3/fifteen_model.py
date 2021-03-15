import random

class FifteenModel:
	def __init__(self):
		i=1
		self.myList=[[0 for x in range(4)] for y in range(4)] #creats empty matrix 
		for m in range(4):
			for n in range(4):
				if m==3 and n==3:
					i=0
				self.myList[m][n]=i
				i=i+1

	
		

	def getValue(self,row,col):
		return self.myList[row][col]

	def tryMove(self,row,col):
		if self.myList[row][col]!=0:

			if 0<=row-1<=3 and 0<=col<=3 and self.myList[row-1][col]==0:
				self.myList[row-1][col]=self.myList[row][col]
				self.myList[row][col]=0
	
			elif 0<=row+1<=3 and 0<=col<=3 and self.myList[row+1][col]==0:
				self.myList[row+1][col]=self.myList[row][col]
				self.myList[row][col]=0
	
			elif 0<=row<=3 and 0<=col-1<=3 and self.myList[row][col-1]==0:
				self.myList[row][col-1]=self.myList[row][col]
				self.myList[row][col]=0
			elif 0<=row<=3 and 0<=col+1<=3 and self.myList[row][col+1]==0:
				self.myList[row][col+1]=self.myList[row][col]
				self.myList[row][col]=0
			else: 
				print("This box can't be moved")
		else:
			print("Press a box that has a number on it")


	def shuffle(self):
		for i in range(1000):
			self.tryMove(random.randint(0,3),random.randint(0,3))

		
