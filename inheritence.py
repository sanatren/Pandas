class Game:
    def __init__(self,name,type,generation,company):
        self.type = type
        self.generation=generation
        self.company = company
        self.name = name
    def game_msg(self):
        print("the {} welcomes you in new era of {} games".format(self.company,self.type))

class GTA(Game):
    def __init__(self,name,type,generation,company,specs_requirement,amount):
        #inheriting the game class in gta.
        super().__init__(name,type,generation,company)

        self.specs_requirement = specs_requirement
        self.amount=amount

    def release(self):
        print("{} will be released on 2004".format(self.name))

San_andreas = GTA("San_andreas","Real_world",3,"Rockstar_Games","i3(1st gen)","$200")

print(San_andreas.name)
print(San_andreas.type)
print(San_andreas.generation)
print(San_andreas.company)
print(San_andreas.specs_requirement)
print(San_andreas.amount)

San_andreas.game_msg()
San_andreas.release()

#show all atrributes and methods of class created and can be used later(basic default funtions).
print(dir(San_andreas))
print(dir(GTA))
print(dir(Game))


