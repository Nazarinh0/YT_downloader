import os
from pytube import Playlist
from moviepy.editor import AudioFileClip
import re
import unicodedata


# Specify the URL of the YouTube playlist
playlist_url = (
    "https://www.youtube.com/playlist?list=PLbCKwl6gVEfBcHaMFhA_rLzlZ9aS4uIir"
)

# Create a Playlist object
playlist = Playlist(playlist_url)
playlist_name = playlist.title
playlist_name = playlist_name.replace(" ", "_").lower()

# Specify the directory where you want to save the audio files
output_dir = os.path.join("audio", playlist_name)

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Download each video's audio and convert to MP3
for video in playlist.videos:
    # Get the audio stream
    audio_stream = video.streams.filter(only_audio=True).first()

    if audio_stream:
        print(f"Downloading audio: {video.title}")
        filename = f"{video.title.replace(' ', '_').lower()}.mp4"
        audio_path = os.path.join(output_dir, filename)
        audio_mp3_path = os.path.join(output_dir, f"{video.title}.mp3")
        
        #SKIP ALREADY EXISTING IF NEEDED - MAINLY FOR PLAYLIST UPDATE
        if os.path.exists(audio_mp3_path):
            print(f"Audio already exists: {video.title}")
            continue

        audio_stream.download(output_path=output_dir, filename=filename)

        # Convert the audio to MP3 using moviepy
        audio_clip = AudioFileClip(audio_path)
        audio_clip.write_audiofile(
            audio_mp3_path, codec="mp3", ffmpeg_params=["-ac", "2"]
        )

        # Clean up the temporary webm file
        audio_clip.close()
        os.remove(audio_path)

print("Download and conversion to MP3 complete!")
