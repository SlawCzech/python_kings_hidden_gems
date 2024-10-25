from abc import ABC

from design_patterns_oop.decorator.before.cars.abs_car import AbsCar


class AbsDecorator(AbsCar, ABC):
    def __init__(self, car):
        self._car = car

    @property
    def car(self):
        return self

    @property
    def premium(self):
        return self._car.premium
