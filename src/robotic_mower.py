from typing import Optional

MOVE_INSTRUCTION = "M"
NORTH_ORIENTATION = "N"
SOUTH_ORIENTATION = "S"
EAST_ORIENTATION = "E"
WEST_ORIENTATION = "W"
ONE_GRID_POINT_UP = 1
ONE_GRID_POINT_DOWN = -1
ONE_GRID_POINT_RIGHT = 1
ONE_GRID_POINT_LEFT = -1


class RoboticMower:

    def __init__(self, x: int, y: int, orientation: str):
        self.__x = x
        self.__y = y
        self.__orientation = orientation

    def execute(self, instructions_string: str) -> Optional[str]:
        for instruction in self.__instructions_split_from(instructions_string):
            if self.__is_move(instruction):
                self.__move()
        return self.__format_position()

    @staticmethod
    def __instructions_split_from(instructions_string):
        return list(instructions_string)

    def __move(self):
        if self.__is_heading(NORTH_ORIENTATION):
            self.__move_vertically(ONE_GRID_POINT_UP)
        if self.__is_heading(SOUTH_ORIENTATION):
            self.__move_vertically(ONE_GRID_POINT_DOWN)
        if self.__is_heading(EAST_ORIENTATION):
            self.__move_horizontally(ONE_GRID_POINT_RIGHT)
        if self.__is_heading(WEST_ORIENTATION):
            self.__move_horizontally(ONE_GRID_POINT_LEFT)

    def __move_horizontally(self, step_size):
        self.__x = self.__x + step_size

    def __move_vertically(self, step_size):
        self.__y = self.__y + step_size

    def __format_position(self):
        return f"{self.__x} {self.__y} {self.__orientation}"

    def __is_heading(self, orientation):
        return self.__orientation == orientation

    @staticmethod
    def __is_move(instruction):
        return instruction == MOVE_INSTRUCTION
