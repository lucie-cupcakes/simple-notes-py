from pepino import PepinoDB
from json import dumps as json_dumps
from json import loads as json_loads

class NoteList:
    def __init__(self):
        self.value = {}
    def set(self, key : str, value : str):
        self.value[key] = value
    def has(self, key : str) -> bool:
        if key in self.value.keys():
            return True
        else:
            return False
    def get(self, key : str) -> str:
        if not self.has(key):
            raise Exception("key does not exists")
        return self.value[key]
    def delete(self, key : str):
        if not self.has(key):
            raise Exception("key does not exists")
        del self.value[key]
    def save(self, db_handle : PepinoDB):
        value_bytes = json_dumps(self.value).encode("utf-8")
        db_handle.save_entry("List", value_bytes)
    @staticmethod
    def load(db_handle : PepinoDB):
        inst = NoteList()
        json_bytes = db_handle.get_entry("List")
        inst.value = json_loads(json_bytes.decode("utf-8"))
        return inst

