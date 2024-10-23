from oop.shipping import iso6346


class ShippingContainer(object, metaclass=type):
    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0

    next_serial = 1337

    @staticmethod
    def _generate_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    # to samo ale metodą klasy
    @classmethod
    def _generate_serial2(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod  # customowy konstruktor!!!
    def create_empty(cls, owner_code, length_ft, **kwargs):
        return cls(owner_code, length_ft, contents=[], **kwargs)

    @classmethod  # customowy konstruktor!!!
    def create_with_items(cls, owner_code, length_ft, items, **kwargs):
        return cls(owner_code, length_ft, contents=list(items), **kwargs)

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6)
        )

    def __init__(self, owner_code, length_ft, contents, **kwargs):
        self.length_ft = length_ft
        self.owner_code = owner_code
        self.contents = contents
        # self.serial = ShippingContainer._generate_serial()
        self.bic = self._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._generate_serial()
        )

    @property
    def volume_ft3(self):
        return self._calc_volume()

    def _calc_volume(self):
        return ShippingContainer.WIDTH_FT * ShippingContainer.WIDTH_FT * self.length_ft


class RefrigeratedShippingContainer(ShippingContainer):
    MAX_CELSIUS = 4.0
    FRIDGE_VOLUME_FT3 = 100

    def __init__(self, owner_code, length_ft, contents, *, celsius, **kwargs):
        super().__init__(owner_code, length_ft, contents, **kwargs)
        self.celsius = celsius

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category='R'
        )

    @property
    def celsius(self):
        return f'{self._celsius} C'

    @celsius.setter
    def celsius(self, value):
        self._set_celsius(value)

    def _set_celsius(self, value):
        if value > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temp too high!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9

    def _calc_volume(self):
        return super()._calc_volume() - RefrigeratedShippingContainer.FRIDGE_VOLUME_FT3


class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):
    MIN_CELSIUS = -20

    # @RefrigeratedShippingContainer.celsius.setter
    # def celsius(self, value):
    #     if not (HeatedRefrigeratedShippingContainer.MIN_CELSIUS < value < RefrigeratedShippingContainer.MAX_CELSIUS):
    #         raise ValueError("Invalid temperature")
    #     self._celsius = value

    def _set_celsius(self, value):
        if value < RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temp too low!")
        super()._set_celsius(value)


# ISO:6346
code = 'CSQU305438'

r1 = ShippingContainer('YML', 20, ['onion'], celsius=2.0)
r2 = HeatedRefrigeratedShippingContainer('YML', 20, ['onion'], celsius=2.0)
r3 = RefrigeratedShippingContainer.create_empty('YML', 20, celsius=-230.0)
r4 = RefrigeratedShippingContainer.create_with_items('YML', 20, ['Snow', 'Ice'], celsius=-230.0)

# print(r1.celsius)
print(r2.celsius)
print(r3.celsius)
print(r4.celsius)
