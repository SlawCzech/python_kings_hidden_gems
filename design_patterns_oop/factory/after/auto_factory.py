from inspect import getmembers, isclass, isabstract

import autos


class AutoFactory:
    autos = {}

    def __init__(self):
        self.load_autos()

    def load_autos(self):
        classes = getmembers(autos, lambda m: isclass(m) and not isabstract(m))
        print(classes)

        for name, _cls in classes:
            if issubclass(_cls, autos.AbsAuto):
                type(self).autos.update({name: _cls})

    def create_instance(self, car_name):
        if car_name in type(self).autos:
            return type(self).autos[car_name]()

        return autos.NullCar(car_name)


# if __name__ == '__main__':
#     auto_factory = AutoFactory()
#     print(auto_factory.autos)
