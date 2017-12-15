import random


class Car(object):
    colors = ['yellow', 'green', 'blue', 'black', 'red']

    def __init__(self, brand, color=None):
        self.brand = brand
        if not color:
            self.color = random.choice(self.colors)
        else:
            self.color = color
        self.km = 0

    def drive(self, km):
        self.km += km


c1 = Car('VW', 'red')
print(c1.km)
c1.drive(10)
print(c1.km)

Car.drive(c1, 10)
print(c1.km)

c2 = Car('BMW', 'black')

cars = [Car(brand, color) for brand, color in zip('abc', ['red', 'green', 'blue'])]

for car in cars:
    print(car.brand, car.color, car.km)

c3 = Car('Fiat')
print(c3.brand, c3.color)
c4 = Car('Audi')
print(c3.brand, c3.color)
