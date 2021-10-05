from src.movement import Movement
from src.orientation.orientation import Orientation


class North(Orientation):
    NORTH_ORIENTATION = "N"

    __name: str = NORTH_ORIENTATION

    def rotate_left(self):
        from src.orientation.west import West

        return West()

    def rotate_right(self):
        from src.orientation.east import East

        return East()

    @staticmethod
    def movement() -> Movement:
        return Movement(horizontal_movement=0, vertical_movement=1)

    def name(self):
        return self.__name
