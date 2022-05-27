from audioop import add
from turtle import down
import youtube_dl
import shutil
import os

########################################################################################
# If not functioning run "pip install youtube_dl"
########################################################################################


# This Python script will download the mp3 files for the given youtube/soundcloud link
def downloadFromYoutube(song):

    video_url = song
    video_info = youtube_dl.YoutubeDL().extract_info(
        url=video_url, download=False
    )
    filename = f"{video_info['title']}.mp3"
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))
    return filename

# Funtion to relocate songs to spotify on your computer
def relocater(filenames, local_folder):
    for file in filenames:
        # absolute path       
        src_path = os.path.abspath(file)
        dst_path = '{0}/{1}'.format(os.path.abspath(local_folder_path), file)
        shutil.move(src_path, dst_path)


if __name__ == '__main__':
    local_folder_path = input('Enter the activated local spotify folder path \nIf unsure, watch https://www.youtube.com/watch?v=vxGMl0Zkeu0 : ')

    add_song = False
    downloaded_files = []
    while(not add_song):
        song_url = input('Enter the youtube/soundcloud URL of the song\n Enter (n) to kill program : ')
        if song_url == 'n':
            print('Terminating Progam')
            add_song = True
        else:
            downloaded_files.append(downloadFromYoutube(song_url))
            relocater(downloaded_files, local_folder_path)

