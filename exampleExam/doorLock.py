class Doorlock:
    def __init__(self,pin):
        self.pin=pin
        self.open=True
        
    def lock(self):
        if self.open:
            self.open=False
        else: 
            print("Door was allredy locked")
    def unlock(self,pin):
        if not self.open:
            if pin==self.pin:
                self.open=True
            else:
                print("wrong pin")
        else:
            print("Door is allredy open")
            
    def set_pin(self, pin,new_pin):
        if self.open:
            if pin==self.pin:
                self.pin=new_pin
            else:
                print("Wrong input pin")
        else: 
            print ("Door needs to be opwn for changing pin")
            
    def get_door(self): #todo ta bort inte en del av uppgiften
        return self.open
    
#test
door=Doorlock(1111)
door.lock()
door.unlock(1111)
door.set_pin(1111,0)
print(door.get_door())
door.lock()
door.unlock(1111)
door.unlock(0)
print(door.get_door())