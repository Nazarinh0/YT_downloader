import os
import youtube_dl

# Specify the URL of the YouTube playlist
playlist_url = "https://youtube.com/playlist?list=PLbCKwl6gVEfBcHaMFhA_rLzlZ9aS4uIir"

# Setup output directory
output_dir = "downloaded_audios"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define youtube-dl options
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'quiet': False,
    'noplaylist': False
}

# Download and convert to mp3
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])

print("Download and conversion to MP3 complete!")