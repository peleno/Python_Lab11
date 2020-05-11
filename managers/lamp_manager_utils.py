from models.ceiling_lamp import CeilingLamp
from models.floor_lamp import FloorLamp
from models.rack_type import RackType
from models.room_type import RoomType
from models.shape_type import ShapeType
from models.sort_type import SortType
from models.table_lamp import TableLamp
from models.table_lamp_type import TableLampType
from models.wall_lamp import WallLamp
import doctest


class LampManagerUtils:
    @staticmethod
    def sort_by_price(lamps, sort_type=SortType.ASCENDING):
        """
        Sorts lamps by price
        :param lamps: list
        :param sort_type: SortType
        :return: list
        >>> #obj = LampManagerUtils()
        >>> result = obj.sort_by_price(lamps_list)
        >>> print(list(map(lambda x: x.price_in_uah, result)))
        [539, 1459, 2701, 3039]
        """
        if sort_type == SortType.ASCENDING:
            return sorted(lamps, key=lambda lamp: lamp.price_in_uah)
        else:
            return sorted(lamps, key=lambda lamp: lamp.price_in_uah, reverse=True)

    @staticmethod
    def sort_by_brand(lamps, sort_type=SortType.ASCENDING):
        """
        Sorts lamps by brand
        :param lamps: list
        :param sort_type: SortType
        :return: list
        >>> result = obj.sort_by_brand(lamps_list, sort_type=SortType.DESCENDING)
        >>> print(list(map(lambda x: x.brand, result)))
        ['Nordlux', 'Lampex', 'Fabbian', 'Artemide']
        """
        if sort_type == SortType.ASCENDING:
            return sorted(lamps, key=lambda lamp: lamp.brand)
        else:
            return sorted(lamps, key=lambda lamp: lamp.brand, reverse=True)


if __name__ == '__main__':
    lamps_list = [CeilingLamp("Classic", 4, "Artemide", 2701, RoomType.LIVING_ROOM, 85, 290, ShapeType.SPHERE),
                  FloorLamp("Country", 1, "Fabbian", 539, RoomType.CHILDREN_ROOM, 1510, 380, RackType.ARC),
                  TableLamp("Classic", 1, "Lampex", 1459, RoomType.BEDROOM, 440, 180, TableLampType.BEDSIDE),
                  WallLamp("Minimal", 2, "Nordlux", 3039, RoomType.BATHROOM, 120, 120, 120, ShapeType.SQUARE)]
    doctest.testmod(verbose=True, extraglobs={'obj': LampManagerUtils()})
