
from switchbot_lib import Http_Client
import json

class Scene:
    def __init__(self, data: json, client: Http_Client = None):
        #self.client =
        self.http_client = client 
        self.id: str = data['sceneId']
        self.name: str = data['sceneName']
        
    def execute(self):
        self.http_client.send('POST', f"scenes/{self.id}/execute")

    def Create_Json(self) -> str:
        _json=f'{{"sceneId": "{self.id}", "sceneName": "{self.name}"}}'
        return _json  
