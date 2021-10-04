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

    def name(self):
        return self.__name
