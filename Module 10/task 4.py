import random
class Car:
    def __init__(self, register_number, maximum_speed,current_speed=0,travelled_distance=0):
        self.register_number = register_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance
    def accelerate(self, speed):
        self.current_speed += speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0
    def get_current_speed(self):
        return self.current_speed
    #task 3
    def drive(self,hour):
        self.travelled_distance += hour*self.current_speed
    def get_travelled_distance(self):
        return self.travelled_distance
    def print_information(self):
        print(f"{self.register_number} | {self.maximum_speed} | {self.current_speed} | {self.travelled_distance}")

#task 4

class Race:
    def __init__(self, name,distance,list_of_car):
        self.name = name
        self.distance = distance
        self.list_of_car = list_of_car
    def hour_passes(self):
        for car in self.list_of_car:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
    def print_status(self):
        for car in self.list_of_car:
            car.print_information()
    def race_finished(self):
        for car in self.list_of_car:
            if car.get_travelled_distance() >=10000:
                return True
list_of_car=[]
time=0
for i in range(10):
    list_of_car.append(Car(f"ABC-{i+1}",random.randint(100,200)))
race=Race("Grand Demolition Derby",8000,list_of_car)
while True:
    race.hour_passes()
    if race.race_finished():
        race.print_status()
        break
    if time%10==0:
        race.print_status()