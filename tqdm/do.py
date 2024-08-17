from pytube import YouTube
from tqdm import tqdm
import os

# URL of the YouTube video
url = "https://youtu.be/dOkWocFSgrk"
url  = "https://www.youtube.com/watch?v=dOkWocFSgrk"

# Create a YouTube object
yt = YouTube(url)

# Choose the highest resolution stream
stream = yt.streams.get_highest_resolution()

# Define a progress callback function
def progress_function(stream, chunk: bytes, bytes_remaining: int):
    total_size = stream.filesize
    progress_bar.update(total_size - bytes_remaining)

# Create a progress bar
total_size = stream.filesize
progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024, desc="Downloading")

# Register the progress callback function
yt.register_on_progress_callback(progress_function)

# Download the video
stream.download(output_path='.', filename='downloaded_video.mp4')

# Close the progress bar
progress_bar.close()

print("Download completed!")
