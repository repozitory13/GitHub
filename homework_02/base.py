from abc import ABC
from homework_02.exceptions import LowFuelError
from homework_02.exceptions import NotEnoughFuel
from homework_02.exceptions import CargoOverload


class Vehicle(ABC):
    weight = 500
    started = 0
    fuel = 0
    fuel_consumption = 10
    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
    def start(self, started):
        self.started = started
        if self.started == 0
            pass
        raise ValueError("not")
    pass

