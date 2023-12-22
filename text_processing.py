"""
テキスト処理の関連機能を提供するモジュール
"""
class TextProcessing:
    @staticmethod
    def add_line(s):
        s_max_count = 30
        if len(s) >= s_max_count:
            if (len(s) - s_max_count) >= 15:
                return s[:s_max_count] + "\n" + s[s_max_count:]
        return s
