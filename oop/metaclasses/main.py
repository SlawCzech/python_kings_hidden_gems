class Widget:
    pass


class Widget2(object, metaclass=type): # pełen zapis defaultowy
    pass


# tworzenie klasy na piechotę
name = "Widget3"
metaclass = type
bases = ()
kwargs = {}
namespace = metaclass.__prepare__(name, bases, **kwargs) # tak powstaje namespace

Widget3 = metaclass.__new__(metaclass, name, bases, namespace, **kwargs) # tutaj mam nowy obiekt klasy
metaclass.__init__(Widget3, name, bases, namespace, **kwargs)

print(Widget3)
w = Widget3()
print(w)

