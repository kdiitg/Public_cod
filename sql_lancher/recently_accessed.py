import os
import datetime

def list_recently_accessed_files_and_dirs(base_path, hours=2, output_file="recently_accessed_files.txt"):
    # Get the current time and the time limit
    current_time = datetime.datetime.now()
    time_limit = current_time - datetime.timedelta(hours=hours)
    
    with open(output_file, 'w') as file:
        # Traverse the directory
        for root, dirs, files in os.walk(base_path):
            for name in dirs + files:
                full_path = os.path.join(root, name)
                try:
                    last_access_time = datetime.datetime.fromtimestamp(os.path.getatime(full_path))
                    if last_access_time > time_limit:
                        file.write(f"FullName: {full_path}, LastAccessTime: {last_access_time}\n")
                except FileNotFoundError:
                    # If the file was deleted during the run
                    continue

if __name__ == "__main__":
    # Change 'C:\\' to the path you want to search
    list_recently_accessed_files_and_dirs('F:\\Virtual', hours=2)
