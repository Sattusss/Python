from numpy import true_divide


class Dog:
    def __init__(self,breed,color,age):
        # instance variable
        self.breed = breed
        self.color = color
        self.age = age
    def bark(self,count=3):
        print("woof"*count)
    def eat(self,food):
        print(f"dog eats {food}")

class Shape:
    def __init__(self,name,sides):
        self.name = name
        self.sides = sides

    def perimeter(self,size=20):
        return self.sides*size
    # string notation of the object
    def __str__(self):
        return f"{self.name} has {self.sides} sides"

# this line checks if the file you run is this file or not
if __name__== "__main__":
    tommy = Dog('Street Dog','brown',3)
    tiger = Dog('BullDog','black',2)
    print(tommy)
    print(tiger)

    print('tommy breed',tommy.breed)
    print('tommy age',tommy.age)

    print('tiger breed',tiger.breed)
    print('tiger age',tiger.age)

    sqr = Shape('square',4)
    Tri = Shape('Triangle',3)
    pen = Shape('Pentagon',5)

    print(sqr)
    print(Tri)
    print(pen)

    print('Square Perimeter',sqr.perimeter())
    print('triangle perimeter',Tri.perimeter(300))
    print('Pentagon Perimeter', pen.perimeter(20))
