from abc import ABC
from homework_02.exceptions import LowFuelError
#from homework_02.exceptions import NotEnoughFuel
#from homework_02.exceptions import CargoOverload


class Vehicle(ABC):
    weight = None
    started = None
    fuel = None
    fuel_consumption = None

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self, started):
        try:
            print(started)
            if started == 0:
                print('ok')
        except Exception as e:
            raise LowFuelError
            print("m")
#            pass


Vehicle(500, 0, 10)
Vehicle.start(1, 1)
