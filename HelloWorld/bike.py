class Bike:
    def __init__(self, color, frame_material):
        self.color = color
        self.frame_material = frame_material

    def brake(self):
        print("Breaking!")

red_bike = Bike('Red', 'Carbon fiber')

print(red_bike.color)
red_bike.brake()
