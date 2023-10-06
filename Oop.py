#Object Oriented Programming example-1
class Dog():
    def __init__(self, mybreed):
        self.breed = mybreed
my_dog = Dog(mybreed='Lab')

print(my_dog.breed)