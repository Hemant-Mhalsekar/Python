#Object Oriented Programming example-3
#Added Operation/Action --> Methods
class Dog():
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots

my_dog = Dog(breed='Lab', name="Sammy", spots=True)

print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)