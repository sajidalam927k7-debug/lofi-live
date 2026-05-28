import os
import subprocess
import random

# Configuration
YOUTUBE_URL = "rtmp://a.rtmp.youtube.com/live2"
STREAM_KEY = "PASTE_YOUR_STREAM_KEY_HERE"  # Apni copied YouTube Stream Key yahan daalein

songs = ["1.mp3", "2.mp3", "3.mp3", "4.mp3", "5.mp3"]
background_photo = "photo.jpg"

def start_lofi_stream():
    print("Sajid bhai, Lofi Live Stream shuru ho rahi hai... 😎🚀")
    
    while True:
        random.shuffle(songs)
        
        for song in songs:
            if os.path.exists(song) and os.path.exists(background_photo):
                print(f"Abhi chal raha hai: {song}")
                
                # FFmpeg command
                cmd = [
                    'ffmpeg', '-loop', '1', '-i', background_photo,
                    '-i', song,
                    '-filter_complex', '[0:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,boxblur=20:10[bg];[0:v]scale=-1:1080[fg];[bg][fg]overlay=(W-w)/2:0[v]',
                    '-map', '[v]', '-map', '1:a',
                    '-c:v', 'libx264', '-tune', 'stillimage', '-pix_fmt', 'yuv420p',
                    '-b:v', '3000k', '-g', '60',
                    '-c:a', 'aac', '-b:a', '128k', '-ar', '44100',
                    '-f', 'flv', f"{YOUTUBE_URL}/{STREAM_KEY}"
                ]
                
                subprocess.run(cmd)
            else:
                print("Koi file missing hai, check karo Sajid bhai!")
                break

if _name_ == "_main_":
    start_lofi_stream()
