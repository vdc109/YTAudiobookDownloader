from pytube import YouTube
import os
from moviepy.editor import *

url = input("URL for video: ")
yt = YouTube(url)

t = yt.streams.all()
out_file = t[0].download()

print (out_file)

mp4_file = out_file

mp3_file = out_file[:-5] + '.mp3'

video = VideoFileClip(mp4_file)

audio = video.audio

audio.write_audiofile(mp3_file)

audio.close()

video.close()