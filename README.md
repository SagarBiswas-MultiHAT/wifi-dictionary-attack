# Wi-Fi Dictionary Attack Script

![Wi-Fi Dictionary Attack Script.](https://imgur.com/sEFTBgT.png)

This Python script is designed to perform a dictionary attack on a Wi-Fi network using the `pywifi` library. It scans available Wi-Fi networks, targets a specific SSID, and attempts to connect using passwords from a given file. Ideal for educational purposes and security testing.

## Features
- Scans available Wi-Fi networks.
- Targets a specific SSID.
- Loads a dictionary of passwords from a file.
- Attempts to connect to the target Wi-Fi network.
- Displays successful connections or failed attempts.

## Requirements
- Python 3.6 or higher
- `pywifi` library

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/SagarBiswas-MultiHAT/wifi-dictionary-attack.git](https://github.com/SagarBiswas-MultiHAT/wifi-dictionary-attack.git
   cd wifi-dictionary-attack
   ```

2. Install the required library:
   ```bash
   pip install pywifi
   ```

## Usage
1. Create a file named `passwords.txt` in the same directory as the script. Add potential passwords, one per line.
2. Update the `target_ssid` variable in the script with the SSID of your target Wi-Fi network.
3. Run the script:
   ```bash
   python3 wifi_dictionary_attack.py
   ```

## Steps to Make It Work on Kali Linux

### 1. Install Required Tools
Ensure `wpa_supplicant` is installed:
```bash
sudo apt install wpasupplicant
```

### 2. Run the Script as Root
Managing Wi-Fi on Linux requires root privileges. Run the script with `sudo`:
```bash
sudo python3 wifi_dictionary_attack.py
```

### 3. Identify Your Wi-Fi Interface
The script assumes the first Wi-Fi interface is being used. On Linux, this might not always be correct. Check your Wi-Fi interfaces with:
```bash
iw dev
```
Replace the interface name in the script if necessary.

### 4. Stop NetworkManager (if needed)
The `NetworkManager` service can interfere with the script. Stop it temporarily:
```bash
sudo systemctl stop NetworkManager
```
After the attack, restart it:
```bash
sudo systemctl start NetworkManager
```

### 5. Verify `pywifi` Functionality
Ensure `pywifi` detects your Wi-Fi interface:
```bash
python3 -c "import pywifi; print(pywifi.PyWiFi().interfaces())"
```
If no interfaces are listed, troubleshoot your Wi-Fi driver or dependencies.

## Notes
- **For Educational Purposes Only**: This script is intended for ethical hacking and security testing. Do not use it on networks you do not own or have permission to test.
- Ensure your system has proper drivers and permissions to manage Wi-Fi connections.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Disclaimer
The author is not responsible for any misuse of this script. Use responsibly and ethically.
