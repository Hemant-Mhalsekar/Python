#Object Oriented Programming example-4
class Circle():

    #Class Object Attribute
    pi = 3.14
    
    def __init__(self, radius = 1):
        self.radius = radius

    #Method to calculate circumference
    def get_circumference(self):
        print(self.radius*self.pi*2)
    
my_circle = Circle(30)
my_circle.get_circumference()