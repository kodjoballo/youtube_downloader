# python program where the user will be insert an url and the save_path of youtube video to be downloaded with the
#highest resolution possible
from ctypes.macholib.dyld import dyld_library_path

# we will install the module pytube

from pytube import YouTube
import tkinter as tk
from tkinter   import filedialog # to have the directory dialog
import yt_dlp

def download_video(url, save_path):
    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    except Exception as e:
        print(e)



def open_file_dialog():
    root = tk.Tk()
    root.withdraw()
    root.update()
    folder = filedialog.askdirectory()
    root.destroy()
    if folder:
        print(f"selected folder: {folder}")

    return folder


if __name__ == "__main__":

    #root = tk.Tk()  # creating object using TK, it's like a window, but it doesn't have to be shown
    #root.withdraw()  # to hide the video
    #root.update()



    video_url = input("Please enter a Youtube url: ")
    save_dir = open_file_dialog()

    if  save_dir:
        print("Started download....")
        print("URL entered:", video_url)
        print("Save path selected:", save_dir)
        download_video(video_url, save_dir)
        print("\nVideo downloaded successfully")
    else:

       print("Invalid location")




