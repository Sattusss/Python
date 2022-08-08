class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # string repr of object
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    # raw repr of object
    def __repr__(self) -> str:
        return self.__str__()
    # special function to overloading > symbol when used for object 
    def __gt__(self,other):
        return self.age > other.age

if __name__ == "__main__":
    p = Person('Raju',39)
    p1 = Person('Vijay',23)
    p2 = Person('Sujal',32)

    if p < p2:
        print(f'{p.name} is elder')
    person_list = [p,p1,p2]
    person_list.sort()
    print(person_list)


