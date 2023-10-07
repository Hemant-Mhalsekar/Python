#Polymorphism Example 2
#Better way to use Polymorphism with Inheretance 
class Animal():
    
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

class Dog(Animal):

    def speak(self):
        return self.name + " says woof!"

class Cat(Animal):

    def speak(self):
        return self.name + " says meow!"
    
felix = Dog("felix")
niko = Cat("niko")

print(felix.speak())
print(niko.speak())