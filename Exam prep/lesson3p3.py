#Implement the classAccountingwhich keeps track ofhow muchsomeone owes someone else when people make loans toeach other.
#Itshould be possible to create the class like this:>>> acc = Accounting()Now if John gives 200 crowns to Mary,
#we can recordit like this:>>>
#acc.transaction("John", "Marry", 200)We can add a few more transactions:>>> acc.transaction("Mary",  "Harry", 50)>>> 
#acc.transaction("Steff", "John", 50)>>> acc.transaction("Mary",  "John", 10)>>> acc.transaction("Mary",  "John", 20)

#At any point it should be possible to call the methodprintReport()tosee 
#for a specific person:●how much and to whom he/she has given money●how much and from whom he/she has received moneyThere two examples
#bellow:>>> acc.printReport("John")Mary  200 30Steff   0 50>>> acc.printReport("Mary")John   30 200Harry  50   0Here the 
#first number on every row is how much thepersonhas given, and the second is how much he/she has received.
#Hint: One way to solve the problem is to maintain a dictionary ofdictionaries. For example, 
#after the first transactionthe state should be:{"John": {"Mary": (200,0)}, "Mary": {"John": (0, 200)}}
#In this way it is always possible to ask for a reportfor both John andMary.

class Accounting:
    def __init__(self):
        self.dict1={}
    def transaction(self,from,to,money):
        pass
    def printReport(self,name):
        pass
    
    
    {"John": {"Mary": (200,0)}, "Mary": {"John": (0, 200)}}
    
    
    
acc = Accounting()

acc.transaction("John", "Marry", 200)

acc.transaction("Mary",  "Harry", 50)
acc.transaction("Steff", "John", 50)
acc.transaction("Mary",  "John", 10)
acc.transaction("Mary",  "John", 20)