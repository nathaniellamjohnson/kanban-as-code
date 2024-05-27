from kanban_parser import *
from pathlib import Path
import json


def create_new_kanban():
    kanban = KanbanBoard()
    for column, list in kanban.columns.items():
        list.append(KanbanCard("Dummy Card", "New Notes", ["New Tag"]))
    return kanban


def save(kanban, file_path):
    kanban_dict = kanban.to_dict()  # Convert the object to a dictionary
    kanban_str = json.dumps(kanban_dict, indent=4)  # Serialize the dictionary
    try:
        Path(file_path).write_text(kanban_str)
    except FileExistsError:
        print(f"Error: File '{file_path}' already exists.")


def main(file_path="./kanban.json"):
    kanban = create_new_kanban()
    save(kanban, file_path)


if __name__ == "__main__":
    main()
