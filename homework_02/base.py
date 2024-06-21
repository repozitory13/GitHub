from abc import ABC
from homework_02.exceptions import NotEnoughFuel
from homework_02.exceptions import LowFuelError


class Vehicle(ABC):
    weight: int
    started: bool
    fuel: int
    fuel_consumption: int

    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        while (self.started is False or True) and self.fuel > 0:
            self.started = True
            break
        else:
            raise LowFuelError("LowFuelError")

    def move(self, distance):
        if self.fuel - self.fuel_consumption * distance >= 0:
            xxx = self.fuel - distance * self.fuel_consumption
            self.fuel = xxx
            return self.fuel
        elif self.fuel - (self.fuel_consumption * distance) <= 0:
            raise NotEnoughFuel("NotEnoughFuel")
