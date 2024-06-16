from abc import ABC
from homework_02.exceptions import LowFuelError
from homework_02.exceptions import NotEnoughFuel
from homework_02.exceptions import CargoOverload


class Vehicle(ABC):
    weight = 0
    started = False
#    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption


    @staticmethod
    def start():
        try:
            if Vehicle.started is False and Vehicle.fuel > 0:
                Vehicle.started = True
            elif Vehicle.fuel <= 0:
                raise LowFuelError("LowFuelError")
        except LowFuelError as e:
            print(e)

    @staticmethod
    def move(dist):
        try:
            if Vehicle.fuel // (Vehicle.fuel_consumption * dist) >= 1:
                return Vehicle.fuel - (Vehicle.fuel_consumption * dist)
            elif Vehicle.fuel - (Vehicle.fuel_consumption * dist) < 0:
                raise NotEnoughFuel("NotEnoughFuel")
        except NotEnoughFuel as e:
            print(e)


#res = Vehicle(30, 50, 10)
#Vehicle.start(1)
#print(res.fuel)
#print(res.move(3))
