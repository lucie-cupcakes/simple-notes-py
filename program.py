from pepino import PepinoDB
class Program:
    def __init__(self):
        self.__db_handle = PepinoDB("http://localhost:50200", "NotesPy", "caipiroska")
    def run(self):
        print("Run program")

