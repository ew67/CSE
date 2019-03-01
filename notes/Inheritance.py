class Vehicle(object):
    def __init__(self, name, engine):
        self.name = name
        self.engine_type = engine


class Car(Vehicle):
    def __init__(self, name, engine_type, body_type):
        super(Car, self).__init__(name, engine_type)
        self.body_type = body_type
        self.steering_wheel = True
        self.engine_status = False  # Because the engine is off
        self.fuel = 100

    def start_engine(self):
        self.engine_status = True
        print("You turn the key and the car turns on.")

    def move_forward(self):
        self.fuel -= 1
        print("You move forward.")

    def turn_left(self):
        self.fuel -= 1
        print("You turn left.")

    def right_turn(self):
        self.fuel -= 1
        print("You turn right.")

    def move_backward(self):
        self.fuel -= 1
        print("You move backward")

    def turn_off(self):
        self.engine_status = False
        print("You turn the engine off.")


class Tesla(Car):
    def __init__(self):
        super(Tesla, self).__init__("Tesla", "Electric", "slim")


class KeylessCar(Car):
    def __init__(self, name, engine_type, body_type):
        super(KeylessCar, self).__init__(name, engine_type, body_type)

    def start_engine(self):
        self.engine_status = True
        print("You push the button and the car starts.")




my_car = Tesla()
my_car.start_engine()
my_car.move_forward()

adam_car = KeylessCar("Adam's Ride", "Diesel", "Toaster")  # This is an instance
adam_car.start_engine()
adam_car.move_forward()
adam_car.turn_off()
