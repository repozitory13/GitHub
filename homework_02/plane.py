"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo = 100

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        Plane.max_cargo = max_cargo
        Plane.cargo = 0

    @staticmethod
    def load_cargo(load):
        if Plane.cargo + load <= Plane.max_cargo:
            Plane.cargo = Plane.cargo + load
        elif Plane.cargo + load > Plane.max_cargo:
#            Plane.cargo = 0
            raise CargoOverload("CargoOverload")

    @staticmethod
    def remove_all_cargo():
        res = Plane.cargo
        Plane.cargo = 0
        return res


if __name__ == "__main__":
    Plane.remove_all_cargo()
    Plane.load_cargo(load=0)
