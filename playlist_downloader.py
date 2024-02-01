import os
from pytube import Playlist
from pytube.exceptions import PytubeError
from tqdm import tqdm

# Specify the URL of the YouTube playlist
playlist_url = (
    "https://www.youtube.com/playlist?list=PLbCKwl6gVEfBcHaMFhA_rLzlZ9aS4uIir"
)

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
            # stream.download(output_path=output_path, on_progress_callback=on_progress)
            stream.download(output_path=output_path)
            print("Download successful!")
            return True
        except Exception as e:
            print(
                f"An error occurred (Attempt {attempt + 1}/{retry_attempts}): {str(e)}"
            )

    print("Download failed after all retry attempts.")
    return False


# Function to update the progress bar
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    progress = bytes_downloaded / total_size * 100
    pbar.update(progress - pbar.n)


# Download each video with retry
for video in playlist.videos:
    # Get the highest resolution stream
    highest_resolution_stream = video.streams.get_highest_resolution()

    if highest_resolution_stream:
        # Initialize the progress bar
        pbar = tqdm(
            total=100, desc=f"Downloading {video.title}", unit="%", unit_scale=True
        )
        download_with_retry(highest_resolution_stream, output_dir)
        pbar.close()

print("All downloads complete!")
