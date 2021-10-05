from src.command.factory_command import FactoryCommand
from src.mower_situation import MowerSituation


class FactoryMap:
    def __init__(self, mower_situation: MowerSituation):
        self.__mower_situation = mower_situation

    def execute(self, command: FactoryCommand):
        self.__mower_situation = command.execute(self.__mower_situation)

    @property
    def mower_situation(self):
        return self.__mower_situation
