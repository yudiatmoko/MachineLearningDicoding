
class Car:
    def __init__(self, color, merk, speed):
        self.color = color
        self.merk = merk
        self.speed = speed

    def addSpeed(self):
        self.speed += 10

car1 = Car("Red", "Honda", 250)
print(car1.speed)

class SportCar(Car):
    def addTurbo(self):
        self.speed += 50

car2 = SportCar("Blue", "Lamborghini", 350)
car2.addTurbo()
print(car2.speed)

# Override
class SportCar2(Car):
    def addSpeed(self):
        self.speed += 20

    def addTurbo(self):
        self.speed += 50

car3 = SportCar2("Green", "Ferrari", 190)
print(car3.speed)
car3.addSpeed()
print(car3.speed)

# Super Class
class SportCar3(Car):
    def addSpeed(self):
        super().addSpeed()
        print("Be careful, your speed is high")
    def addTurbo(self):
        self.speed += 50

car4 = SportCar3("Yellow", "BMW", 200)
print(car4.speed)
car4.addSpeed()
print(car4.speed)

# Quiz
class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

class Cat(Animal):
    def description(self):
        return f"{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"

    def catSound(self):
        return "meow!"

myCat = Cat("Neko", 3, "Persian")
print(myCat.description())
print(myCat.catSound())
