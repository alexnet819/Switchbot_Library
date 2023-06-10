from switchbot_lib import Http_Client
import json

class Device:
    def __init__(self, data:json = None, client: Http_Client = None) -> None:
        self.http_client = client
        self.deviceid = data['deviceId']
        self.devicename = data['deviceName']
        self.devicetype = data['deviceType']
        #elf.enablecloudservice = dev_info['hubDeviceId']
        self.hubdeviceid =  data['hubDeviceId']
        #self.is_virtual = False
        #self.status = ""

    def execute(self, command:json) -> json:
        res = self.http_client.send("POST", f"devices/{self.deviceid}/commands", command)
        return res
    def get_Status(self) -> json:
        res = self.http_client.send("GET", f"devices/{self.deviceid}/status")
        return res["body"]
    
    def Create_Json(self) -> str:
        _json=f'{{"deviceId": "{self.deviceid}", "deviceName": "{self.devicename}", "deviceType": "{self.devicetype}", "hubDeviceId": "{self.hubdeviceid}"}}'
        return _json
    def get_DeviceID(self) -> str:
        return self.deviceid
    def get_DeviceName(self) -> str:
        return self.devicename
    def get_DeviceType(self) -> str:
        return self.devicetype
    def get_HubDeviceID(self) -> str:
        return self.hubdeviceid

    
    def set_DeviceID(self, value: str):
        self.deviceid = value
    def set_DeviceName(self, value: str):
        self.devicename = value
    def set_DeviceType(self, value: str):
        self.devicetype = value
    def set_HubDeviceID(self, value: str):
        self.hubdeviceid = value


class BlindTilt(Device):
    def __init__(self, data:json = None, client: Http_Client = None):
        super.__init__(data, client)
        self.blindTiltDevicesIds = data['blindTiltDevicesIds']
        self.calibrate = data['calibrate']
        self.group = data['group']
        self.master = data['master']
        self.direction = data['direction']
        self.slidePosition = data['slidePosition']


class Remote_Device:
    def __init__(self, data:json = None, client: Http_Client = None):
        self.http_client = client
        self.deviceid = ""
        self.devicename = ""
        self.remotetype = ""
        self.hubdeviceid = ""
        if data != None:
            self.deviceid = data['deviceId']
            self.devicename = data['deviceName']
            self.remotetype = data['remoteType']
            self.hubdeviceid = data['hubDeviceId']
    
    def get_Status(self) -> json:
        res = self.http_client.send("GET", f"devices/{self.deviceid}/status")
        return res["body"]
    def execute(self, command:json) -> json:
        res = self.http_client.send("POST", f"devices/{self.deviceid}/commands", command)
        return res
    def Create_Json(self) -> str:
        _json=f'{{"deviceId": "{self.deviceid}", "deviceName": "{self.devicename}", "remoteType": "{self.remotetype}", "hubDeviceId": "{self.hubdeviceid}"}}'
        return _json    


    def get_DeviceID(self) -> str:
        return self.deviceid
    def get_DeviceName(self) -> str:
        return self.devicename
    def get_RemoteType(self) -> str:
        return self.remotetype
    def get_HubDeviceID(self) -> str:
        return self.hubdeviceid
    
    def set_DeviceID(self, value: str):
        self.deviceid = value
    def set_DeviceName(self, value: str):
        self.devicename = value
    def set_RemoteType(self, value: str):
        self.remotetype = value
    def set_EnableCloudService(self, value: str):
        self.enablecloudservice = value
    def set_HubDeviceID(self, value: str):
        self.hubdeviceid = value

