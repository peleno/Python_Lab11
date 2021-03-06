from models.lamp import Lamp


class WallLamp(Lamp):
    def __init__(self, style, count_of_bulbs, brand, price_in_uah, room, height_in_mm, width_in_mm, depth_in_mm, shape):
        super().__init__(style, count_of_bulbs, brand, price_in_uah, room, height_in_mm, width_in_mm)
        self.depth_in_mm = depth_in_mm
        self.shape = shape
