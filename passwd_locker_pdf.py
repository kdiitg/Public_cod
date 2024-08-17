import os
import time
import PyPDF2
import tkinter as tk
from tkinter import filedialog

def encrypt_pdf(input_path, output_path, password):
    with open(input_path, 'rb') as input_file:
        reader = PyPDF2.PdfReader(input_file)
        
        # Check if the PDF is encrypted, and decrypt it if necessary
        if reader.is_encrypted:
            reader.decrypt(password)

        writer = PyPDF2.PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        writer.encrypt(password)
        
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

def rotate_encryption_keys(input_file, output_dir, password, rotation_interval):
    while True:
        # Generate a new encryption key
        import random

        new_password = random.randint(321000, 874000)
        new_password = str(new_password)
        # new_password = generate_new_password()

        # Encrypt the input PDF file with the new key
        input_filename = os.path.basename(input_file)
        output_path = os.path.join(output_dir, input_filename)
        encrypt_pdf(input_file, output_path, new_password)
        print(f"{input_filename} encrypted with new key {new_password}")

        # Wait for the rotation interval before rotating keys again
        time.sleep(rotation_interval)

def generate_new_password():
    # Implement your logic to generate a new encryption key/password here
    # Example: Generate a random password
    import secrets
    return secrets.token_urlsafe(16)

def browse_input_file():
    input_file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    input_file_entry.delete(0, tk.END)
    input_file_entry.insert(0, input_file)

def browse_output_directory():
    output_directory = filedialog.askdirectory()
    output_dir_entry.delete(0, tk.END)
    output_dir_entry.insert(0, output_directory)

if __name__ == "__main__":
    # Create Tkinter window
    root = tk.Tk()
    root.title("PDF Encryption Key Rotation")

    # Frame for the input file
    input_frame = tk.Frame(root)
    input_frame.pack(pady=10)

    tk.Label(input_frame, text="Input File:").pack(side=tk.LEFT)
    input_file_entry = tk.Entry(input_frame, width=50)
    input_file_entry.pack(side=tk.LEFT, padx=10)
    tk.Button(input_frame, text="Browse", command=browse_input_file).pack(side=tk.LEFT)

    # Frame for the output directory
    output_frame = tk.Frame(root)
    output_frame.pack(pady=10)

    tk.Label(output_frame, text="Output Directory:").pack(side=tk.LEFT)
    output_dir_entry = tk.Entry(output_frame, width=50)
    output_dir_entry.pack(side=tk.LEFT, padx=10)
    tk.Button(output_frame, text="Browse", command=browse_output_directory).pack(side=tk.LEFT)

    input_file = ""
    output_dir = ""

    def start_rotation():
        global input_file, output_dir
        input_file = input_file_entry.get()
        output_dir = output_dir_entry.get()
        password = "75tp@27_p3"
        rotation_interval = 100  # Rotate keys every hour
        rotate_encryption_keys(input_file, output_dir, password, rotation_interval)

    # Button to start rotation
    start_button = tk.Button(root, text="Start Rotation", command=start_rotation)
    start_button.pack(pady=10)

    root.mainloop()
