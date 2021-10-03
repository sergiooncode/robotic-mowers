from src.robotic_mower import RoboticMower
from src.robotic_mower_controller import MOVE_INSTRUCTION, RoboticMowerController


def test_return_position_when_empty_instructions_received():
    initial_x = 1
    initial_y = 2
    initial_orientation = "N"
    empty_instructions = ""

    expected_position = "1 2 N"

    current_position = RoboticMowerController(
        mower=RoboticMower(x=initial_x, y=initial_y, orientation=initial_orientation)
    ).execute(instructions_string=empty_instructions)

    assert expected_position == current_position


def test_return_position_when_orientation_north_and_move_instruction_received():
    initial_x = 1
    initial_y = 2
    initial_orientation = "N"
    received_instructions = MOVE_INSTRUCTION

    expected_position = "1 3 N"

    current_position = RoboticMowerController(
        mower=RoboticMower(x=initial_x, y=initial_y, orientation=initial_orientation)
    ).execute(instructions_string=received_instructions)

    assert expected_position == current_position


def test_return_position_when_orientation_south_and_move_instruction_received():
    initial_x = 1
    initial_y = 2
    initial_orientation = "S"
    received_instructions = MOVE_INSTRUCTION

    expected_position = "1 1 S"

    current_position = RoboticMowerController(
        mower=RoboticMower(x=initial_x, y=initial_y, orientation=initial_orientation)
    ).execute(instructions_string=received_instructions)

    assert expected_position == current_position


def test_return_position_when_orientation_east_and_move_instruction_received():
    initial_x = 1
    initial_y = 2
    initial_orientation = "E"
    received_instructions = MOVE_INSTRUCTION

    expected_position = "2 2 E"

    current_position = RoboticMowerController(
        mower=RoboticMower(x=initial_x, y=initial_y, orientation=initial_orientation)
    ).execute(instructions_string=received_instructions)

    assert expected_position == current_position


def test_return_position_when_orientation_west_and_move_instruction_received():
    initial_x = 1
    initial_y = 2
    initial_orientation = "W"
    received_instructions = MOVE_INSTRUCTION

    expected_position = "0 2 W"

    current_position = RoboticMowerController(
        mower=RoboticMower(x=initial_x, y=initial_y, orientation=initial_orientation)
    ).execute(instructions_string=received_instructions)

    assert expected_position == current_position


def test_return_position_when_orientation_east_and_several_move_instruction_received():
    initial_x = 1
    initial_y = 2
    initial_orientation = "E"
    received_instructions = f"{MOVE_INSTRUCTION}{MOVE_INSTRUCTION}"

    expected_position = "3 2 E"

    current_position = RoboticMowerController(
        mower=RoboticMower(x=initial_x, y=initial_y, orientation=initial_orientation)
    ).execute(instructions_string=received_instructions)

    assert expected_position == current_position


def test_return_position_when_orientation_north_and_turn_left_instruction_received():
    initial_x = 1
    initial_y = 2
    initial_orientation = "N"
    received_instructions = "L"

    expected_position = "1 2 W"

    current_position = RoboticMowerController(
        mower=RoboticMower(x=initial_x, y=initial_y, orientation=initial_orientation)
    ).execute(instructions_string=received_instructions)

    assert expected_position == current_position


def test_return_position_when_orientation_north_and_turn_right_instruction_received():
    initial_x = 1
    initial_y = 2
    initial_orientation = "N"
    received_instructions = "R"

    expected_position = "1 2 E"

    current_position = RoboticMowerController(
        mower=RoboticMower(x=initial_x, y=initial_y, orientation=initial_orientation)
    ).execute(instructions_string=received_instructions)

    assert expected_position == current_position


def test_return_position_when_orientation_south_and_turn_left_instruction_received():
    initial_x = 1
    initial_y = 2
    initial_orientation = "S"
    received_instructions = "L"

    expected_position = "1 2 E"

    current_position = RoboticMowerController(
        mower=RoboticMower(x=initial_x, y=initial_y, orientation=initial_orientation)
    ).execute(instructions_string=received_instructions)

    assert expected_position == current_position


def test_return_position_when_orientation_south_and_turn_right_instruction_received():
    initial_x = 1
    initial_y = 2
    initial_orientation = "S"
    received_instructions = "R"

    expected_position = "1 2 W"

    current_position = RoboticMowerController(
        mower=RoboticMower(x=initial_x, y=initial_y, orientation=initial_orientation)
    ).execute(instructions_string=received_instructions)

    assert expected_position == current_position


def test_return_position_when_orientation_west_and_turn_left_instruction_received():
    initial_x = 1
    initial_y = 2
    initial_orientation = "W"
    received_instructions = "L"

    expected_position = "1 2 S"

    current_position = RoboticMowerController(
        mower=RoboticMower(x=initial_x, y=initial_y, orientation=initial_orientation)
    ).execute(instructions_string=received_instructions)

    assert expected_position == current_position


def test_return_position_when_orientation_west_and_turn_right_instruction_received():
    initial_x = 1
    initial_y = 2
    initial_orientation = "W"
    received_instructions = "R"

    expected_position = "1 2 N"

    current_position = RoboticMowerController(
        mower=RoboticMower(x=initial_x, y=initial_y, orientation=initial_orientation)
    ).execute(instructions_string=received_instructions)

    assert expected_position == current_position


def test_return_position_when_orientation_east_and_turn_left_instruction_received():
    initial_x = 1
    initial_y = 2
    initial_orientation = "E"
    received_instructions = "L"

    expected_position = "1 2 N"

    current_position = RoboticMowerController(
        mower=RoboticMower(x=initial_x, y=initial_y, orientation=initial_orientation)
    ).execute(instructions_string=received_instructions)

    assert expected_position == current_position


def test_return_position_when_orientation_east_and_turn_right_instruction_received():
    initial_x = 1
    initial_y = 2
    initial_orientation = "E"
    received_instructions = "R"

    expected_position = "1 2 S"

    current_position = RoboticMowerController(
        mower=RoboticMower(x=initial_x, y=initial_y, orientation=initial_orientation)
    ).execute(instructions_string=received_instructions)

    assert expected_position == current_position


def test_return_position_when_orientation_east_and_turn_right_instruction_received():
    initial_x = 1
    initial_y = 2
    initial_orientation = "E"
    received_instructions = "R"

    expected_position = "1 2 S"

    current_position = RoboticMowerController(
        mower=RoboticMower(x=initial_x, y=initial_y, orientation=initial_orientation)
    ).execute(instructions_string=received_instructions)

    assert expected_position == current_position


def test_return_position_when_orientation_east_and_two_turn_right_instructions_received():
    initial_x = 1
    initial_y = 2
    initial_orientation = "E"
    received_instructions = "RR"

    expected_position = "1 2 W"

    current_position = RoboticMowerController(
        mower=RoboticMower(x=initial_x, y=initial_y, orientation=initial_orientation)
    ).execute(instructions_string=received_instructions)

    assert expected_position == current_position
