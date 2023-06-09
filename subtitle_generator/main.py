"""
メイン実行のファイル
"""

import glob
import os
from file_selector import FileSelector
from subtitle_creator import SubtitleCreator
from subtitle_adder import SubtitleAdder

if __name__ == "__main__":
    folder_path = FileSelector.select_directory()

    video_files = glob.glob(os.path.join(folder_path, "*.mp4"))
    output_directory = "output"
    os.makedirs(output_directory, exist_ok=True)

    total_files = len(video_files)

    for i, video_file_path in enumerate(video_files):
        print(f"Processing file {i+1}/{total_files}: {os.path.basename(video_file_path)}")

        SubtitleCreator.create_subtitles(video_file_path, output_directory)
        SubtitleAdder.add_subtitles_to_video(video_file_path, output_directory)
