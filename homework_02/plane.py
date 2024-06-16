"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 20
    max_cargo = 100

    def __init__(self, max_cargo):
        super().__init__(self.weight, self.fuel, self.fuel_consumption)
        self.max_cargo = max_cargo

    @staticmethod
    def load_cargo(load):
        try:
            if Plane.cargo + load <= aaa.max_cargo:
                Plane.cargo = Plane.cargo + load
                return Plane.cargo
            elif Plane.cargo + load > aaa.max_cargo:
                raise CargoOverload("CargoOverload")
        except CargoOverload as e:
            print(e)

    @staticmethod
    def remove_all_cargo():
        Plane.load_cargo = Plane.cargo
        return Plane.cargo


aaa = Plane(40)
Plane.load_cargo(21)
