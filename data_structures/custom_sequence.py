from collections.abc import MutableSequence


class ModTwoSequence(MutableSequence):
    _list: list = []

    @staticmethod
    def _validate(self, value):
        if value % 2 != 0:
            raise ValueError("Value must be an even number")

    def insert(self, index, value):
        self._validate(self, value)
        type(self)._list.insert(index, value)

    def __getitem__(self, index):
        return type(self)._list[index]

    def __setitem__(self, index, value):
        self._validate(self, value)
        type(self)._list[index] = value

    def __delitem__(self, index):
        del type(self)._list[index]

    def __len__(self):
        return len(type(self)._list)

    def __repr__(self):
        return repr(type(self)._list)


my_seq = ModTwoSequence()
my_seq.insert(0, 40)
my_seq.insert(1, 410)
my_seq.insert(2, 42)
my_seq.insert(3, 430)

print(my_seq)
print(len(my_seq))
print(my_seq[1])

my_seq[1] = 10
print(my_seq)
del my_seq[1]
print(my_seq)
