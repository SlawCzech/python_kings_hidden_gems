from design_patterns_oop.abstract_factory.after.autos.gm.cadillac import CadillacCTS
from design_patterns_oop.abstract_factory.after.autos.gm.camaro import ChevyCamaro
from design_patterns_oop.abstract_factory.after.autos.gm.spark import ChevySpark
from design_patterns_oop.abstract_factory.after.factories.abs_factory import AbsFactory


class GMFactory(AbsFactory):

    @staticmethod
    def create_economy():
        return ChevySpark()

    @staticmethod
    def create_sport():
        return ChevyCamaro()

    @staticmethod
    def create_luxury():
        return CadillacCTS()
