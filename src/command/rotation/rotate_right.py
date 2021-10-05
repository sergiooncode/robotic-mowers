from src.command.rotation.rotation_command import RotationCommand
from src.movement import Movement
from src.orientation.orientation import Orientation


class RotateRight(RotationCommand):
    def rotate(self, orientation: Orientation) -> Movement:
        return orientation.rotate_right()
