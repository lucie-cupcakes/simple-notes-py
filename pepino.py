import requests
class PepinoDB:
    def __init__(self, url: str, db_name: str, password: str):
       self.__url = url
       self.__db_name = db_name
       self.__password = password
    def __build_url_for_entry(self, entry_name: str) -> str:
        params = self.__url + "/?password=" + self.__password
        params += "&db=" + self.__db_name + "&entry=" + entry_name
        return params
    def get_entry(self, entry_name : str) -> bytes:
        res = requests.get(self.__build_url_for_entry(entry_name))
        if res.status_code != 200:
            msg = res.content.decode("utf-8")
            raise Exception("HTTP error " + str(res.status_code) + ":\n" + msg)
        return res.content
    def save_entry(self, entry_name : str, entry_value : bytes):
        res = requests.post(self.__build_url_for_entry(entry_name), entry_value)
        if res.status_code != 200:
            msg = res.content.decode("utf-8")
            raise Exception("HTTP error " + str(res.status_code) + ":\n" + msg)
    def delete_entry(self, entry_name : str):
        res = requests.delete(self.__build_url_for_entry(entry_name))
        if res.status_code != 200:
            msg = res.content.decode("utf-8")
            raise Exception("HTTP error " + str(res.status_code) + ":\n" + msg)
