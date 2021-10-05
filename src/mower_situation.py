from src.command.move.movement_command import MovementCommand
from src.orientation.orientation import Orientation
from src.position import Position

POSITION_FORMAT = "{x} {y} {orientation}"


class MowerSituation:
    def __init__(self, position: Position, orientation: Orientation):
        self.__position = position
        self.__orientation = orientation

    def move_forward(self, movement_command: MovementCommand):
        movement = movement_command.move(self.__orientation)
        return self.__with_position(self.__position.move(movement))

    def __with_position(self, move: Position):
        return MowerSituation(move, self.__orientation)

    def rotate(self, rotation):
        return self.__with_orientation(rotation.rotate(self.__orientation))

    def __with_orientation(self, rotate: Orientation):
        return MowerSituation(self.__position, rotate)

    def format_position(self):
        return POSITION_FORMAT.format(
            x=self.__position.x,
            y=self.__position.y,
            orientation=self.__orientation.name(),
        )
