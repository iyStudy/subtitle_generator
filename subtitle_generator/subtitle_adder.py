import os
import subprocess
import glob
from file_selector import FileSelector

"""
ビデオに字幕を追加する機能を提供するモジュール
assファイルを作成し、mp4ファイルに字幕を追加する
"""
class SubtitleAdder:

    @staticmethod
    def customize_ass_style(ass_file_path):
        youtube_style = """
    [V4+ Styles]
    Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
    Style: Default,Arial,16,&Hffffff,&Hffffff,&H000000,&H80000000,-1,0,0,0,100,100,0,0,1,2,2,2,10,10,10,0
    """

        with open(ass_file_path, 'r', encoding='utf-8') as file:
            content = file.readlines()

        with open(ass_file_path, 'w', encoding='utf-8') as file:
            styles_section_found = False
            for line in content:
                if '[V4+ Styles]' in line:
                    file.write(youtube_style)
                    styles_section_found = True
                elif styles_section_found and 'Style:' in line:
                    continue  # Skip original styles
                else:
                    file.write(line)


    @staticmethod
    def add_subtitles_to_video(video_file_path, output_directory):
        name_without_extension = os.path.splitext(os.path.basename(video_file_path))[0]
        srt_file_path = f'{output_directory}/{name_without_extension}.srt'
        ass_file_path = f'{output_directory}/{name_without_extension}.ass'

        # SRTからASSに変換
        subprocess.run(['ffmpeg', '-i', srt_file_path, ass_file_path])

        # ASSファイルのスタイルをカスタマイズ
        SubtitleAdder.customize_ass_style(ass_file_path)

        # 動画に字幕を追加
        subprocess.run(['ffmpeg', '-i', video_file_path, '-vf', f'ass={ass_file_path}', f'{output_directory}/{name_without_extension}_output.mp4'])

    @staticmethod
    def create_mp4(video_file_path, output_directory):
        name_without_extension = os.path.splitext(os.path.basename(video_file_path))[0]
        ass_file_path = f'{output_directory}/{name_without_extension}.ass'

        # ASSファイルのスタイルをカスタマイズ
        SubtitleAdder.customize_ass_style(ass_file_path)

        # 動画に字幕を追加
        subprocess.run(['ffmpeg', '-i', video_file_path, '-vf', f'ass={ass_file_path}', f'{output_directory}/{name_without_extension}_output.mp4'])



# 選択するのはinputフォルダ
# assファイルを編集しただけの時に使用
if __name__ == "__main__":
    folder_path = FileSelector.select_directory()
    video_files = glob.glob(os.path.join(folder_path, "*.mp4"))
    output_directory = "output"
    total_files = len(video_files)

    for i, video_file_path in enumerate(video_files):
        print(f"Processing file {i+1}/{total_files}: {os.path.basename(video_file_path)}")
        SubtitleAdder.add_subtitles_to_video(video_file_path, output_directory)
