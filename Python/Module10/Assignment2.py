class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.current_floor = bottom_floor
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    def go_to_floor(self, target_floor):
        while self.current_floor != target_floor:
            if target_floor < self.current_floor:
                self.floor_down()
            elif target_floor > self.current_floor:
                self.floor_up()

    def floor_up(self):
        self.current_floor += 1

    def floor_down(self):
        self.current_floor -= 1

class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

        self.elevators = [
            Elevator(bottom_floor, top_floor)
            for _ in range(number_of_elevators)
        ]

    def run_elevator(self, elevator_number, target_floor):
        elevator = self.elevators[elevator_number]
        elevator.go_to_floor(target_floor)