# AudioConvertPy

AudioConvertPy is a tool for converting M4A and MP4 files to MP3 format while preserving metadata such as album information, title, and artist.

## Installation

### Prerequisites

- Python 3.6 or later
- FFmpeg must be installed on your system

### Install with pip

#### Exists requirements.txt

```bash
pip install -r requirements.txt
```

#### New install
```bash
touch requirements.txt
pip install ffmpeg-python mutagen tk
```

## Building Executable for Windows

To create a standalone executable for Windows:

1. Install PyInstaller:

```bash
pip install pyinstaller
```

2. Navigate to your project directory and run:

```bash
pyinstaller --onefile your_script_name.py
```

Replace `your_script_name.py` with the name of your Python script. This will generate a single executable file in the `dist` directory.

## Usage

1. Run the application.
2. Select the folder containing your M4A/MP4 files.
3. Choose the destination folder for the MP3 files.
4. The application will convert all M4A/MP4 files in the selected folder to MP3 format, copying all metadata.

## プロジェクト名：AudioConvertPy

AudioConvertPyは、アルバム情報、タイトル、アーティストなどのメタデータを保持しながら、M4AおよびMP4ファイルをMP3形式に変換するツールです。

## インストール方法

### 前提条件

- Python 3.6以上
- システムにFFmpegがインストールされていること

### pipでのインストール

#### Exists requirements.txt

```bash
pip install -r requirements.txt
```

#### New install
```bash
touch requirements.txt
pip install ffmpeg-python mutagen tk
```

## Windows用実行ファイルのビルド

Windows用のスタンドアロン実行ファイルを作成するには：

1. PyInstallerをインストールします：

```bash
pip install pyinstaller
```

2. プロジェクトディレクトリに移動し、次を実行します：

```bash
pyinstaller --onefile your_script_name.py
```

`your_script_name.py`をPythonスクリプトの名前に置き換えてください。これにより、`dist`ディレクトリに単一の実行ファイルが生成されます。

## 使い方

1. アプリケーションを実行します。
2. M4A/MP4ファイルが含まれるフォルダを選択します。
3. MP3ファイルの保存先フォルダを選択します。
4. アプリケーションは、選択されたフォルダ内のすべてのM4A/MP4ファイルをMP3形式に変換し、すべてのメタデータをコピーします。
```

この`README

.md`はプロジェクトの目的、インストール方法、ビルド手順、および基本的な使用方法を英語と日本語で説明しています。プロジェクトの具体的な詳細や要件に応じて、このテンプレートを適宜調整してください。