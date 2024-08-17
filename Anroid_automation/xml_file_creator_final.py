"""
This file create a xml file in android. and that file is copied from mobile to pc at ur desired location.
this xml file used for  automation purpose. Using this script we can find attributes like text, className, bounds etc.

<node index="4" text="Check Balance" resource-id="net.one97.paytm:id/tv_button_text" class="android.widget.TextView" package="net.one97.paytm" content-desc="" checkable="false" checked="false" clickable="true"  selected="false" bounds="[717,1143][1035,1208]" /></node>

"""




import subprocess
import tkinter as tk
from tkinter import simpledialog, filedialog

def run_adb_command(command):
    """ Run a command using subprocess and return the output """
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout, result.stderr

def list_connected_devices():
    """ List connected devices """
    stdout, stderr = run_adb_command('adb devices')
    if stderr:
        print(f"Error listing devices: {stderr}")
    else:
        print("Connected devices:")
        print(stdout)
        # Parse the list of devices
        devices = [line.split()[0] for line in stdout.splitlines() if line and not line.startswith("List of devices")]
        return devices

def get_preferred_device(devices):
    """ Prefer Wi-Fi device if available, otherwise return the first device """
    wifi_device = None
    for device in devices:
        # Check if the device is connected via Wi-Fi
        stdout, _ = run_adb_command(f'adb -s {device} shell getprop dev.bootcomplete')
        if "1" in stdout:
            wifi_device = device
            break
    
    if wifi_device:
        print(f"Preferred Wi-Fi device: {wifi_device}")
        return wifi_device
    elif devices:
        print(f"Using first available device: {devices[0]}")
        return devices[0]
    else:
        print("No devices found.")
        return None

def connect_device_ip(ip_address):
    """ Connect to a device using the provided IP address """
    print(f"Connecting to device at {ip_address}...")
    stdout, stderr = run_adb_command(f'adb connect {ip_address}')
    if stderr:
        print(f"Error connecting to device: {stderr}")
    else:
        print(f"Connected to {ip_address}")

def dump_ui_hierarchy(device_id):
    """ Run adb command to dump UI hierarchy for a specific device """
    print("Running ADB command to dump UI hierarchy...")
    stdout, stderr = run_adb_command(f'adb -s {device_id} shell uiautomator dump /sdcard/ui_dump.xml')
    if stderr:
        print(f"Error running adb command: {stderr}")
    else:
        print("UI hierarchy dumped successfully.")

def pull_xml_file(device_id, destination_path):
    """ Pull the XML file from mobile device to PC """
    print(f"Pulling XML file to {destination_path}...")
    stdout, stderr = run_adb_command(f'adb -s {device_id} pull /sdcard/ui_dump.xml "{destination_path}"')
    if stderr:
        print(f"Error pulling file: {stderr}")
    else:
        print("File pulled successfully.")

def save_file_dialog():
    """ Open a file dialog to select the save location """
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.asksaveasfilename(defaultextension=".xml",
                                           filetypes=[("XML files", "*.xml")],
                                           title="Save XML file as")
    return file_path

def main():
    # Step 1: List connected devices
    devices = list_connected_devices()
    
    if not devices:
        print("No devices found.")
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        
        # Ask for the IP address of the device to connect to
        ip_address = simpledialog.askstring("Device IP", "Enter the IP address of the device (default port 5555):", initialvalue="192.168.1.3:5555")
        
        if ip_address:
            # Connect to the specified device via Wi-Fi
            connect_device_ip(ip_address)
            
            # List devices again after connecting
            devices = list_connected_devices()
            
            if not devices:
                print("Failed to connect to any device.")
                return
    
    # Step 2: Select a preferred device
    device_id = get_preferred_device(devices)
    
    if not device_id:
        return
    
    # Step 3: Dump the UI hierarchy
    dump_ui_hierarchy(device_id)
    
    # Step 4: Open a save file dialog to get the destination path
    destination_path = save_file_dialog()
    
    if destination_path:
        # Step 5: Pull the XML file from the device
        pull_xml_file(device_id, destination_path)
    else:
        print("No file path selected. Exiting.")

if __name__ == "__main__":
    main()
