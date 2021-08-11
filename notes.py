from pepino import PepinoDB

db = PepinoDB("http://localhost:50200", "NotesPy", "caipiroska")
db.save_entry("Yes", str.encode("Yes, this is data", "utf-8"))
print(db.get_entry("Yes").decode("utf-8"))
