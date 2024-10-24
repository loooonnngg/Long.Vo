class Car:
    def __init__(self, register_number, maximum_speed):
        self.register_number = register_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self, speed):
        self.current_speed += speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0
    def get_current_speed(self):
        return self.current_speed
    def drive(self,hour):
        self.travelled_distance += hour*self.current_speed
    def get_travelled_distance(self):
        return self.travelled_distance
    def print_information(self):
        print(f"{self.register_number}, {self.maximum_speed}, {self.current_speed}, {self.travelled_distance}")
class ElectricCar(Car):
    def __init__(self, register_number,maximum_speed,battery_capacity):
        super().__init__(register_number, maximum_speed)
        self.battery_capacity = battery_capacity
    def print_information(self):
        super().print_information()
        print(f"Battery capacity: {self.battery_capacity}")
class GasolineCar(Car):
    def __init__(self, register_number,maximum_speed,tank_volume):
        super().__init__(register_number, maximum_speed)
        self.tank_volume = tank_volume
    def print_information(self):
        super().print_information()
        print(f"Tank volume: {self.tank_volume}")
electric_car=ElectricCar("ABC-15", 180, "52.5 kWh")
gasoline_car=GasolineCar("ACD-123", 165, "32.3 l")
electric_car.accelerate(100)
gasoline_car.accelerate(120)
electric_car.drive(3)
print(electric_car.get_travelled_distance())
gasoline_car.drive(3)
print(gasoline_car.get_travelled_distance())