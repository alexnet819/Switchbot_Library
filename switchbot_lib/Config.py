import configparser
import os
import json

class Config:
    def __init__(self) -> None:
        self.jsonfile = json

    def Read(self, path:str = None) -> json:
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                self.jsonfile = json.load(f)
                return self.jsonfile
        else:
            raise RuntimeError("File not found.")

    def Show_Config(self):
         for value in self.jsonfile.values():
             print(value)
        
    def Write(self, path:str, config:str):
        with open(path, mode='w', encoding="utf-8") as f:
            json.dump(json.loads(config), f, indent=4, ensure_ascii=False)
