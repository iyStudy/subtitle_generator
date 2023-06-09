import os
import glob
import subprocess
import tkinter as tk
from tkinter import filedialog
import whisper
from datetime import timedelta
from srt import Subtitle, compose

def add_line(s):
    s_max_count = 30
    if len(s) >= s_max_count:
        if (len(s) - s_max_count) >= 15:
            return s[:s_max_count] + "\n" + s[s_max_count:]
    return s

def select_directory():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    return filedialog.askdirectory()  # Open the directory dialog

def create_subtitles(file_path, folder_path):
    name_without_extension = os.path.splitext(os.path.basename(file_path))[0]
    model = whisper.load_model("medium")
    result = model.transcribe(file_path)
    
    subs = [
        Subtitle(
            index=1,
            start=timedelta(seconds=data["start"]),
            end=timedelta(seconds=data["end"]),
            content=add_line(data["text"]),
            proprietary='',
        )
        for data in result["segments"]
    ]
    
    with open(os.path.join(folder_path, f"{name_without_extension}.srt"), mode="w", encoding="utf-8") as f:
        f.write(compose(subs))

def add_subtitles_to_video(video_file_path, output_directory):
    name_without_extension = os.path.splitext(os.path.basename(video_file_path))[0]
    subprocess.run(['ffmpeg', '-i', f'{output_directory}/{name_without_extension}.srt', f'{output_directory}/{name_without_extension}.ass'])
    subprocess.run(['ffmpeg', '-i', video_file_path, '-vf', f'ass={output_directory}/{name_without_extension}.ass', f'{output_directory}/{name_without_extension}_output.mp4'])

if __name__ == "__main__":
    folder_path = select_directory()

    video_files = glob.glob(os.path.join(folder_path, "*.mp4"))
    output_directory = "output"
    os.makedirs(output_directory, exist_ok=True)

    total_files = len(video_files)

    for i, video_file_path in enumerate(video_files):
        print(f"Processing file {i+1}/{total_files}: {os.path.basename(video_file_path)}")

        create_subtitles(video_file_path, output_directory)
        add_subtitles_to_video(video_file_path, output_directory)
