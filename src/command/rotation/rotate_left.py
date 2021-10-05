from src.command.rotation.rotation_command import RotationCommand
from src.movement import Movement
from src.orientation.orientation import Orientation


class RotateLeft(RotationCommand):
    def rotate(self, orientation: Orientation) -> Movement:
        return orientation.rotate_left()
