from pytube import YouTube
import os

# Specify the URL of the YouTube video
video_url = "https://www.youtube.com/watch?v=o0XbHvKxw7Y"

# Create a YouTube object
video = YouTube(video_url)

# Get the highest resolution stream
highest_resolution_stream = video.streams.get_highest_resolution()

# Specify the directory where you want to save the video
output_dir = "videos"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Download the video
print(f"Downloading: {video.title}")
highest_resolution_stream.download(output_path=output_dir)

print("Download complete!")