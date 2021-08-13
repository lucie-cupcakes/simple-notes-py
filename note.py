from typing import Dict
from uuid import uuid4
from datetime import datetime
from pepino import PepinoDB
from json import dumps as json_dumps
from json import loads as json_loads
class Note:
    def __init__(self, title : str, contents : str):
        self.id = str(uuid4())
        self.title = title
        self.contents = contents
        self.creation_time = datetime.utcnow()
        self.last_modified = self.creation_time
    @staticmethod
    def from_json(json_data : str):
        dtfmt = "%Y-%m-%dT%H:%M:%S.%f"
        data = json_loads(json_data)
        note = Note(data["title"], data["contents"])
        note.id = data["id"]
        note.creation_time = datetime.strptime(data["creation_time"], dtfmt)
        note.last_modified = datetime.strptime(data["last_modified"], dtfmt)
        return note
    def to_json(self) -> str:
        dtfmt = "%Y-%m-%dT%H:%M:%S.%f"
        data : Dict[str, str] = {}
        data["id"] = self.id
        data["title"] = self.title
        data["contents"] = self.contents
        data["creation_time"] = self.creation_time.strftime(dtfmt)
        data["last_modified"] = self.last_modified.strftime(dtfmt)
        return json_dumps(data)
    def modify(self, title : str, contents : str):
        self.title = title
        self.contents = contents
        self.last_modified = datetime.utcnow()
    def to_string(self) -> str:
        dtfmt = "%Y-%m-%dT%H:%M:%S.%f"
        creation_time_str = self.creation_time.strftime(dtfmt)
        last_modified_str = self.last_modified.strftime(dtfmt)
        s = f"title: {self.title}\nCreation time: {creation_time_str}"
        s = f"{s}\nModification time: {last_modified_str}\n{self.contents}"
        return s
    def save(self, db_handler : PepinoDB):
        json_bytes = self.to_json().encode("utf-8")
        db_handler.save_entry(self.id, json_bytes)
    @staticmethod
    def load(note_id : str, db_handler : PepinoDB):
        note_json = db_handler.get_entry(note_id).decode("utf-8")
        return Note.from_json(note_json)
