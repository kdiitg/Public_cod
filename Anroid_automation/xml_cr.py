import subprocess
import tkinter as tk
from tkinter import filedialog
import os

def run_adb_command(command):
    """ Run a command using subprocess and return the output """
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout, result.stderr

def dump_ui_hierarchy():
    """ Run adb command to dump UI hierarchy """
    print("Running ADB command to dump UI hierarchy...")
    stdout, stderr = run_adb_command('adb shell uiautomator dump /sdcard/ui_dump.xml')
    if stderr:
        print(f"Error running adb command: {stderr}")
    else:
        print("UI hierarchy dumped successfully.")

def pull_xml_file(destination_path):
    """ Pull the XML file from mobile device to PC """
    print(f"Pulling XML file to {destination_path}...")
    stdout, stderr = run_adb_command(f'adb pull /sdcard/ui_dump.xml "{destination_path}"')
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
    # Step 1: Dump the UI hierarchy
    dump_ui_hierarchy()
    
    # Step 2: Open a save file dialog to get the destination path
    destination_path = save_file_dialog()
    
    if destination_path:
        # Step 3: Pull the XML file from the device
        pull_xml_file(destination_path)
    else:
        print("No file path selected. Exiting.")

if __name__ == "__main__":
    main()
