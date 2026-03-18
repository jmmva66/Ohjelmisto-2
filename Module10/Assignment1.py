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