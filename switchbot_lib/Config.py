import configparser
import os
import json

class Config:
    def __init__(self) -> None:
        self.jsonfile = {}

    def read(self, path: str) -> dict:
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                self.jsonfile = json.load(f)
                return self.jsonfile
        else:
            raise RuntimeError("File not found.")

    def show_config(self) -> None:
        for value in self.jsonfile.values():
            print(value)

    def write(self, path: str, config: dict) -> None:
        with open(path, mode='w', encoding="utf-8") as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
