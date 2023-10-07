#Inheretance Example
#Base class (or prent class)

class Animal():

    def __init__(self):
        print("Animal created")

    def who_am_i(self):
        print("I am na animal")
    
    def eat(self):
        print("I am eating")

#Derived class 

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    #Overriding the function
    def who_am_i(self):
        print("I am a dog")

    def bark(self):
        print("WOOF!")