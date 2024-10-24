#task 1
class Elevator:
    def __init__(self, bottom_floor,top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor
    def floor_up(self):
        self.current_floor+=1
    def floor_down(self):
        self.current_floor-=1
    def go_to_floor(self,floor):
        if floor-self.current_floor>0:
            for i in range(abs(floor-self.current_floor)):
                self.floor_up()
                print(f"The elevator is now at floor {self.current_floor}")
        elif floor-self.current_floor<0:
            for i in range(abs(floor-self.current_floor)):
                self.floor_down()
                print(f"The elevator is now at floor {self.current_floor}")
        else:
            print("you are already at that floor")
h=Elevator(1,20)
h.go_to_floor(5)
h.go_to_floor(1)
#task 2
class Building:
    def __init__(self, bottom_floor,top_floor,num_of_elevator):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.num_of_elevator = num_of_elevator
        self.elevators=[]
        for i in range(num_of_elevator):
            self.elevators.append(Elevator(bottom_floor,top_floor))
    def run_elevators(self,num_of_elevator,des_floor):
        for elevator in self.elevators:
            elevator.go_to_floor(des_floor)
    #task 3
    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)
building=Building(1,7,3)
building.run_elevators(3,5)
building.fire_alarm()