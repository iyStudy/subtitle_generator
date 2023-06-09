"""
ビデオに字幕を追加する機能を提供するモジュール
assファイルを作成し、mp4ファイルに字幕を追加する
"""

import os
import subprocess
import glob
from file_selector import FileSelector

class SubtitleAdder:
    @staticmethod
    def add_subtitles_to_video(video_file_path, output_directory):
        name_without_extension = os.path.splitext(os.path.basename(video_file_path))[0]
        subprocess.run(['ffmpeg', '-i', f'{output_directory}/{name_without_extension}.srt', f'{output_directory}/{name_without_extension}.ass'])
        subprocess.run(['ffmpeg', '-i', video_file_path, '-vf', f'ass={output_directory}/{name_without_extension}.ass', f'{output_directory}/{name_without_extension}_output.mp4'])


    # assファイル作成済みでmp4を作成する
    def create_mp4(video_file_path, output_directory):
        name_without_extension = os.path.splitext(os.path.basename(video_file_path))[0]
        subprocess.run(['ffmpeg', '-i', video_file_path, '-vf', f'ass={output_directory}/{name_without_extension}.ass', f'{output_directory}/{name_without_extension}_output.mp4'])


    # 選択するのはinputフォルダ
    # assファイルを編集しただけの時に使用
    if __name__ == "__main__":

        folder_path = FileSelector.select_directory()

        video_files = glob.glob(os.path.join(folder_path, "*.mp4"))
        output_directory = "output"

        total_files = len(video_files)

        for i, video_file_path in enumerate(video_files):
            print(f"Processing file {i+1}/{total_files}: {os.path.basename(video_file_path)}")
            create_mp4(video_file_path, output_directory)
