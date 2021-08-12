from pepino import PepinoDB
from note import Note
from notelist import NoteList
class Program:
    def __init__(self):
        self.__db_handle = PepinoDB("http://localhost:50200", "NotesPy", "caipiroska")
        try:
            self.__note_list = NoteList.load(self.__db_handle)
        except:
            self.__note_list = NoteList()
    def run(self):
        cmd = input("Notes>")
        if cmd.startswith("new"):
            self.__new_command()
        elif cmd.startswith("list"):
            self.__list_command()
        elif cmd.startswith("mod"):
            self.__modify_command()
        elif cmd.startswith("del"):
            self.__delete_command()
        elif cmd.startswith("print"):
            self.__print_command()
        elif cmd.startswith("help"):
            self.__help_command()
        else:
            print("Command not found")
    def __read_until_finish(self) -> str:
        result = ""
        while not (line := input()).rstrip().startswith("@finish@"):
            result = f"{result}\n{line}"
    def __help_command(self):

    def __new_command(self):
        try:
            title = input("title: ")
            contents = self.__read_until_finish()
            note = Note(title, contents)
            note.save(self.__db_handle)
            self.__note_list.put(note.id, note.title)
            self.__note_list.save(self.__db_handle)
        except Exception as e:
            print(e)
