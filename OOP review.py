class Dog:
    species = "canis lupus familiaris"  # Class variable shared by all instances
    toatal_dogs = 0  # Class variable to keep track of the total number of Dog instances
    def __init__(self, name, age):
        self.name = name
        self.age = age

        Dog.toatal_dogs += 1  # Increment the total_dogs count whenever a new Dog instance is created
#create the object
dog1 = Dog('Buddy', 3)
dog2 = Dog('Max', 5)
dog3 = Dog('Charlie', 2)
print(Dog.toatal_dogs) 
print(dog1.age + dog2.age) # Accessing the class variable through an instance