from abc import ABC
from homework_02.exceptions import NotEnoughFuel
from homework_02.exceptions import LowFuelError


class Vehicle(ABC):
    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        Vehicle.weight = weight
        Vehicle.fuel = fuel
        Vehicle.fuel_consumption = fuel_consumption
        Vehicle.started = False

    @staticmethod
    def start():
        while Vehicle.fuel is not 0:
            Vehicle.started = True
            break
        else:
            Vehicle.fuel = 0
            Vehicle.started = False
            raise LowFuelError("LowFuelError")



    @staticmethod
    def move(distance):
        if Vehicle.fuel - Vehicle.fuel_consumption * distance >= 0:
            xxx = Vehicle.fuel - distance * Vehicle.fuel_consumption
            Vehicle.fuel = xxx
        elif Vehicle.fuel - (Vehicle.fuel_consumption * distance) == 0:
            raise NotEnoughFuel("NotEnoughFuel")

#res = Vehicle(20, 0, 40)
#res.start()
#print(Vehicle.started)


if __name__ == "__main__":
    Vehicle.start()
