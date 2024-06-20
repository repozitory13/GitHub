from abc import ABC
from homework_02.exceptions import LowFuelError
from homework_02.exceptions import NotEnoughFuel


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
        if Vehicle.started is False and Vehicle.fuel > 0:
            Vehicle.started = True
        elif Vehicle.fuel <= 0:
            raise LowFuelError("LowFuelError")





    @staticmethod
    def move(distance):
        try:
            if Vehicle.fuel - Vehicle.fuel_consumption * distance >= 0:
                Vehicle.fuel = Vehicle.fuel - distance * Vehicle.fuel_consumption
            elif Vehicle.fuel - (Vehicle.fuel_consumption * distance) == 0:
                raise NotEnoughFuel("NotEnoughFuel")
        except Exception as e:
            return e
