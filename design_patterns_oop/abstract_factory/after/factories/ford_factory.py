from abc import ABC

from design_patterns_oop.abstract_factory.after.autos.ford.fiesta import FordFiesta
from design_patterns_oop.abstract_factory.after.autos.ford.lincoln import LincolnMKS
from design_patterns_oop.abstract_factory.after.autos.ford.mustang import FordMustang
from design_patterns_oop.abstract_factory.after.factories.abs_factory import AbsFactory


class FordFactory(AbsFactory):

    @staticmethod
    def create_economy():
        return FordFiesta()

    @staticmethod
    def create_sport():
        return FordMustang()

    @staticmethod
    def create_luxury():
        return LincolnMKS()
