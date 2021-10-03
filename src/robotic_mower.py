from dataclasses import dataclass

NORTH_ORIENTATION = "N"
SOUTH_ORIENTATION = "S"
EAST_ORIENTATION = "E"
WEST_ORIENTATION = "W"
ONE_GRID_POINT_UP = 1
ONE_GRID_POINT_DOWN = -1
ONE_GRID_POINT_RIGHT = 1
ONE_GRID_POINT_LEFT = -1


@dataclass
class RoboticMower:
    x: int
    y: int
    orientation: str

    def __is_heading(self, orientation):
        return self.orientation == orientation

    def __move_horizontally(self, step_size):
        self.x += step_size

    def __move_vertically(self, step_size):
        self.y += step_size

    def move(self) -> None:
        if self.__is_heading(NORTH_ORIENTATION):
            self.__move_vertically(ONE_GRID_POINT_UP)
        if self.__is_heading(SOUTH_ORIENTATION):
            self.__move_vertically(ONE_GRID_POINT_DOWN)
        if self.__is_heading(EAST_ORIENTATION):
            self.__move_horizontally(ONE_GRID_POINT_RIGHT)
        if self.__is_heading(WEST_ORIENTATION):
            self.__move_horizontally(ONE_GRID_POINT_LEFT)

    def turn_right(self) -> None:
        if self.__is_heading(NORTH_ORIENTATION):
            self.orientation = EAST_ORIENTATION
        elif self.__is_heading(SOUTH_ORIENTATION):
            self.orientation = WEST_ORIENTATION
        elif self.__is_heading(WEST_ORIENTATION):
            self.orientation = NORTH_ORIENTATION
        elif self.__is_heading(EAST_ORIENTATION):
            self.orientation = SOUTH_ORIENTATION

    def turn_left(self) -> None:
        if self.__is_heading(NORTH_ORIENTATION):
            self.orientation = WEST_ORIENTATION
        elif self.__is_heading(SOUTH_ORIENTATION):
            self.orientation = EAST_ORIENTATION
        elif self.__is_heading(WEST_ORIENTATION):
            self.orientation = SOUTH_ORIENTATION
        elif self.__is_heading(EAST_ORIENTATION):
            self.orientation = NORTH_ORIENTATION
