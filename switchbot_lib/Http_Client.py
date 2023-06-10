import time
import hashlib
import hmac
import base64
import uuid
import requests
import json

API_HOST_URL = 'https://api.switch-bot.com/v1.1/'

class Http_Client:

    def __init__(self) -> None:
        pass

    def __init__(self, token:str, secret:str) -> None:
        self.session: requests.Session = requests.Session()
        nonce = uuid.uuid4()
        t = int(round(time.time() * 1000))
        string_to_sign = '{}{}{}'.format(token, t, nonce)

        string_to_sign = bytes(string_to_sign, 'utf-8')
        secret = bytes(secret, 'utf-8')

        sign = base64.b64encode(hmac.new(secret, msg=string_to_sign, digestmod=hashlib.sha256).digest())

        self.session.headers['Authorization']=token
        self.session.headers['Content-Type']='application/json'
        self.session.headers['charset']='utf8'
        self.session.headers['t']=str(t)
        self.session.headers['sign']=str(sign, 'utf-8')
        self.session.headers['nonce']=str(nonce)
    
    def send(self, method:str, path:str, command:json = None) -> json:
        if command == None:
            url: str = API_HOST_URL + path
            response = self.session.request(method, url)
            if response.status_code != 200:
                raise RuntimeError("http returns status " + response.status_code)
            elif response.status_code == 200 :
                return response.json()
            
        if command != None:
            url: str = API_HOST_URL + path
            response = self.session.request(method, url, json=command)
            if response.status_code != 200:
                raise RuntimeError("http returns status " + response.status_code)
            elif response.status_code == 200 :
                return response.json()
    
