from typing import Optional

MOVE_COMMAND = "M"
NORTH_ORIENTATION = "N"
SOUTH_ORIENTATION = "S"
EAST_ORIENTATION = "E"
WEST_ORIENTATION = "W"


class RoboticMower:

    def __init__(self, x: int, y: int, orientation: str):
        self.__x = x
        self.__y = y
        self.__orientation = orientation

    def execute(self, instructions: str) -> Optional[str]:
        for instruction in list(instructions):
            if instruction == MOVE_COMMAND:
                if self.__orientation == NORTH_ORIENTATION:
                    self.__y += 1
                if self.__orientation == SOUTH_ORIENTATION:
                    self.__y -= 1
                if self.__orientation == EAST_ORIENTATION:
                    self.__x -= 1
                if self.__orientation == WEST_ORIENTATION:
                    self.__x += 1
        return self.__format_position()

    def __format_position(self):
        return f"{self.__x} {self.__y} {self.__orientation}"
