value_ = [[i] for i in range(1000000)]
another_ = [[i] for i in range(1000000)]


class Magic:
    __slots__ = ['value', 'another']  # blokuje dodanie __dict__ !!! dlatego nie da się nic nowego dodawać do obiektów!

    def __init__(self, value, another):
        self.value = value
        self.another = another


# m = Magic(22, 2137)
# print(vars(m))
# m.xd = 42 # poleci błąd!!! bo nie ma __dict__


def main():
    import tracemalloc
    tracemalloc.start()
    n = [Magic(value_, another_) for i in range(10000)]
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(peak)


main()
