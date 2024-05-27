import pytest
import json
import sys

import kanban_parser
import kanban_as_code
from kanban_create_new import create_new_kanban
from kanban_list import main as kanban_list_main
from kanban_verify import verify_kanban_board


def test_kanban_as_code():
    # No tests needed for kanban_as_code
    assert True


def test_kanban_create_new():
    # Test case for kanban_create_new
    a = json.dumps(create_new_kanban().to_dict(), indent=4)
    with open("tests/test_json/kanban_create_new_valid.json") as file:
        b = file.read()
    assert a == b


def test_kanban_list(capsys):
    # Test case for kanban_list
    kanban_list_main("tests/test_json/kanban_list_test.json")

    captured = capsys.readouterr()

    with open("tests/test_json/kanban_list_test_output.txt") as file:
        valid_output = file.read()

    assert captured.out == valid_output


def test_kanban_verify():
    # Test case for kanban_verify
    input1 = verify_kanban_board("tests/test_json/kanban_verify_parse_invalid.json")
    input1_expected_output = False
    input2 = verify_kanban_board("tests/test_json/kanban_verify_parse_valid.json")
    input2_expected_output = True

    assert input1 == input1_expected_output
    assert input2 == input2_expected_output
