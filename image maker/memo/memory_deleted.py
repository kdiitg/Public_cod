import ctypes
import time

variable1 = "Hello from process 1"
address1 = id(variable1)

print(f"Memory address of variable: {address1}")
time.sleep(2)  # Keep the process alive for a wh


del variable1

try:
    print(variable1)
except Exception:
    print("Variable no longer exists.")
    pass

addressx = int(input("Enter memory address: "))


try:
    content2 = ctypes.cast(addressx, ctypes.py_object).value
    print(f"Content at memory address: {content2}")
except ValueError:
    print("Could not access memory address.")
except Exception as e:
    print(f"An error occurred: {e}")


