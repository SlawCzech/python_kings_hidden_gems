def sentence(name):
    class Yolo:
        pass

    def full_sentence(city):
        return f"My name is {name} and city is {city}", Yolo

    return full_sentence


message = sentence("Paweł")


# print(message("Kraków"))

# print(message.__closure__[0].cell_contents)


def power10(base):
    return base ** 10


def power5(base):
    return base ** 5


def power_factory(exponent):
    def power(base):
        return base ** exponent

    return power


power10 = power_factory(10)
power5 = power_factory(10)


# generowanie id

def gen_id(idx=0):

    def next_idx(num=None):
        if num:
            next_idx.idx = num
            result = next_idx.idx
            next_idx.idx += 1
            return result
        result = next_idx.idx
        next_idx.idx += 1
        return result

    next_idx.idx = idx

    return next_idx


next_id_ = gen_id(10)

print(next_id_())
print(next_id_())
print(next_id_(50))
print(next_id_())
print(next_id_())


# def gen_id():
#     idx = [0]  # Zmienna jest przechowywana jako lista, aby obejść użycie nonlocal
#
#     def next_idx():
#         result = idx[0]
#         idx[0] += 1  # Modyfikujemy wartość listy
#         return result
#
#     return next_idx
#
# # Tworzymy closure
# generate_id = gen_id()
#
# # Wywołanie closure
# print(generate_id())  # 0
# print(generate_id())  # 1
# print(generate_id())  # 2