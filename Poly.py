#Polymorphism

class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"

class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"
    
felix = Dog("felix")
niko = Cat("niko")

for pet in [niko, felix]:
    print(pet.speak())
