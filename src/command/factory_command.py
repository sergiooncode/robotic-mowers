from abc import abstractmethod, ABC

from src.mower_situation import MowerSituation


class FactoryCommand(ABC):
    @abstractmethod
    def execute(self, situation: MowerSituation) -> MowerSituation:
        pass
