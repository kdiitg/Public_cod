import subprocess
import os

def run_adb_command(command):
    """Run an adb command and return the output."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{command}': {e.stderr.strip()}")
        return None

def is_device_connected(devices_output):
    """Check if any devices are connected based on adb devices output."""
    lines = devices_output.splitlines()
    for line in lines:
        if 'device' in line and not line.startswith('List of devices attached'):
            return True
    return False

def take_screenshot():
    # Define file paths
    screenshot_path_device = "/sdcard/screenshot.png"
    screenshot_path_local = "screenshot.png"

    # Ensure ADB is connected
    print("Checking connected devices...")
    devices_output = run_adb_command("adb devices")

    # Check if any devices are connected
    if devices_output is None or not is_device_connected(devices_output):
        print("No devices detected. Ensure USB debugging is enabled and the device is connected.")
        print("use command ---->  adb connect device_serial_number         OR -----> adb connect ip:port ")
        return

    # Take screenshot on the device
    print("Taking screenshot...")
    result = run_adb_command(f"adb shell screencap -p {screenshot_path_device}")
    if result is None:
        print("Failed to take screenshot.")     # this may be case of upi pin / password of any app
        return

    # Pull screenshot to local machine
    print("Pulling screenshot to local machine...")
    result = run_adb_command(f"adb pull {screenshot_path_device} {screenshot_path_local}")
    if result is None:
        print("Failed to pull screenshot.")
        return

    # Optionally, remove the screenshot from the device
    print("Removing screenshot from device...")
    result = run_adb_command(f"adb shell rm {screenshot_path_device}")
    if result is None:
        print("Failed to remove screenshot from device.")

    # Print the current working directory
    print(f"Screenshot saved to {os.path.abspath(screenshot_path_local)}")

if __name__ == "__main__":
    take_screenshot()
