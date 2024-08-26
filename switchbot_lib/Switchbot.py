from switchbot_lib import Http_Client
from switchbot_lib import Config
from switchbot_lib import Device
from switchbot_lib import Scene
import os
import json

class Switchbot:
    def __init__(self, token:str = None, secret:str = None) -> None:
        self.__client = Http_Client
        self.__config = json
        self.Devices = []
        self.RemoteDevices = []
        self.Scenes = []
        self.token = ""
        self.secret = ""
        self.config_path = ""

        self.commands = open("./switchbot_lib/command.json",'r', encoding="utf-8")
        self.commands = json.load(self.commands) 
        if token != None and secret != None:
            self.token = token
            self.secret = secret
            self.__client = Http_Client.Http_Client(token, secret)

    def __set_Config(self):
        try:
            if "API_Key" in self.__config and "token" in self.__config['API_Key'] and "secret" in self.__config['API_Key']:
                self.token = self.__config['API_Key']['token']
                self.secret = self.__config['API_Key']['secret']
                self.__client = Http_Client.Http_Client(self.token, self.secret)
            if "deviceList" in self.__config:
                for dev in self.__config['deviceList']:
                    self.Devices.append(Device.Device(dev, self.__client))
                #print(dev['deviceId'])
            if "infraredRemoteList" in self.__config:
                for remote in self.__config['infraredRemoteList']:
                    self.RemoteDevices.append(Device.Remote_Device(remote, self.__client))
            if "senceList" in self.__config:
                for scene in self.__config['senceList']:
                    self.Scenes.append(Scene.Scene(scene, self.__client))
        except TypeError as e:
            print('data not found')



# Config Method
  
    def Load_Config(self, path:str) -> bool:
        self.config_path = path
        file = Config.Config()
        #self.__config = Config.Config()
        self.__config = file.read(self.config_path)
        self.__set_Config()
        return True
   
    def Show_Config(self):
        print(self.__config)

    def Show_Commands(self):
        print(self.commands)

    def Save_Config(self, path:str = None):
        if path == None:
            path = self.config_path 
        _conf = Config.Config()
        data = f'{{"API_Key":{{\n"token": "{self.token}",\n"secret": "{self.secret}"}},\n'
        data += f'"deviceList": [\n'
        count = 0
        for device in self.Devices:
            if count != 0:
                data += ",\n"
                
            data += device.Create_Json()
            count += 1
        data += f'],\n"infraredRemoteList": [\n'
        count = 0
        for remote in self.RemoteDevices:
            if count != 0:
                data += ",\n"
            data += remote.Create_Json()
            count += 1
        data += f'],\n"senceList": [\n'
        count = 0
        for scene in self.Scenes:
            if count != 0:
                data += ",\n"
            data += scene.Create_Json()
            count += 1
        data += f'\n]\n}}'
        #ファイル書き出し
        _conf.write(path, data)


    def __set_Device_Config(self, value):
        if self.__is_type(value) == 'Device':
            self.__config.set_Device(value)
        elif self.__is_type(value) == 'Sence':
            self.Scenes.append(value) 

    def __is_type(self, obj) -> str:
        if type(obj) is Device.Device:
            return 'Device'
        elif type(obj) is Scene.Scene:
            return 'Sence'
        elif obj.__base is Device.Device:
            return 'Device'
# Device Method

    def get_Device(self, devid:str) -> Device:
        for device in self.Devices:
            if device.get_DeviceID() == devid:
                return device    

       
    def get_Devices_from_Server(self):
        data = self.__client.send('GET', 'devices')
        if self.Check_StatusCode(data['statusCode']) == False:
            raise RuntimeError(f'An error occurred: {data["message"]}')
        for d in data['body']['deviceList']:
            self.Devices.append(Device.Device(d))
        for d in data['body']['infraredRemoteList']:
            self.RemoteDevices.append(Device.Remote_Device(d))
    def get_Devices_from_Config(self) -> json:
        return self.__config['deviceList']

    def Check_StatusCode(self, code) -> bool:
        if code == 100:
            return True
        else:
            return False

    def get_Remotes_from_Config(self) -> json:
        return self.__config['infraredRemoteList']

    def get_Remote(self, devid:str) -> Device.Remote_Device:
        for remote in self.RemoteDevices:
            if remote.get_DeviceID() == devid:
                return remote    



# Sence Method

    def get_Sense(self, devid:str) -> Scene:
        for sense in self.Scenes:
            if sense.id == devid:
                return sense
  
    def get_Scenes_from_Server(self):
        data = self.__client.send('GET', 'scenes')
        if self.Check_StatusCode(data['statusCode']) == False:
            raise RuntimeError(f'An error occurred: {data["message"]}')
        for d in data['body']:
            self.Scenes.append(Scene.Scene(d))
      
    def get_Scenes_from_Config(self) -> json:
        return self.__config['senceList']

    def Create_Curtain_setPosition(self, mode, position) -> json:
        command = self.commands['Curtain']['setPosition']
        if mode ==0 or mode == 1:
            if 0 <= position or position <= 100:
                command['parameter'] = f'{mode},ff,{position}'
                return command
            else:
                raise RuntimeError("The value of the argument (position) is wrong.")
        else:
            raise RuntimeError("The value of the argument (mode) is wrong.")


    def Create_setMode(self, param) -> json:
        command = self.commands['Humidifier']['setMode']
        if 0 <= param and param <= 103:
            command['parameter'] = param
            return command
        else:
            raise RuntimeError("The value of the argument (param) is wrong.")
        
    def Create_setBrightness(self, param) -> json:
        command = self.commands['Color Bulb']['setBrightness']
        if 0 <= param and param <= 100:
            command['parameter'] = param
            return command
        else:
            raise RuntimeError("The value of the argument (param) is wrong.")
    def Create_setColor(self, red, blue, green) -> json:
        command = self.commands['Strip Light']['setColor']
        if 0 <= red and red <= 255:
                if 0 <= blue and blue <= 255:
                    if 0 <= green and green <= 255:
                        command['parameter'] = f'{red},{blue},{green}'
                        return command
                    else:
                        raise RuntimeError("The value of the argument (green) is wrong.")
                else:
                    raise RuntimeError("The value of the argument (blue) is wrong.")
        else:
            raise RuntimeError("The value of the argument (red) is wrong.")
    def Create_setColorTemperature(self, param) -> json:
        command = self.commands['Color Bulb']['setColorTemperature']
        if 2700 <= param and param <= 6500:
            command['parameter'] = param
            return command
        else:
            raise RuntimeError("The value of the argument (param) is wrong.")
        
    def Create_PowLevel(self, param) -> json:
        command = self.commands['Robot Vacuum Cleaner S1']['PowLevel']
        if 0 <= param and param <= 3:
            command['parameter'] = param
            return command
        else:
            raise RuntimeError("The value of the argument (param) is wrong.")
        
    def Create_createKey(self, name, type, password, startTime, endTime) -> json:
        command = self.commands['Keypad']['createKey'] 
        command['parameter']['name'] = name
        command['parameter']['type'] = type
        command['parameter']['password'] = password
        command['parameter']['startTime'] = startTime
        command['parameter']['endTime'] =endTime

        return command
    def Create_deleteKey(self, param) -> json:
        command = self.commands['Keypad']['deleteKey'] 
        command['parameter']['id'] = param
        return command

    def Create_BlindTilt_setPosition(self, mode, position) -> json:
        command = self.commands['Blind Tilt']['setPosition'] 
        if mode =="up" or mode == "down":
            if 0 <= position or position <= 100:
                command['parameter'] = f'{mode},ff,{position}'
                return command
            else:
                raise RuntimeError("The value of the argument (position) is wrong.")
        else:
            raise RuntimeError("The value of the argument (mode) is wrong.")

    def Create_AirConditioner_setAll(self, temp, mode, fanspd, power) -> json:
        command = self.commands['Air Conditioner']['setAll'] 
        if 1 <= mode and mode <= 5:
            if 1 <= fanspd and power <= 4:
                if power =="on" or power == "down":
                    command['parameter'] = f'{temp},{mode},{fanspd},{power}'
                    return command
                else:
                    raise RuntimeError("The value of the argument (mode) must be entered as 1 (auto), 2 (low), 3 (medium), or 4 (high).")
            else:
                raise RuntimeError("The value of the argument (mode) must be entered on or off.")
        else:
            raise RuntimeError("The value of the argument (mode) must be 1 (auto), 2 (cool), 3 (dry), 4 (fan), or 5 (heat).")  
    def Create_SetChannel(self, param) -> json:
        command = self.commands['TV/IPTV/Streamer/Set Top Box"']['SetChannel']
        command['parameter'] = param
        return command

import json
from .Config import Config
from .Http_Client import Http_Client
from .Device import Device
from .Scene import Scene

class Switchbot:
	def __init__(self, token: str = None, secret: str = None) -> None:
		self.__client = None
		self.__config = {}
		self.devices = []
		self.remote_devices = []
		self.scenes = []
		self.token = token or ""
		self.secret = secret or ""
		self.config_path = ""

		self.load_commands()
		if token and secret:
			self.__client = Http_Client(token, secret)

	def load_commands(self) -> None:
		with open("./switchbot_lib/command.json", 'r', encoding="utf-8") as f:
			self.commands = json.load(f)

	def load_config(self, path: str) -> bool:
		config = Config()
		self.__config = config.read(path)
		self.__set_config()
		return True

	def show_config(self) -> None:
		print(self.__config)

	def show_commands(self) -> None:
		print(self.commands)

	def save_config(self, path: str = None) -> None:
		if not path:
			path = self.config_path
		config = Config()
		data = {
			"API_Key": {
				"token": self.token,
				"secret": self.secret
			},
			"deviceList": [device.create_json() for device in self.devices],
			"infraredRemoteList": [remote.create_json() for remote in self.remote_devices],
			"senceList": [scene.create_json() for scene in self.scenes]
		}
		config.write(path, data)

	def __set_config(self) -> None:
		try:
			if "API_Key" in self.__config:
				self.token = self.__config['API_Key'].get('token', "")
				self.secret = self.__config['API_Key'].get('secret', "")
				self.__client = Http_Client(self.token, self.secret)
			if "deviceList" in self.__config:
				self.devices = [Device(dev, self.__client) for dev in self.__config['deviceList']]
			if "infraredRemoteList" in self.__config:
				self.remote_devices = [Device.Remote_Device(remote, self.__client) for remote in self.__config['infraredRemoteList']]
			if "senceList" in self.__config:
				self.scenes = [Scene(scene, self.__client) for scene in self.__config['senceList']]
		except TypeError as e:
			print('Data not found')

	def get_device(self, devid: str) -> Device:
		# Implementation here
		pass

	def get_devices_from_server(self) -> None:
		# Implementation here
		pass

	def get_devices_from_config(self) -> dict:
		# Implementation here
		pass

	def check_status_code(self, code) -> bool:
		# Implementation here
		pass

	def get_remotes_from_config(self) -> dict:
		# Implementation here
		pass

	def get_remote(self, devid: str) -> Device.Remote_Device:
		# Implementation here
		pass

	def get_sense(self, devid: str) -> Scene:
		# Implementation here
		pass

	def get_scenes_from_server(self) -> None:
		# Implementation here
		pass

	def get_scenes_from_config(self) -> dict:
		# Implementation here
		pass

	def create_curtain_set_position(self, mode, position) -> dict:
		# Implementation here
		pass

	def create_set_mode(self, param) -> dict:
		# Implementation here
		pass

	def create_set_brightness(self, param) -> dict:
		# Implementation here
		pass

	def create_set_color(self, red, blue, green) -> dict:
		# Implementation here
		pass

	def create_set_color_temperature(self, param) -> dict:
		# Implementation here
		pass

	def create_pow_level(self, param) -> dict:
		# Implementation here
		pass

	def create_create_key(self, name, type, password, start_time, end_time) -> dict:
		# Implementation here
		pass

	def create_delete_key(self, param) -> dict:
		# Implementation here
		pass

	def create_blind_tilt_set_position(self, mode, position) -> dict:
		# Implementation here
		pass

	def create_air_conditioner_set_all(self, temp, mode, fanspd, power) -> dict:
		# Implementation here
		pass

	def create_set_channel(self, param) -> dict:
		# Implementation here
		pass