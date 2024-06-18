# UAV Intercept and Control Script

This Python script allows you to intercept and control UAV (Unmanned Aerial Vehicle) traffic using the Scapy library and multithreading.

## Features

- **Interception**: Listens for UDP packets on port 5556 to identify and intercept UAV communication.
- **Command Injection**: Once a UAV is identified, the script can inject commands to control its behavior.
- **Commands Supported**: Emergency land and takeoff commands are supported based on intercepted UAV communication.

## Requirements

- Python 3.x
- Scapy library (`scapy`): Install using `pip install scapy`

## Usage

1. Ensure your wireless interface (`mon0` in this case) is set up for monitor mode.
2. Run the script using Python 3:
3. The script will start listening for UAV traffic.
4. Once a UAV is found, you can press ENTER to initiate an emergency landing command.

## Script Details

- **InterceptThread**: Extends `threading.Thread` to asynchronously sniff UDP packets on port 5556.
- **Command Injection**: Uses `sendp()` from Scapy to inject AT commands (`AT*COMWDG` and `AT*REF`) to control the UAV.
- **Error Handling**: Basic error handling is implemented to manage exceptions during packet interception.

Feel free to modify and extend the script based on your specific UAV communication protocols and requirements.
