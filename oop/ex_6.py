class A:
    def magic(self):
        print('class A')


class B(A):
    def magic(self):
        print('class B')


class C(B):
    def magic(self):
        print('class C')


# class X(C):
#     pass

# class X(C, A):  # bez zmian
#     pass


class X(A, C):  # nie zadziała, bo C zależy od A
    pass


print(X.__mro__)
