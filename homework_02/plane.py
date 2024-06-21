"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo: int
    max_cargo: int

    def __init__(self, weight=0, fuel=0, fuel_consumption=0, max_cargo=0):
        self.cargo = 0
        self.max_cargo = max_cargo
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.started = False


    def load_cargo(self, load):
        if self.cargo + load <= self.max_cargo:
            self.cargo = self.cargo + load
        elif self.cargo + load > self.max_cargo:
#            Plane.cargo = 0
            raise CargoOverload("CargoOverload")

    def remove_all_cargo(self):
        res = self.cargo
        self.cargo = 0
        return res
