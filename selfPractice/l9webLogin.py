class User:
    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email
    def getName(self): return self.name
    def getPassword(self): return self.password
    def sendMessage(self,message): print(message,"sent to",self.email)

    class WebLogin:
    def __init__(self):
        pass
    def addUser(self,name,password,email):
        self.user=User(name,password,email)
    def login(self,name,password):
        if self.user.getName()==name and self.user.getPassword()==password:
            return True
    return False
    def sendPassword(self, name):
        message='Your password is: '+ str(self.user.getPassword())
        self.user.sendMessage(message)