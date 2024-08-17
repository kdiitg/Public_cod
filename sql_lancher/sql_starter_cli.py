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
        print("MySQL service is already running.")
    else:
        try:
            subprocess.run(["net", "start", "MySQL80"], check=True)
            print("MySQL service started successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to start MySQL service: {e}")

def stop_mysql():
    """Stop MySQL service."""
    if not check_mysql_status():
        print("MySQL service is already stopped.")
    else:
        try:
            subprocess.run(["net", "stop", "MySQL80"], check=True)
            print("MySQL service stopped successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to stop MySQL service: {e}")

def restart_mysql():
    """Restart MySQL service."""
    stop_mysql()
    start_mysql()

def main():
    """Main function to display menu and handle user input."""
    while True:
        subprocess.run("cls", shell=True)
        print("\nMySQL Service Manager\n=====================\n")
        print("1. Start MySQL")
        print("2. Stop MySQL")
        print("3. Restart MySQL")
        print("4. Exit\n")
        
        try:
            if not choice:
                choice = input("Enter your choice (1-4): ")
        except:
            choice = input("Enter your choice (1-4): ")
        
        if choice.strip() == "1":
            start_mysql()
        elif choice.strip() == "2":
            stop_mysql()
        elif choice.strip() == "3":
            restart_mysql()
        elif choice.strip() == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
        # input("\nPress Enter to for Main Menu")
        choice = input("\nEnter your choice (1-4): ")

if __name__ == "__main__":
    if not run_as_admin():
        sys.exit()

    main()
