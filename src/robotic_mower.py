from typing import Optional

from src.position import Position

MOVE_INSTRUCTION = "M"
NORTH_ORIENTATION = "N"
SOUTH_ORIENTATION = "S"
EAST_ORIENTATION = "E"
WEST_ORIENTATION = "W"
ONE_GRID_POINT_UP = 1
ONE_GRID_POINT_DOWN = -1
ONE_GRID_POINT_RIGHT = 1
ONE_GRID_POINT_LEFT = -1
POSITION_FORMAT = "{x} {y} {orientation}"


class RoboticMower:
    def __init__(self, position: Position):
        self.__position = position

    def execute(self, instructions_string: str) -> Optional[str]:
        for instruction in self.__instructions_split_from(instructions_string):
            if self.__is_move(instruction):
                self.__move()
            if instruction == "L":
                if self.__position.orientation == "N":
                    self.__position.orientation = "W"
                elif self.__position.orientation == "S":
                    self.__position.orientation = "E"
                elif self.__position.orientation == "W":
                    self.__position.orientation = "S"
                elif self.__position.orientation == "E":
                    self.__position.orientation = "N"
            if instruction == "R":
                if self.__position.orientation == "N":
                    self.__position.orientation = "E"
                elif self.__position.orientation == "S":
                    self.__position.orientation = "W"
                elif self.__position.orientation == "W":
                    self.__position.orientation = "N"
                elif self.__position.orientation == "E":
                    self.__position.orientation = "S"
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
        self.__position.x += step_size

    def __move_vertically(self, step_size):
        self.__position.y += step_size

    def __format_position(self):
        return POSITION_FORMAT.format(
            x=self.__position.x,
            y=self.__position.y,
            orientation=self.__position.orientation,
        )

    def __is_heading(self, orientation):
        return self.__position.orientation == orientation

    @staticmethod
    def __is_move(instruction):
        return instruction == MOVE_INSTRUCTION
