#Object Oriented Programming example-3
#Added Operation/Action --> Methods
class Dog():
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots

    #Operation/Action --> Methods
    def bark(self):
            print("WOOF! My name is {} and my breed is {}".format(self.name, self.breed))

my_dog = Dog(breed='Lab', name="Sammy", spots=True)

print(my_dog.name)
my_dog.bark()
