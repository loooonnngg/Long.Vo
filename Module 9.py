import random
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
    #task 3
    def drive(self,hour):
        self.travelled_distance += hour*self.current_speed
    def get_travelled_distance(self):
        return self.travelled_distance
    def __str__(self):
        return f"{self.register_number}, {self.maximum_speed}, {self.current_speed}, {self.travelled_distance}"
#task 1
new_car= Car("ABC-123",142)
print(str(new_car))

#task 2
new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)
print(new_car.get_current_speed())
new_car.accelerate(-200)
print(new_car.get_current_speed())

#task 4
list_of_car=[]
race_status=None
for i in range(10):
    list_of_car.append(Car(f"ABC-{i+1}",random.randint(100,200)))

while True:
    for car in list_of_car:
        car.accelerate(random.randint(-10,15))
        car.drive(1)
        if car.get_travelled_distance() >=10000:
            race_status=True
            break
    if race_status:
        break
for i in list_of_car:
    print(str(i))