import os
from pytube import Playlist
from pytube.exceptions import PytubeError

# Specify the URL of the YouTube playlist
playlist_url = "https://www.youtube.com/watch?v=nV7cI5zgOpk&list=PLA0M1Bcd0w8yv0XGiF1wjerjSZVSrYbjh&pp=iAQB"

# Create a Playlist object
playlist = Playlist(playlist_url)
playlist_name = playlist.title
playlist_name = playlist_name.replace(" ", "_").lower()

# Specify the directory where you want to save the videos
output_dir = os.path.join("videos", playlist_name)

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to handle retries for download
def download_with_retry(stream, output_path, retry_attempts=3):
    for attempt in range(retry_attempts):
        try:
            print(f"Downloading: {video.title}")
            stream.download(output_path=output_path)
            print("Download successful!")
            return True
        except Exception as e:
            print(f"An error occurred (Attempt {attempt + 1}/{retry_attempts}): {str(e)}")
    
    print("Download failed after all retry attempts.")
    return False

# Download each video with retry
for video in playlist.videos:
    # Get the highest resolution stream
    highest_resolution_stream = video.streams.get_highest_resolution()
    
    if highest_resolution_stream:
        download_with_retry(highest_resolution_stream, output_dir)

print("All downloads complete!")
