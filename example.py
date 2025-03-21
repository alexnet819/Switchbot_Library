from switchbot_lib import Switchbot

# https://github.com/OpenWonderLabs/SwitchBotAPI

# To obtain device information, etc. from the SwitchbotAPI server and operate devices, please refer to the program up to line 34.

# Issue a Switchbot token key and secret key and store them in variables.
switch_bot_token = 'token'
switch_bot_secret = 'secret'
switch = Switchbot.Switchbot(switch_bot_token, switch_bot_secret)
# Stores device information from SwitchbotAPI into variables.
switch.get_Scenes_from_Server()
switch.get_Devices_from_Server()

# This is an example of a function for operating a device such as an air conditioner.
print(switch.get_Remote("deviceid").execute(switch.commands['Ceiling Light']['turnOn']))
# Command Execution Example
switch.RemoteDevices[0].execute(switch.commands['Bot']['turnOn'])
# Command Execution Example
switch.get_Remote("deviceid").execute(switch.Create_AirConditioner_setAll(22, 1, 1, "on"))
# Function to perform an operation that is created in the automation of the Switchbot application.
switch.get_Sense("sceneId").execute()

# Token and device information is stored in the specified json file.
switch.Save_Config("dev.json")

############################################################################################

# To obtain and operate device information, etc., from the configuration, refer to the program up to line 58.
switch = Switchbot.Switchbot()
switch.Load_Config('dev.json')

# To operate a terminal, execute with the deviceid as an argument.
print(switch.get_Remote("deviceid").execute(switch.commands['Ceiling Light']['turnOn']))

# Functions for operating some terminals, such as air conditioners, are provided; see Switchbot.py.
switch.get_Remote().execute(switch.Create_AirConditioner_setAll(22, 1, 1, "on"))

# Displays information stored in the configuration (dev.json).
switch.Show_Config()

# Devices sold by Switchbot are stored in Device.

# Obtain device status information.
print(switch.get_Device('deviceid').get_Status())