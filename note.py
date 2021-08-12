from uuid import uuid4
from datetime import datetime

class Note:
    def __init__(self, title : str, contents : str):
        self.id = uuid4()
        self.title = title
        self.contents = contents
        self.creation_time = datetime.utcnow()
        self.last_modified = self.creation_time
    def modify(self, title : str, contents : str):
        self.title = title
        self.contents = contents
        self.last_modified = datetime.utcnow()
    def to_string(self) -> str:
        res = f"title: {self.title}\nCreation time: {self.creation_time}"
        f"\nModification time: {self.last_modified}\n{self.contents}"
        return res

