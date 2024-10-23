import inspect
from dataclasses import dataclass


def auto_repr(cls):
    members = vars(cls)

    if "__repr__" in members:
        raise TypeError(f'{cls.__name__} already defines __repr__')

    if "__init__" not in members:
        raise TypeError(f'{cls.__name__} does not override __init__')

    signature = inspect.signature(cls.__init__)
    parameter_names = list(signature.parameters)[1:]

    if not all(members.get(name, None) for name in parameter_names):
        raise TypeError(f'Cannot apply auto repr to {cls.__name__}, because not all '
                        f'__init__ parameters have matching properties.')

    def synthesized_repr(self):
        return "{type_class}({args}".format(
            type_class=type(self).__name__,
            args=", ".join(f'{name}={getattr(self, name)!r}' for name in parameter_names)
        )

    setattr(cls, "__repr__", synthesized_repr)

    return cls


@auto_repr
class Position:
    def __init__(self, latitude, longitude):
        if not (-90 <= latitude <= +90):
            raise ValueError(f"Latitude {latitude} out of range")

        if not (-180 <= longitude <= +180):
            raise ValueError(f"Longitude {longitude} out of range")

        self._latitude = latitude
        self._longitude = longitude

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    @property
    def latitude_hemisphere(self):
        return "N" if self._latitude >= 0 else "S"

    @property
    def longitude_hemisphere(self):
        return "E" if self._longitude >= 0 else "W"

    # def __repr__(self):
    #     return f"{type(self).__name__}(latitude={self._latitude}, longitude={self._longitude})"

    def __str__(self):
        return format(self)

    def __format__(self, format_spec):
        component_format_spec = ".2f"
        prefix, dot, suffix = format_spec.partition(".")

        if dot:
            num_decimal_places = int(suffix)
            component_format_spec = f".{num_decimal_places}f"

        latitude = format(abs(self._latitude), component_format_spec)
        longitude = format(abs(self._longitude), component_format_spec)

        return f"{latitude} {self.latitude_hemisphere}, {longitude} {self.longitude_hemisphere}"

    def __eq__(self, other):
        if not isinstance(other, Position):
            return NotImplemented

        return self.latitude == other.latitude and self.longitude == other.longitude

    def __hash__(self):
        return hash((self.latitude, self.longitude))  # hash z tupli dwuelementowej


class EarthPosition(Position):
    pass


class MarsPosition(Position):
    pass


@auto_repr
class Location:
    def __init__(self, name, position):
        self._name = name
        self._position = position

    @property
    def name(self):
        return self._name

    @property
    def position(self):
        return self._position

    # def __repr__(self):
    #     return f"{type(self).__name__}(name={self.name}, position={self.position})"

    def __str__(self):
        return self.name


@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=True, frozen=True)
class Location2:
    name: str
    position: Position

    def __post_init__(self):
        if self.name == "":
            raise ValueError(f"Name cannot be an empty string")


# hong_kong = Location("Hong Kong", EarthPosition(22.29, 114.16))
# cape_town = Location("Cape Town", EarthPosition(-33.93, 18.42))

hong_kong = Location2("Hong Kong", EarthPosition(22.29, 114.16))
hong_kong2 = Location2("Hong Kong", EarthPosition(22.29, 114.16))
cape_town = Location2("Cape Town", EarthPosition(-33.93, 18.42))

print(f'{hong_kong!r}')
print(f'{cape_town!r}')

print(hong_kong == cape_town)

# ep = EarthPosition(22.29, 113.16)
# mp = MarsPosition(22.29, 113.16)
#
# print(ep == mp)
# print(hash(mp))
# print(hash(ep))

# hong_kong2.name = "Krakow"
