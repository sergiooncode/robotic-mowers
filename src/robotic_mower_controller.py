from typing import Optional

from src.robotic_mower import RoboticMower

MOVE_INSTRUCTION = "M"
LEFT_TURN_INSTRUCTION = "L"
RIGHT_TURN_INSTRUCTION = "R"
POSITION_FORMAT = "{x} {y} {orientation}"


class RoboticMowerController:
    def __init__(self, mower: RoboticMower):
        self.__mower = mower

    def execute(self, instructions_string: str) -> Optional[str]:
        for instruction in self.__instructions_split_from(instructions_string):
            if self.__is_move(instruction):
                self.__mower.move()
            if self.__is_left_turn(instruction):
                self.__mower.turn_left()
            if self.__is_right_turn(instruction):
                self.__mower.turn_right()
        return self.__format_position()

    @staticmethod
    def __instructions_split_from(instructions_string):
        return list(instructions_string)

    def __format_position(self):
        return POSITION_FORMAT.format(
            x=self.__mower.x,
            y=self.__mower.y,
            orientation=self.__mower.orientation,
        )

    @staticmethod
    def __is_move(instruction):
        return instruction == MOVE_INSTRUCTION

    @staticmethod
    def __is_left_turn(instruction):
        return instruction == LEFT_TURN_INSTRUCTION

    @staticmethod
    def __is_right_turn(instruction):
        return instruction == RIGHT_TURN_INSTRUCTION
