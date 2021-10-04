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

    def name(self):
        return self.__name
