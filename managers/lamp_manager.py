import doctest
import sys
from pprint import pprint

from models.ceiling_lamp import CeilingLamp
from models.floor_lamp import FloorLamp
from models.rack_type import RackType
from models.room_type import RoomType
from models.shape_type import ShapeType
from models.table_lamp import TableLamp
from models.table_lamp_type import TableLampType
from models.wall_lamp import WallLamp

a = 5


class LampManager:
    """
    >>> living_room_lamp = obj.find_by_room(RoomType.LIVING_ROOM)
    >>> living_room_lamp[0].style
    'Luxury'
    """

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


if __name__ == "__main__":
    print('hello from lamp manager')
    lamps_list = [CeilingLamp("Luxury", 4, "Artemide", 2701, RoomType.LIVING_ROOM, 85, 290, ShapeType.SPHERE),
                  FloorLamp("Country", 1, "Fabbian", 539, RoomType.CHILDREN_ROOM, 1510, 380, RackType.ARC),
                  TableLamp("Classic", 1, "Lampex", 1459, RoomType.BEDROOM, 440, 180, TableLampType.BEDSIDE),
                  WallLamp("Minimal", 2, "Nordlux", 3039, RoomType.BATHROOM, 120, 120, 120, ShapeType.SQUARE)]
    doctest.testmod(verbose=True, extraglobs={'obj': LampManager(lamps_list)})
# pprint(sys.modules['__main__'].__dict__)


