# subtitle_generator

このプロジェクトは、ビデオファイルに自動的に字幕を生成し追加するPythonスクリプトです。

## 概要

このプロジェクトは、字幕の生成と追加のプロセスをそれぞれ取り扱ういくつかのPythonファイルで構成されています。

- `file_selector.py`: ファイルおよびディレクトリ選択に関連する機能を提供するモジュールです。
- `main.py`: メインの実行ファイルです。ディレクトリを選択し、その中のMP4ファイルをイテレーション処理し、各ビデオに対して字幕を生成し、ビデオに字幕を追加します。
- `subtitle_adder.py`: ビデオに字幕を追加する機能を提供するモジュールです。ASSファイルを作成し、MP4ファイルに字幕を追加します。
- `subtitle_creator.py`: 字幕の作成に関連する機能を提供するモジュールです。SRTファイルを作成します。
- `text_processing.py`: テキスト処理の関連機能を提供するモジュールです。例えば、長すぎる行を複数の行に分割します。

## 使い方

1.Google Colabolatory上でSubTitle_Gneerator.ipynbを実行


## 注意

これは個人プロジェクトであり、すべてのユースケースに適しているわけではありません。必要に応じてコードを変更してお使いください。
