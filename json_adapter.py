import json
import os


class JSONAdapter:
    def __init__(self, path):
       self.__path = path

    def from_json(self):
        if os.path.exists(self.__path) is True:
            with open(self.__path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data
        else:
            data = []
            return data

    def to_json(self, my_list):
        data = self.from_json()

        for i in my_list:
            data.append(i)

        with open(self.__path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            print("Data saved")
