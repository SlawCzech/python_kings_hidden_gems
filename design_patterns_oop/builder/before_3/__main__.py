from design_patterns_oop.builder.before_3.my_computer import MyComputer

builder = MyComputer()
builder.build_computer()
computer = builder.get_computer()
computer.display()

