from dataclasses import dataclass


@dataclass(frozen=True)
class Movement:
    horizontal_movement: int
    vertical_movement: int
