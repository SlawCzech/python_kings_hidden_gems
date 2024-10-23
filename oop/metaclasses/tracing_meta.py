from oop.location.position import auto_repr


class TracingMeta(type):

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):  # tutaj manipuluje się typem wartości, które trafią do namespace
        print("TracingMeta.__prepare__")
        print(f" {mcs = }")
        print(f" {name = }")
        print(f" {bases = }")
        print(f" {kwargs = }")

        namespace = super().__prepare__(name, bases)

        print(f" -> {namespace = }")
        return namespace

    def __new__(mcs, name, bases, namespace, **kwargs):  # konfiguracja nowej klasy (pola, metody)
        print("TracingMeta.__new__")
        print(f" {mcs = }")
        print(f" {name = }")
        print(f" {bases = }")
        print(f" {kwargs = }")

        cls = super().__new__(mcs, name, bases, namespace)
        setattr(cls, "__repr__", auto_repr)
        print(f" -> {cls = }")

        return cls

    def __init__(cls, name, bases, namespace, **kwargs):
        print("TracingMeta.__init__")
        print(f" {cls = }")
        print(f" {name = }")
        print(f" {bases = }")
        print(f" {kwargs = }")

        super().__init__(name, bases, namespace)


class Widget(metaclass=TracingMeta):
    the_answer = 42

    def action(self, message):
        print(message)
