"""
 ファイルおよびディレクトリ選択に関連する機能を提供するモジュール
"""
import tkinter as tk
from tkinter import filedialog

class FileSelector:
    @staticmethod
    def select_directory():
        root = tk.Tk()
        root.withdraw()
        return filedialog.askdirectory()
