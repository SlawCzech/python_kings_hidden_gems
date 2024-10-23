class A:
    magic = 42

    @classmethod
    def yolo(cls):
        return 42

# print(A.magic)

print(type(5))


def yolo(obj):
    obj.xd = 42


Magic = type('Magic', (object,),
             {
                 'magic': 42,
                 # '__init__': yolo,
                 '__init__': lambda obj: setattr(obj, 'xd', 42),
                 'true_magic': classmethod(lambda obj: setattr(obj, 'xd', 42))
             })

m = Magic()

print(m.magic)
print(m.xd)

print(m)
