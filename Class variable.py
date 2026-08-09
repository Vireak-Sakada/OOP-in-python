class Dog:
    species = "Canis familiaris"  # Class variable shared by all instances
    total_dogs = 2 # Class variable to keep track of the total number of Dog instances

    def __init__(self, name, age):
        self.name = name
        self.age = age
        #MODIFY class variable 
        Dog.total_dogs += 2  # Increment the total_dogs count whenever a new Dog instance is created
#create the object
dog1 = Dog('Buddy', 3)
dog2 = Dog('Max', 5)

print(f"Total number of dogs: {Dog.total_dogs}") 
print() # Accessing the class variable directly from the class    
