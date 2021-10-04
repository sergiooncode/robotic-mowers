from dataclasses import dataclass

from src.orientation.east import East
from src.orientation.north import North
from src.orientation.orientation import Orientation
from src.orientation.south import South
from src.orientation.west import West

ONE_GRID_POINT_UP = 1
ONE_GRID_POINT_DOWN = -1
ONE_GRID_POINT_RIGHT = 1
ONE_GRID_POINT_LEFT = -1


@dataclass
class RoboticMower:
    x: int
    y: int
    orientation: Orientation

    def __is_heading(self, orientation_name):
        return self.orientation.name() == orientation_name

    def __move_horizontally(self, step_size):
        self.x += step_size

    def __move_vertically(self, step_size):
        self.y += step_size

    def move(self) -> None:
        if self.__is_heading(North.NORTH_ORIENTATION):
            self.__move_vertically(ONE_GRID_POINT_UP)
        if self.__is_heading(South.SOUTH_ORIENTATION):
            self.__move_vertically(ONE_GRID_POINT_DOWN)
        if self.__is_heading(East.EAST_ORIENTATION):
            self.__move_horizontally(ONE_GRID_POINT_RIGHT)
        if self.__is_heading(West.WEST_ORIENTATION):
            self.__move_horizontally(ONE_GRID_POINT_LEFT)

    def turn_right(self) -> None:
        if self.__is_heading(North.NORTH_ORIENTATION):
            self.orientation = North().rotate_right()
        elif self.__is_heading(South.SOUTH_ORIENTATION):
            self.orientation = South().rotate_right()
        elif self.__is_heading(West.WEST_ORIENTATION):
            self.orientation = West().rotate_right()
        elif self.__is_heading(East.EAST_ORIENTATION):
            self.orientation = East().rotate_right()

    def turn_left(self) -> None:
        if self.__is_heading(North.NORTH_ORIENTATION):
            self.orientation = North().rotate_left()
        elif self.__is_heading(South.SOUTH_ORIENTATION):
            self.orientation = South().rotate_left()
        elif self.__is_heading(West.WEST_ORIENTATION):
            self.orientation = West().rotate_left()
        elif self.__is_heading(East.EAST_ORIENTATION):
            self.orientation = East().rotate_left()
