from src.movement import Movement


class Position:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def move(self, movement: Movement):
        return Position(
            self.__x + movement.horizontal_movement, self.__y + movement.vertical_movement
        )

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
