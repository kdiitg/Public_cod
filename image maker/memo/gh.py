
import ctypes

y_address = 2443356635248
y_address = input("addrress of ")


y_content = ctypes.cast(y_address, ctypes.py_object).value

print(f"Content at memory address of y: {y_content}")

# Print the content at y's memory address
y_content_after_del = ctypes.cast(y_address, ctypes.py_object).value
print(f"Content at memory address of y after deleting x: {y_content_after_del}")
