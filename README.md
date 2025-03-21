# Switchbot Library

A Python library for interacting with SwitchBot devices through the SwitchBot API.

## Overview

This library provides a simple interface to control SwitchBot devices and access their information using the official SwitchBot API. It allows you to:

- Retrieve device information from the SwitchBot API server
- Control various SwitchBot devices (Bots, Curtains, Lights, Air Conditioners, etc.)
- Execute scenes created in the SwitchBot app
- Save and load device configurations

## Prerequisites

- Python 3.6 or higher
- SwitchBot account
- SwitchBot API token and secret key (obtain from the SwitchBot app)

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/Switchbot_Library.git
cd Switchbot_Library

# Install the required dependencies
pip install requests
```

## Usage

There are two ways to use this library:

### 1. Direct API Access

```python
from switchbot_lib import Switchbot

# Initialize with your token and secret
switch_bot_token = 'your_token'
switch_bot_secret = 'your_secret'
switch = Switchbot.Switchbot(switch_bot_token, switch_bot_secret)

# Get device information from the server
switch.get_Scenes_from_Server()
switch.get_Devices_from_Server()

# Example: Turn on a ceiling light
print(switch.get_Remote("your_device_id").execute(switch.commands['Ceiling Light']['turnOn']))

# Example: Control an air conditioner
switch.get_Remote("your_device_id").execute(switch.Create_AirConditioner_setAll(22, 1, 1, "on"))

# Execute a scene
switch.get_Sense("your_scene_id").execute()

# Save configuration for later use
switch.Save_Config("dev.json")
```

### 2. Configuration-based Access

```python
from switchbot_lib import Switchbot

# Initialize from saved configuration
switch = Switchbot.Switchbot()
switch.Load_Config('dev.json')

# Control devices using the loaded configuration
print(switch.get_Remote("your_device_id").execute(switch.commands['Ceiling Light']['turnOn']))

# Display configuration information
switch.Show_Config()

# Get device status
print(switch.get_Device('your_device_id').get_Status())
```

## Supported Devices

The library supports various SwitchBot devices including:

- Bot
- Curtain
- Lock
- Humidifier
- Plug/Plug Mini
- Color Bulb
- Strip Light
- Robot Vacuum Cleaner
- Ceiling Light
- Keypad
- Blind Tilt
- Air Conditioner
- TV/IPTV/Streamer/Set Top Box
- DVD/Speaker
- Fan
- Light

## Device Commands

Each device type has specific commands. For example:

- Bot: turnOn, turnOff, Press
- Curtain: setPosition, turnOff, turnOn
- Air Conditioner: setAll (temperature, mode, fan speed, power)

See the `command.json` file for a complete list of available commands for each device type.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## References

- [SwitchBot API Documentation](https://github.com/OpenWonderLabs/SwitchBotAPI)
