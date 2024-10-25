from collections.abc import MutableMapping


class ModTwoMapping(MutableMapping):
    _mapping: dict = {}

    @staticmethod
    def _validate(self, value):
        if value % 2 != 0:
            raise ValueError("Value must be an even number")

    def __setitem__(self, __key, __value):
        self._validate(self, __value)
        type(self)._mapping[__key] = __value

    def __delitem__(self, __key):
        del type(self)._mapping[__key]

    def __getitem__(self, __key):
        return type(self)._mapping[__key]

    def __len__(self):
        return len(type(self)._mapping)

    def __iter__(self):
        return iter(type(self)._mapping.values())

    def __repr__(self):
        return repr(type(self)._mapping)


m = ModTwoMapping()
m[1] = 42
m['ala'] = 666
print(m[1])

for val in m:
    print(val)

