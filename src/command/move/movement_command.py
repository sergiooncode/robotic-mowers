from abc import ABC, abstractmethod

from src.movement import Movement
from src.orientation.orientation import Orientation


class MovementCommand(ABC):
    @abstractmethod
    def move(self, orientation: Orientation) -> Movement:
        pass
