from collections import OrderedDict

print(issubclass(OrderedDict, dict))

od = OrderedDict()

print(od)

od = OrderedDict([("key1", "value1"), ("key2", "value2"), ("key3", "value3")])
print(od)

od.move_to_end("key1")
print(od)

od_ = OrderedDict([("a", 1), ("b", 2), ("c", 3)])

print(od_)
last_item = od_.popitem()

print(last_item)
print(od_)


od_ = OrderedDict([("a", 1), ("b", 2), ("c", 3)])

print(od_)
first_item = od_.popitem(last=False)

print(first_item)
print(od_)

# expected sequence of A/B test phases
expected_sequence = OrderedDict([
    ("baseline", "Original version without changes"),
    ("change1", "Increased font size for better readability"),
    ("change2", "Changed call-to-action button color"),
    ("final", "Added customer testimonials")
])

# actual sequence followed in one of the test setups
actual_sequence_test = OrderedDict([
    ("baseline", "Original version without changes"),
    ("change2", "Changed call-to-action button color"),
    ("change1", "Increased font size for better readability"),
    ("final", "Added customer testimonials")
])

print(actual_sequence_test == expected_sequence)

