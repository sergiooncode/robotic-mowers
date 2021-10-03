from src.robotic_mower import RoboticMower


def test_return_position_when_empty_instructions_received():
    initial_x = 1
    initial_y = 2
    initial_orientation = "N"
    empty_instructions = ""
    current_position = RoboticMower(
        x=initial_x, y=initial_y, orientation=initial_orientation
    ).execute(instructions=empty_instructions)

    assert "1 2 N" == current_position
