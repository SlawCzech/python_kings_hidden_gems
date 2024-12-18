from abc import ABC, abstractmethod


class AbsFactory(ABC):

    @staticmethod
    @abstractmethod
    def create_economy():
        pass

    @staticmethod
    @abstractmethod
    def create_sport():
        pass

    @staticmethod
    @abstractmethod
    def create_luxury():
        pass
