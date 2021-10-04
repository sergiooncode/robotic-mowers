from src.orientation.north import North
from src.orientation.orientation import Orientation
from src.orientation.south import South


class West(Orientation):
    WEST_ORIENTATION = "W"

    __name: str = WEST_ORIENTATION

    def rotate_left(self):
        return South()

    def rotate_right(self):
        return North()

    def name(self):
        return self.__name
