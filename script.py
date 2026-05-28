import os
import random
import subprocess

# Live Stream Settings
YOUTUBE_URL = "rtmp://a.rtmp.youtube.com/live2"
STREAM_KEY = "YOUR_STREAM_KEY_HERE"  # Raat ko jab stream key milegi tab yahan daalenge

def start_lofi_stream():
    # Saare mp3 gaano ki list
    songs = ["1.mp3", "2.mp3", "3.mp3", "4.mp3", "5.mp3"]
    background_photo = "photo.jpg"
    
    print("Sajid bhai, Lofi Live Stream shuru ho rahi hai... 😎🚀")
    
    while True:
        # Gaano ko random order me chalane ke liye shuffle
        random.shuffle(songs)
        
        for song in songs:
            if os.path.exists(song) and os.path.exists(background_photo):
                print(f"Abhi chal raha hai: {song}")
                
                # FFmpeg command jo photo aur audio ko mix karke live stream karegi
                cmd = [
                    'ffmpeg', '-loop', '1', '-i', background_photo,
                    '-i', song, '-c:v', 'libx264', '-tune', 'stillimage',
                    '-pix_fmt', 'yuv420p', '-b:v', '4500k', '-g', '60',
                    '-c:a', 'aac', '-b:a', '128k', '-ar', '44100',
                    '-f', 'flv', f"{YOUTUBE_URL}/{STREAM_KEY}"
                ]
                
                # Command execute karna
                subprocess.run(cmd)
            else:
                print("Koi file missing hai, check karo Sajid bhai!")
                break

if _name_ == "_main_":
    start_lofi_stream()
