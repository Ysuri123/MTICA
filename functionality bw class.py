class Animal:#base class
    def __init__(self,name,color):#init=constructor
        self.name=name
        self.color=color
class Cat(Animal):#dirivid class
    def mew(self):
        print("Cat meows")
class Dog(Animal):#dirived class
    def bark(self):
        print("Woof")
if __name__ == "__main__":
    print(__name__)
    pet1=Dog("tomy","brown")
    pet2=Cat('luch','white')
    pet1.bark()
    pet2.mew()
    print(pet1.name)
    print(pet2.name)
