class Car:

    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0


Car1 = Car("ABC-123", 142)

print(f"License plate: {Car1.license_plate}"
      f"\nMaximum speed: {Car1.maximum_speed}"
      f"\nCurrent speed: {Car1.current_speed}"
      f"\nTravelled distance: {Car1.travelled_distance}")