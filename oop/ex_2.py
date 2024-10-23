class Y:
    def __init__(self, value):
        print("init Y")
        self.value_y = value

class X:
    def __new__(cls, *args, **kwargs):
        # print("new X")
        # super().__new__(cls, *args, **kwargs)
        # return Y(42)
        self = super().__new__(cls)
        self.magic = 42
        return self

# jeśli new zwraca inny obiekt, to kod niżej się już nie wywoła

    def __init__(self):
        print("init X")
        self.value = 42

    def multiply_value(self, multiplier):
        return self.value * multiplier


x = X()

result = x.multiply_value(2)
result_2 = X.multiply_value(x, 3)
x.new_value = 2137
print(result)
print(result_2)
print(x.new_value)


