class car:
    def __init__(self,engine,windows,tyres): #onstructor
        self.windows = windows  #through self keyword we can access and call any attributes easily.
        self.tyres = tyres
        self.engine = engine
    
    #methods
    def self_driving(self,engine): #self keword to define a functionn also
      print("the car type is {} engine ".format(engine))#provinding seperate argument as engine (not of call)

car1 = car("petrol",4,4) #creating an object
print("the number of tyres in car is {}".format(car1.tyres))
print("the number of windows in car is {}".format(car1.windows))
print("the type of fuel req. in car is {}".format(car1.engine))
car1.self_driving("electric") #when argument needed
#car1.self_driving()
