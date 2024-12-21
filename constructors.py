#multiple constructors cant be used in python 
#but there is a way to use initialization more then arguments or less.

class Animal:
    def __init__(self, *args):
        if len(args) == 1:
            self.name = args[0]
        elif len(args) == 2:
            self.name = args[0]
            self.species = args[1]
        elif len(args) == 3:
            self.name = args[0]
            self.species = args[1]
            self.age = args[2]

    @staticmethod
    def make_sound(name, sound):
        print("The animal is {} and makes the sound {}".format(name, sound))

# Create an instance of the Animal class
hyena = Animal("hyena", "mammalia", 6)

# Call the static make_sound method
Animal.make_sound("hyena", "laughing")

#The @staticmethod decorator in Python is used to define a static method within a class.
 #A static method is a method that belongs to a class rather than an instance of the class. 
#It doesn't have access to the instance or its attributes (self), and it doesn't modify the state of the instance