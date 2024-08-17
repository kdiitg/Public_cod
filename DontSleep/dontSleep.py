import pyautogui
import time

# Set the interval (in seconds) for moving the mouse cursor
interval = 200
i= 1
while True:
    print(f'mouse-Moved {i+1}')
    pyautogui.moveRel(1, 1)  # Move the mouse cursor
    time.sleep(interval)  # Wait for the specified interval
    i += 1
