from collections import defaultdict

# print(issubclass(defaultdict, dict))


# dd = defaultdict(list)
# print(dd)
#
# dd['magic'].append(42)
# print(dd)


# std_dict = {}
#
# std_dict.setdefault("key", "Default")
# print(std_dict["key"])
#
# dd = defaultdict(lambda: "Default")
# print(dd["key"])

#
# from timeit import timeit
#
# setup_defaultdict = """
# from collections import defaultdict
# dd = defaultdict(list)
# """
#
# stmt_defaultdict_append = "[dd[f'key_{i // 2}'].append(1) for i in range(2000000)]"
#
# time_defaultdict_append = timeit(stmt=stmt_defaultdict_append, setup=setup_defaultdict, number=100)
#
# setup_setdefault_dict = """
# std_dict = {}
# """
#
# stmt_setdefault_append = "[std_dict.setdefault(f'key_{i // 2}', []).append(1) for i in range(2000000)]"
#
# time_setdefault_append = timeit(stmt=stmt_setdefault_append, setup=setup_setdefault_dict, number=100)
#
# print(f"defaultdict: {time_defaultdict_append}\n", f"dict: {time_setdefault_append}")


# Suma dla każdej kategorii
items = [
    ("Apple", 5, "Fruit"),
    ("Banana", 3, "Fruit"),
    ("Hammer", 10, "Tool"),
    ("Screwdriver", 10, "Tool"),
    ("Laptop", 5000, "Electronics"),
    ("Smartphone", 4000, "Electronics")
]


category_dict = defaultdict(int)

for _, value, category in items:
    category_dict[category] += value

print(category_dict)

