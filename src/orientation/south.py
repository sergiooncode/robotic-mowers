from src.movement import Movement
from src.orientation.orientation import Orientation


class South(Orientation):
    SOUTH_ORIENTATION = "S"

    __name: str = SOUTH_ORIENTATION

    def rotate_left(self):
        from src.orientation.east import East

        return East()

    def rotate_right(self):
        from src.orientation.west import West

        return West()

    @staticmethod
    def movement() -> Movement:
        return Movement(horizontal_movement=0, vertical_movement=-1)

    def name(self):
        return self.__name
