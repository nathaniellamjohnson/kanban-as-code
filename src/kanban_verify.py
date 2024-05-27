import json
from kanban_parser import KanbanBoard


def parse_json_file(file_path):
    with open(file_path, "r") as file:
        a = json.load(file)
        b = KanbanBoard(json_dict=a)
        return b


def verify_kanban_board(file_path):
    try:
        verify_board = parse_json_file(file_path)
        if not isinstance(verify_board, KanbanBoard):
            return (
                False,
                "Error in creating KanbanBoard. Check that this is a valid JSON.",
            )
        if not verify_board.name:
            return (False, "Error in creating KanbanBoard. Check that a name exists.")
        if not verify_board.columns:
            return (False, "Error in creating KanbanBoard. Check that columns exist.")
        if not all(
            name in ["todo", "inprogress", "review", "done"]
            for name in verify_board.columns
        ):
            return (
                False,
                "Error in creating KanbanBoard. Check that only 'todo', 'inprogress', 'review', 'done' columns exist.",
            )
        return True
    except (FileNotFoundError, json.JSONDecodeError):
        return False


def main(file_path):
    is_valid = verify_kanban_board(file_path)
    if is_valid:
        print("\033[1;32;40m VALID \033[0m The JSON file is a valid KanbanBoard.")
        return
    else:
        print("\033[1;31;40m ERROR \033[0m The JSON file is not a valid KanbanBoard.")
        raise Exception("Invalid KanbanBoard.")


if __name__ == "__main__":
    main()
