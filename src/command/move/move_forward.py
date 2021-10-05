from src.command.factory_command import FactoryCommand
from src.command.move.movement_command import MovementCommand
from src.movement import Movement
from src.mower_situation import MowerSituation
from src.orientation.orientation import Orientation


class MoveForward(FactoryCommand, MovementCommand):
    def execute(self, situation: MowerSituation) -> MowerSituation:
        return situation.move_forward(self)

    def move(self, orientation: Orientation) -> Movement:
        return orientation.movement()
