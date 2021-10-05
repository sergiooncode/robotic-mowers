from typing import Optional

from src.command.move.move_forward import MoveForward
from src.command.rotation.rotate_left import RotateLeft
from src.command.rotation.rotate_right import RotateRight
from src.factory_map import FactoryMap
from src.orientation.east import East
from src.orientation.north import North
from src.orientation.south import South
from src.orientation.west import West

MOVE_INSTRUCTION = "M"
LEFT_TURN_INSTRUCTION = "L"
RIGHT_TURN_INSTRUCTION = "R"


class RoboticMowerController:
    def __init__(self, factory_map: FactoryMap):
        self.__factory_map = factory_map

    def execute(self, instructions_string: str) -> Optional[str]:
        for instruction in self.__instructions_split_from(instructions_string):
            self.__factory_map.execute(self.__map_command_to_instruction()[instruction])

        return self.__factory_map.mower_situation.format_position()

    @staticmethod
    def __instructions_split_from(instructions_string):
        return list(instructions_string)

    @staticmethod
    def orientation_for(orientation_name: str):
        return {
            North.NORTH_ORIENTATION: North(),
            South.SOUTH_ORIENTATION: South(),
            East.EAST_ORIENTATION: East(),
            West.WEST_ORIENTATION: West(),
        }[orientation_name]

    @staticmethod
    def __map_command_to_instruction():
        return {
            MOVE_INSTRUCTION: MoveForward(),
            LEFT_TURN_INSTRUCTION: RotateLeft(),
            RIGHT_TURN_INSTRUCTION: RotateRight(),
        }
