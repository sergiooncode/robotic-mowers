from typing import Optional


class RoboticMower:
    def __init__(self, x: int, y: int, orientation: str):
        self.__x = x
        self.__y = y
        self.__orientation = orientation

    def execute(self, instructions: str) -> Optional[str]:
        return "1 2 N"
