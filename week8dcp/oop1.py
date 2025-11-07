import pyttsx3

engine = pyttsx3.init()

class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        pass

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def speak(self):
        print(f"{self.name} says Woof!")
        engine.say("Woof Woof Woof")
        engine.runAndWait

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def speak(self):
        print(f"{self.name} says Meow!")
        engine.say("Meow Meow Meow")
        engine.runAndWait

'''

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        

    def speak(self):
        print(f"{self.name} says woof")
        engine.say("Woof woof woof")
        engine.runAndWait

class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        

    def speak(self):
        print(f"{self.name} says meow")
        engine.say("Meow Meow Meow")
        engine.runAndWait
'''


lucy = Dog("Lucy",5)
lucy.speak()

topcat = Cat("topcat",6)
topcat.speak()

animals = []
animals.appeend(lucy)
animals.append(topcat)
animals.append("Bryan")

for animal in animals:
    animal.speak() # duck typing