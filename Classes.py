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


class Truck(Car):
    def drive(self, km):
        self.km += 2 * km

    def __add__(self, other):
        return Truck(self.brand + other.brand, self.color + other.color)



t1 = Truck('MAN', 'white')
print(t1.brand, t1.color, t1.km)
t1.drive(50)
print(t1.brand, t1.color, t1.km)

print(Truck.mro())

t2 = Truck('MAN')
t3 = Truck('Scania', 'black')
t4 = t2 + t3
print(t4.brand, t4.color)
