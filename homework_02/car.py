"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle


class Car(Vehicle):
    engine: int
#    Engine(0, 0)

    @staticmethod
    def set_engine(zzz):
        Car.engine = zzz


if __name__ == "__main__":
    Car.set_engine(zzz=0)
