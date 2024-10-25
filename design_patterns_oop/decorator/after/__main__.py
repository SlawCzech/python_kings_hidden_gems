from design_patterns_oop.decorator.before.cars.luxury import Luxury
from design_patterns_oop.decorator.before.decorators.black import Black
from design_patterns_oop.decorator.before.decorators.v6 import V6
from design_patterns_oop.decorator.before.decorators.vinyl import Vinyl


def show_car(car):
    print(f"Description: {car.description}, cost: {car.cost}")


def main():
    car1 = Luxury()
    show_car(car1)
    car1 = V6(car1)
    show_car(car1)
    car = Vinyl(car1)
    show_car(car)
    car = Black(car)
    show_car(car)


if __name__ == "__main__":
    main()
