from typing import Optional

MOVE_COMMAND = "M"


class RoboticMower:

    def __init__(self, x: int, y: int, orientation: str):
        self.__x = x
        self.__y = y
        self.__orientation = orientation

    def execute(self, instructions: str) -> Optional[str]:
        if instructions == MOVE_COMMAND:
            self.__y += 1
        return self.__format_position()

    def __format_position(self):
        return f"{self.__x} {self.__y} {self.__orientation}"
