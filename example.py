from switchbot_lib import Switchbot

# https://github.com/OpenWonderLabs/SwitchBotAPI

#SwitchbotAPIサーバからデバイス情報等を取得しデバイスを操作する場合はxx行までのプログラムを参考にしてください。
#To obtain device information, etc. from the SwitchbotAPI server and operate devices, please refer to the program up to line 34.

#Switchbotのトークンキーとシークレットキーを発行して変数に格納してください。
#Issue a Switchbot token key and secret key and store them in variables.
switch_bot_token = 'key'
switch_bot_secret = 'key'
switch = Switchbot.Switchbot(switch_bot_token, switch_bot_secret)
#SwitchbotAPIからデバイス情報し変数に格納する。
#Stores device information from SwitchbotAPI into variables.
switch.get_Scenes_from_Server()
switch.get_Devices_from_Server()

#エアコンなどのデバイスを操作する場合の関数の一例です。
#This is an example of a function for operating a device such as an air conditioner.
print(switch.get_Remote("deviceid").execute(switch.commands['Ceiling Light']['turnOn']))
#コマンド実行例
#Command Execution Example
switch.RemoteDevices[0].execute(switch.commands['Bot']['turnOn'])
#コマンドを実行する
#Command Execution Example
switch.get_Remote("deviceid").execute(switch.Create_AirConditioner_setAll(22, 1, 1, "on"))
#Switchbotアプリのオートメーションに作成されている操作を実行する関数です。
#Function to perform an operation that is created in the automation of the Switchbot application.
switch.get_Sense("sceneId").execute()

#トークンやデバイス情報を指定のjsonファイルに格納する。
#Token and device information is stored in the specified json file.
switch.Save_Config("dev.json")

############################################################################################

#コンフィグからデバイス情報等を取得し操作する場合はxx行目までのプログラムを参考にしてください。
#To obtain and operate device information, etc., from the configuration, refer to the program up to line 58.
switch = Switchbot.Switchbot()
switch.Load_Config('dev.json')

#端末を操作する場合はdeviceidを引数にして実行してください。
#To operate a terminal, execute with the deviceid as an argument.
print(switch.get_Remote("deviceid").execute(switch.commands['Ceiling Light']['turnOn']))

#エアコンなどの一部の端末を操作する用の関数を用意しています。Switchbot.pyを参照してください。
#Functions for operating some terminals, such as air conditioners, are provided; see Switchbot.py.
switch.get_Remote().execute(switch.Create_AirConditioner_setAll(22, 1, 1, "on"))

#コンフィグ(dev.json)に格納されている情報を表示します。
#Displays information stored in the configuration (dev.json).
switch.Show_Config()

#Switchbot社から販売されているデバイスをDeviceに格納されます。
#Devices sold by Switchbot are stored in Device.

#デバイスのステータス情報を取得します。
#Obtain device status information.
print(switch.get_Device('deviceid').get_Status())