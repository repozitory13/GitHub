"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine
from homework_02 import engine


class Car(Vehicle):
    engine: int
#    Engine(0, 0)

    def set_engine(self, zzz):
        self.zzz = zzz
        Car.engine = zzz
