from design_patterns_oop.abstract_factory.after.factories.ford_factory import FordFactory
from design_patterns_oop.abstract_factory.after.factories.gm_factory import GMFactory

for factory in FordFactory, GMFactory:
    car = factory.create_economy()
    car.start()
    car.stop()

