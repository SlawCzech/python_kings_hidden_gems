from auto_factory import AutoFactory

factory = AutoFactory()

for car_name in 'ChevyVolt', 'FordFusion', 'JeepSahara', 'Tesla':
    car = factory.create_instance(car_name)
    car.start()
    car.stop()

