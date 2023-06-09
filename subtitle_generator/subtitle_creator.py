"""
字幕の作成に関連する機能を提供するモジュール
srtファイルを作成
"""
import os
from datetime import timedelta
from srt import Subtitle, compose
import whisper
from text_processing import TextProcessing

class SubtitleCreator:
    @staticmethod
    def create_subtitles(file_path, folder_path):
        name_without_extension = os.path.splitext(os.path.basename(file_path))[0]
        model = whisper.load_model("medium")
        result = model.transcribe(file_path)
        
        subs = [
            Subtitle(
                index=1,
                start=timedelta(seconds=data["start"]),
                end=timedelta(seconds=data["end"]),
                content=TextProcessing.add_line(data["text"]),
                proprietary='',
            )
            for data in result["segments"]
        ]
        
        with open(os.path.join(folder_path, f"{name_without_extension}.srt"), mode="w", encoding="utf-8") as f:
            f.write(compose(subs))
