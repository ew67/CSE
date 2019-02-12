class WaterGun(object):
    def __init__(self, capacity, distance, stock, duration):
        # These are things that a WaterGun has.
        # All of these should be relevant to our program.
        self.capacity = capacity
        self.range = distance
        self.trigger = True # Someone's triggered?
        self.stock = stock
        self.duration_of_pressure = 5

    def shoot(self, time):
        if self.trigger:
            if self.duration_of_pressure <= 0:
                print("There's no pressure")
            elif self.duration_of_pressure < time:
                print("You've ran out of pressure after firing for %s seconds.", self.duration_of_pressure)
                self.duration_of_pressure = 0
            else:
                print("You shoot for %s seconds.", time)
                self.duration_of_pressure -= time
        else:
            print("There's no trigger!")


my_water_gun = WaterGun(1.0, 1, False, 10)

