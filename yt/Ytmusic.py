from pytube import YouTube
import os

link=input("Link:")
directory=input("Directory:")
try:
    yt=YouTube(link)
except:
    print("Invalid Link")
    exit()

mp3=yt.streams.filter(only_audio=True).first()
print("Dowloading...")
output= mp3.download(directory)
base, ext=os.path.splitext(directory)
to_mp3= base + ".mp3"
os.rename(output, to_mp3)