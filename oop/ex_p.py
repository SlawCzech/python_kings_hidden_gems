# 2 < value < 10

class X:
    def __init__(self, value: str):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not (2 < len(value) < 10):
            raise ValueError("Something is no yes!")
        self._value = value


x = X('Roman')
x.value = "ala ma "
x._value = "ala ma kota i HIV i AIDS i wszy"
print(x.value)
print(vars(x))
print(vars(X))