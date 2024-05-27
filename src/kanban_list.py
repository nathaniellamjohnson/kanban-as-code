from kanban_parser import *
from kanban_verify import parse_json_file
import json


def load_kanban_from_file(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)

    kanban = KanbanBoard()
    for column_name, cards in data.items():
        kanban.columns[column_name] = [KanbanCard(**card) for card in cards]

    return kanban


def list_kanban_in_terminal(file_path):
    try:
        list_board = parse_json_file(file_path)
        print(f"Board: {list_board.name}")
        for column_name, cards in list_board.columns.items():
            print(f"\n{column_name.capitalize()}:")
            for card in cards:
                print(f"\t{card['name']}\t{card['notes']}\t{', '.join(card['tags'])}")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(
            "\033[1;31;40m ERROR \033[0m Unable to list the Kanban board. Check validity using -v."
        )
        raise e


def main(file_path="./kanban.json"):
    list_kanban_in_terminal(file_path)


if __name__ == "__main__":
    main()
