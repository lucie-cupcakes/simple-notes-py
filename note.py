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
        data = json_loads(json_data)
        note = Note(data.title, data.contents)
        note.id = data.id
        note.creation_time = data.creation_time
        note.last_modified = data.last_modified
        return note
    def modify(self, title : str, contents : str):
        self.title = title
        self.contents = contents
        self.last_modified = datetime.utcnow()
    def to_string(self) -> str:
        res = f"title: {self.title}\nCreation time: {self.creation_time}"
        f"\nModification time: {self.last_modified}\n{self.contents}"
        return res
    def save(self, db_handler : PepinoDB):
        note_bytes = json_dumps(self).encode("utf-8")
        db_handler.save_entry(self.id, note_bytes)
    @staticmethod
    def load(note_id : str, db_handler : PepinoDB):
        note_json = db_handler.get_entry(note_id).decode("utf-8")
        return Note.from_json(note_json)
