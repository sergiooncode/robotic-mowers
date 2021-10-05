from src.factory_map import FactoryMap
from src.mower_situation import MowerSituation
from src.orientation.east import East
from src.orientation.north import North
from src.orientation.south import South
from src.orientation.west import West
from src.position import Position
from src.robotic_mower_controller import MOVE_INSTRUCTION, RoboticMowerController, LEFT_TURN_INSTRUCTION, \
    RIGHT_TURN_INSTRUCTION


def test_return_position_when_empty_instructions_received():
    initial_x = 1
    initial_y = 2
    empty_instructions = ""

    expected_position = "1 2 N"

    current_position = RoboticMowerController(
        factory_map=FactoryMap(
            mower_situation=MowerSituation(
                position=Position(x=initial_x, y=initial_y), orientation=North()
            )
        ),
    ).execute(instructions_string=empty_instructions)

    assert expected_position == current_position


def test_return_position_when_orientation_north_and_move_instruction_received():
    initial_x = 1
    initial_y = 2
    received_instructions = MOVE_INSTRUCTION

    expected_position = "1 3 N"

    current_position = RoboticMowerController(
        factory_map=FactoryMap(
            mower_situation=MowerSituation(
                position=Position(x=initial_x, y=initial_y), orientation=North()
            )
        ),
    ).execute(instructions_string=received_instructions)

    assert expected_position == current_position


def test_return_position_when_orientation_south_and_move_instruction_received():
    initial_x = 1
    initial_y = 2
    received_instructions = MOVE_INSTRUCTION

    expected_position = "1 1 S"

    current_position = RoboticMowerController(
        factory_map=FactoryMap(
            mower_situation=MowerSituation(
                position=Position(x=initial_x, y=initial_y), orientation=South()
            )
        ),
    ).execute(instructions_string=received_instructions)

    assert expected_position == current_position


def test_return_position_when_orientation_east_and_move_instruction_received():
    initial_x = 1
    initial_y = 2
    received_instructions = MOVE_INSTRUCTION

    expected_position = "2 2 E"

    current_position = RoboticMowerController(
        factory_map=FactoryMap(
            mower_situation=MowerSituation(
                position=Position(x=initial_x, y=initial_y), orientation=East()
            )
        ),
    ).execute(instructions_string=received_instructions)

    assert expected_position == current_position


def test_return_position_when_orientation_west_and_move_instruction_received():
    initial_x = 1
    initial_y = 2
    received_instructions = MOVE_INSTRUCTION

    expected_position = "0 2 W"

    current_position = RoboticMowerController(
        factory_map=FactoryMap(
            mower_situation=MowerSituation(
                position=Position(x=initial_x, y=initial_y), orientation=West()
            )
        ),
    ).execute(instructions_string=received_instructions)

    assert expected_position == current_position


def test_return_position_when_orientation_east_and_several_move_instruction_received():
    initial_x = 1
    initial_y = 2
    received_instructions = f"{MOVE_INSTRUCTION}{MOVE_INSTRUCTION}"

    expected_position = "3 2 E"

    current_position = RoboticMowerController(
        factory_map=FactoryMap(
            mower_situation=MowerSituation(
                position=Position(x=initial_x, y=initial_y), orientation=East()
            )
        ),
    ).execute(instructions_string=received_instructions)

    assert expected_position == current_position


def test_return_position_when_orientation_north_and_turn_left_instruction_received():
    initial_x = 1
    initial_y = 2
    received_instructions = LEFT_TURN_INSTRUCTION

    expected_position = "1 2 W"

    current_position = RoboticMowerController(
        factory_map=FactoryMap(
            mower_situation=MowerSituation(
                position=Position(x=initial_x, y=initial_y), orientation=North()
            )
        ),
    ).execute(instructions_string=received_instructions)

    assert expected_position == current_position


def test_return_position_when_orientation_north_and_turn_right_instruction_received():
    initial_x = 1
    initial_y = 2
    received_instructions = RIGHT_TURN_INSTRUCTION

    expected_position = "1 2 E"

    current_position = RoboticMowerController(
        factory_map=FactoryMap(
            mower_situation=MowerSituation(
                position=Position(x=initial_x, y=initial_y), orientation=North()
            )
        ),
    ).execute(instructions_string=received_instructions)

    assert expected_position == current_position


def test_return_position_when_orientation_south_and_turn_left_instruction_received():
    initial_x = 1
    initial_y = 2
    received_instructions = LEFT_TURN_INSTRUCTION

    expected_position = "1 2 E"

    current_position = RoboticMowerController(
        factory_map=FactoryMap(
            mower_situation=MowerSituation(
                position=Position(x=initial_x, y=initial_y), orientation=South()
            )
        ),
    ).execute(instructions_string=received_instructions)

    assert expected_position == current_position


def test_return_position_when_orientation_south_and_turn_right_instruction_received():
    initial_x = 1
    initial_y = 2
    received_instructions = RIGHT_TURN_INSTRUCTION

    expected_position = "1 2 W"

    current_position = RoboticMowerController(
        factory_map=FactoryMap(
            mower_situation=MowerSituation(
                position=Position(x=initial_x, y=initial_y), orientation=South()
            )
        ),
    ).execute(instructions_string=received_instructions)

    assert expected_position == current_position


def test_return_position_when_orientation_west_and_turn_left_instruction_received():
    initial_x = 1
    initial_y = 2
    received_instructions = LEFT_TURN_INSTRUCTION

    expected_position = "1 2 S"

    current_position = RoboticMowerController(
        factory_map=FactoryMap(
            mower_situation=MowerSituation(
                position=Position(x=initial_x, y=initial_y), orientation=West()
            )
        ),
    ).execute(instructions_string=received_instructions)

    assert expected_position == current_position


def test_return_position_when_orientation_west_and_turn_right_instruction_received():
    initial_x = 1
    initial_y = 2
    received_instructions = RIGHT_TURN_INSTRUCTION

    expected_position = "1 2 N"

    current_position = RoboticMowerController(
        factory_map=FactoryMap(
            mower_situation=MowerSituation(
                position=Position(x=initial_x, y=initial_y), orientation=West()
            )
        ),
    ).execute(instructions_string=received_instructions)

    assert expected_position == current_position


def test_return_position_when_orientation_east_and_turn_left_instruction_received():
    initial_x = 1
    initial_y = 2
    received_instructions = LEFT_TURN_INSTRUCTION

    expected_position = "1 2 N"

    current_position = RoboticMowerController(
        factory_map=FactoryMap(
            mower_situation=MowerSituation(
                position=Position(x=initial_x, y=initial_y), orientation=East()
            )
        ),
    ).execute(instructions_string=received_instructions)

    assert expected_position == current_position


def test_return_position_when_orientation_east_and_turn_right_instruction_received():
    initial_x = 1
    initial_y = 2
    received_instructions = RIGHT_TURN_INSTRUCTION

    expected_position = "1 2 S"

    current_position = RoboticMowerController(
        factory_map=FactoryMap(
            mower_situation=MowerSituation(
                position=Position(x=initial_x, y=initial_y), orientation=East()
            )
        ),
    ).execute(instructions_string=received_instructions)

    assert expected_position == current_position


def test_return_position_when_orientation_east_and_two_turn_right_instructions_received():
    initial_x = 1
    initial_y = 2
    received_instructions = f"{RIGHT_TURN_INSTRUCTION}{RIGHT_TURN_INSTRUCTION}"

    expected_position = "1 2 W"

    current_position = RoboticMowerController(
        factory_map=FactoryMap(
            mower_situation=MowerSituation(
                position=Position(x=initial_x, y=initial_y), orientation=East()
            )
        ),
    ).execute(instructions_string=received_instructions)

    assert expected_position == current_position


def test_provided_acceptance_tests():
    input = "5 5\n1 2 N\nLMLMLMLMM\n3 3 E\nMMRMMRMRRM"

    actual_output = []
    deployed_mowers_settings = input.split("\n")[1:]

    expected_output_string = "1 3 N\n5 1 E"

    for mower_group_index in range(len(deployed_mowers_settings) // 2):
        situation = deployed_mowers_settings[mower_group_index * 2].split(" ")
        instructions = deployed_mowers_settings[mower_group_index * 2 + 1]
        current_position = RoboticMowerController(
            factory_map=FactoryMap(
                mower_situation=MowerSituation(
                    position=Position(x=int(situation[0]), y=int(situation[1])),
                    orientation=RoboticMowerController.orientation_for(situation[2])
                )
            ),
        ).execute(instructions_string=instructions)
        print(current_position)
        actual_output.append(current_position)

    assert expected_output_string == "\n".join(actual_output)
