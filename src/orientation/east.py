from src.movement import Movement
from src.orientation.north import North
from src.orientation.orientation import Orientation
from src.orientation.south import South


class East(Orientation):
    EAST_ORIENTATION = "E"

    __name: str = EAST_ORIENTATION

    def rotate_left(self):
        return North()

    def rotate_right(self):
        return South()

    @staticmethod
    def movement() -> Movement:
        return Movement(horizontal_movement=1, vertical_movement=0)

    def name(self):
        return self.__name
