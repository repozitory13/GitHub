from abc import ABC
from homework_02.exceptions import LowFuelError
from homework_02.exceptions import NotEnoughFuel
from homework_02.exceptions import CargoOverload


class Vehicle(ABC):
    weight = None
    started = 0
    fuel = None
    fuel_consumption = None

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    @staticmethod
    def start():
        try:
            if Vehicle.started != 1 and res.fuel > 0:
                Vehicle.started += 1
                return Vehicle.started
            elif res.fuel <= 0:
                raise LowFuelError("LowFuelError")
        except LowFuelError as e:
            print(e)

    @staticmethod
    def move(dist):
        try:
            if res.fuel // (res.fuel_consumption * dist) >= 1:
                return res.fuel - (res.fuel_consumption * dist)
            elif res.fuel - (res.fuel_consumption * dist) < 0:
                raise NotEnoughFuel("NotEnoughFuel")
        except NotEnoughFuel as e:
            print(e)


res = Vehicle(30, 50, 10)
#Vehicle.start(1)
#print(res.fuel)
print(res.move(3))
