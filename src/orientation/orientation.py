from abc import abstractmethod, ABC


class Orientation(ABC):
    @abstractmethod
    def rotate_left(self):
        pass

    @abstractmethod
    def rotate_right(self):
        pass

    @abstractmethod
    def name(self):
        pass
