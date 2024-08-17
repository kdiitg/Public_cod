import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import ctypes

def is_admin():
    """Check if the script is running with administrative privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    """Attempt to elevate privileges if not already running with admin rights."""
    if is_admin():
        return True
    else:
        # Request elevation
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        return False

def check_mysql_status():
    """Check MySQL service status."""
    try:
        result = subprocess.run(["sc", "query", "MySQL80"], capture_output=True, text=True, check=True)
        if "STATE" in result.stdout:
            state_line = next(line for line in result.stdout.splitlines() if "STATE" in line)
            return "RUNNING" in state_line
        else:
            return False
    except subprocess.CalledProcessError:
        return False

def start_mysql():
    """Start MySQL service."""
    if check_mysql_status():
        messagebox.showinfo("MySQL Service", "MySQL service is already running.")
    else:
        try:
            subprocess.run(["net", "start", "MySQL80"], check=True)
            messagebox.showinfo("MySQL Service", "MySQL service started successfully.")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("MySQL Service Error", f"Failed to start MySQL service: {e}")

def stop_mysql():
    """Stop MySQL service."""
    if not check_mysql_status():
        messagebox.showinfo("MySQL Service", "MySQL service is already stopped.")
    else:
        try:
            subprocess.run(["net", "stop", "MySQL80"], check=True)
            messagebox.showinfo("MySQL Service", "MySQL service stopped successfully.")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("MySQL Service Error", f"Failed to stop MySQL service: {e}")

def restart_mysql():
    """Restart MySQL service."""
    stop_mysql()
    start_mysql()

def main():
    """Create Tkinter GUI."""
    window = tk.Tk()
    window.title("MySQL Service Manager")

    def handle_start():
        start_mysql()

    def handle_stop():
        stop_mysql()

    def handle_restart():
        restart_mysql()

    tk.Button(window, text="Start MySQL", command=handle_start).pack(pady=10)
    tk.Button(window, text="Stop MySQL", command=handle_stop).pack(pady=10)
    tk.Button(window, text="Restart MySQL", command=handle_restart).pack(pady=10)
    tk.Button(window, text="Exit", command=window.quit).pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    if not run_as_admin():
        sys.exit()

    main()
