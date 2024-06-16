"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    engine: Engine = Engine(0, 0)

    def set_engine(self, volume, pistons):
        self.engine.volume = volume
        self.engine.pistons = pistons
