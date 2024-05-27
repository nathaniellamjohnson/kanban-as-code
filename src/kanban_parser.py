import json
from typing import List


def parse_json(json_str):
    return json.loads(json_str)


def parse_json_file(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


class KanbanCard:
    def __init__(
        self,
        name="Placeholder Name",
        notes="Placeholder Notes",
        tags=None,
        json_str=None,
    ):
        if json_str:
            data = parse_json(json_str)
            self.name = data["name"]
            self.notes = data["notes"]
            self.tags = data["tags"]
        else:
            self.name = name
            self.notes = notes
            self.tags = tags if tags else []

    def to_dict(self):
        return {
            "name": self.name,
            "notes": self.notes,
            "tags": self.tags,
        }

    def to_dict(self):
        return {
            "name": self.name,
            "notes": self.notes,
            "tags": self.tags,
        }


class KanbanBoard:
    def __init__(self, json_dict=None):
        if json_dict:
            self.name = json_dict["name"]
            self.columns = json_dict["columns"]
        else:
            self.name = "My First Kanban-As-Code Board"
            self.columns = {"todo": [], "inprogress": [], "review": [], "done": []}

    def to_dict(self):
        a = {
            column_name: [card.to_dict() for card in cards]
            for column_name, cards in self.columns.items()
        }
        b = {}
        b["name"] = self.name
        b["columns"] = a
        return b
