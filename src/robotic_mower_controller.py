from typing import Optional

from src.orientation.east import East
from src.orientation.north import North
from src.orientation.south import South
from src.orientation.west import West
from src.robotic_mower import RoboticMower

MOVE_INSTRUCTION = "M"
LEFT_TURN_INSTRUCTION = "L"
RIGHT_TURN_INSTRUCTION = "R"
POSITION_FORMAT = "{x} {y} {orientation}"


class RoboticMowerController:
    def __init__(self, mower: RoboticMower):
        self.__mower = mower

    def execute(self, instructions_string: str) -> Optional[str]:
        instruction_to_command_map = {
            MOVE_INSTRUCTION: self.__mower.move,
            LEFT_TURN_INSTRUCTION: self.__mower.turn_left,
            RIGHT_TURN_INSTRUCTION: self.__mower.turn_right
        }

        for instruction in self.__instructions_split_from(instructions_string):
            instruction_to_command_map[instruction]()

        return self.__format_position()

    @staticmethod
    def __instructions_split_from(instructions_string):
        return list(instructions_string)

    def __format_position(self):
        return POSITION_FORMAT.format(
            x=self.__mower.x,
            y=self.__mower.y,
            orientation=self.__mower.orientation.name(),
        )

    @staticmethod
    def orientation_for(orientation_name: str):
        return {
            North.NORTH_ORIENTATION: North(),
            South.SOUTH_ORIENTATION: South(),
            East.EAST_ORIENTATION: East(),
            West.WEST_ORIENTATION: West(),
        }[orientation_name]
