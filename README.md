### WiFi-Dictionary-Attack

```markdown
# Wi-Fi Dictionary Attack Script

A Python script designed for dictionary attacks on Wi-Fi networks. This tool uses the `pywifi` library to test multiple passwords against a target SSID, enabling security testing and educational exploration of Wi-Fi vulnerabilities.

---

## Features

- **Targeted Network Scanning**: Identifies Wi-Fi networks by SSID.
- **Password Dictionary Attack**: Tests passwords from a file against the target network.
- **Customizable Settings**: Specify the target SSID and password file.
- **Connection Feedback**: Provides real-time feedback on each password attempt.

---

## Requirements

- Python 3.6+
- `pywifi` library installed

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/wifi-dictionary-attack.git](https://github.com/SagarBiswas-MultiHAT/wifi-dictionary-attack.git
   cd wifi-dictionary-attack
   ```

2. Install the required library:
   ```bash
   pip install pywifi
   ```

---

## Usage

1. Create a password file (`passwords.txt`) with one password per line.

2. Update the script with your target SSID:
   ```python
   target_ssid = "Your_SSID_Here"
   ```

3. Run the script:
   ```bash
   python3 wifi_attack.py
   ```

4. Follow the output for connection results.

---

## Steps to Make It Work on Linux

To use this script on Linux, follow these additional steps:

1. **Install Required Packages**:
   Ensure `wpa_supplicant` is installed:
   ```bash
   sudo apt install wpasupplicant
   ```

2. **Run with Root Privileges**:
   Managing Wi-Fi networks requires root access. Run the script with `sudo`:
   ```bash
   sudo python3 wifi_attack.py
   ```

3. **Stop NetworkManager (Optional)**:
   If NetworkManager is interfering with `pywifi`, temporarily stop it:
   ```bash
   sudo systemctl stop NetworkManager
   ```

4. **Check Wireless Interface**:
   Ensure the script uses the correct Wi-Fi interface. Use the following command to identify your interface:
   ```bash
   iw dev
   ```
   Update the script if the interface is not detected.

5. **Verify pywifi Functionality**:
   Test that `pywifi` can access your Wi-Fi interface:
   ```bash
   python3 -c "import pywifi; print(pywifi.PyWiFi().interfaces())"
   ```

---

## Notes

- This script is intended for **educational purposes** and should only be used on networks you own or have permission to test.
- Improper usage of this tool may violate laws and ethical guidelines.

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```
