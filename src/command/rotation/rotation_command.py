from abc import abstractmethod, ABC

from src.command.factory_command import FactoryCommand
from src.movement import Movement
from src.mower_situation import MowerSituation
from src.orientation.orientation import Orientation


class RotationCommand(FactoryCommand, ABC):
    def execute(self, situation: MowerSituation) -> MowerSituation:
        return situation.rotate(self)

    @abstractmethod
    def rotate(self, orientation: Orientation) -> Movement:
        pass
