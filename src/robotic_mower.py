from typing import Optional

MOVE_INSTRUCTION = "M"
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
            if self.__is_move(instruction):
                if self.__is_heading(NORTH_ORIENTATION):
                    self.__y += 1
                if self.__is_heading(SOUTH_ORIENTATION):
                    self.__y -= 1
                if self.__is_heading(EAST_ORIENTATION):
                    self.__x -= 1
                if self.__is_heading(WEST_ORIENTATION):
                    self.__x += 1
        return self.__format_position()

    def __format_position(self):
        return f"{self.__x} {self.__y} {self.__orientation}"

    def __is_heading(self, orientation):
        return self.__orientation == orientation

    @staticmethod
    def __is_move(instruction):
        return instruction == MOVE_INSTRUCTION
