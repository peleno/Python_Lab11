from models.lamp import Lamp


class FloorLamp(Lamp):
    def __init__(self, style, count_of_bulbs, brand, price_in_uah, room, height_in_mm, width_in_mm, rack):
        super().__init__(style, count_of_bulbs, brand, price_in_uah, room, height_in_mm, width_in_mm)
        self.rack = rack