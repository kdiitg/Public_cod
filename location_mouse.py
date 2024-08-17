# this will give the location of mouse pointer

import pyautogui

try:
    while True:
        # Get and print the current mouse cursor position
        a =int(input('Press 1 know the value'))
        if a ==1:
            current_position = pyautogui.position()
            print("Current Mouse Cursor Position:", current_position)
            
            # Add a small delay to avoid consuming too much CPU
            pyautogui.sleep(1)
        else:
            raise KeyboardInterrupt
except KeyboardInterrupt:
    print("\nScript terminated by user.")
