class LampManager:
    def __init__(self, lamps=None):
        if lamps is None:
            lamps = []
        self.lamps = lamps

    def find_by_room(self, room):
        matched_lamps = []
        for lamp in self.lamps:
            if lamp.room == room:
                matched_lamps.append(lamp)
        return matched_lamps

    def find_by_style(self, style):
        matched_lamps = []
        for lamp in self.lamps:
            if lamp.style == style:
                matched_lamps.append(lamp)
        return matched_lamps
