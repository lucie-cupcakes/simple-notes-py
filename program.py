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
        print("Welcome to the Notes program!\n"
              "TIP: type help for the command list")
        while True:
            cmd = input("Notes>").lstrip().rstrip()
            self.__cmd = cmd
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
            elif cmd.startswith("exit"):
                break
            else:
                print("Command not found")
    def __read_until_finish(self) -> str:
        print("TIP: type @finish@ when you finish.")
        result = ""
        while not (line := input()).rstrip().startswith("@finish@"):
            result = f"{result}\n{line}"
        return result
    def __help_command(self):
        print("Commands:\n"
              "new-\tCreate a Note\n"
              "del-\tDelete a Note\n"
              "mod-\tModify a Note\n"
              "list-\tList Notes\n"
              "print-\tPrint a Note to the screen\n"
              "exit-\tLeave the program.")
    def __new_command(self):
        try:
            title = input("title: ")
            contents = self.__read_until_finish()
            note = Note(title, contents)
            note.save(self.__db_handle)
            self.__note_list.set(note.id, note.title)
            self.__note_list.save(self.__db_handle)
        except Exception as e:
            print(e)
    def __list_command(self):
        try:
            if len(self.__note_list.value) < 1:
                print("There are not saved notes.")
                return
            for note_id in self.__note_list.value:
                note_title = self.__note_list.value[note_id]
                print(f"{note_id}\t{note_title}")
        except Exception as e:
            print(e)
    def __print_command(self):
        try:
            cmd_arr = self.__cmd.split(" ")
            if len(cmd_arr) < 2:
                print("usage: print <id>")
                return
            note_id = cmd_arr[1]
            note = Note.load(note_id, self.__db_handle)
            print(note.to_string())
        except Exception as e:
            print(e)
    def __modify_command(self):
        try:
            cmd_arr = self.__cmd.split(" ")
            if len(cmd_arr) < 2:
                print("usage: mod <id>")
                return
            note_id = cmd_arr[1]
            if not self.__note_list.has(note_id):
                print("the note does not exists.")
                return
            note = Note.load(note_id, self.__db_handle)
            print(note.to_string())
            title = input("title: ")
            contents = self.__read_until_finish()
            note.modify(title, contents)
            note.save(self.__db_handle)
            self.__note_list.set(note.id, note.title)
            self.__note_list.save(self.__db_handle)
        except Exception as e:
            print(e)
    def __delete_command(self):
        try:
            cmd_arr = self.__cmd.split(" ")
            if len(cmd_arr) < 2:
                print("usage: del <id>")
                return
            note_id = cmd_arr[1]
            if not self.__note_list.has(note_id):
                print("the note does not exists.")
                return
            self.__db_handle.delete_entry(note_id)
            self.__note_list.delete(note_id)
            self.__note_list.save(self.__db_handle)
        except Exception as e:
            print(e)
if __name__ == "__main__":
    try:
        program = Program()
        program.run()
    except Exception as e:
        print(e)
