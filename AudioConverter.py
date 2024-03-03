import os
import ffmpeg
from mutagen.mp4 import MP4, MP4Cover
from mutagen.id3 import ID3, APIC, TIT2, TPE1, TALB, TRCK, TYER
from tkinter import Tk, filedialog

def convert_file(input_path, output_path):
    # M4A/MP4からMP3へ変換
    ffmpeg.input(input_path).output(output_path, format='mp3').run()

def copy_metadata(input_path, output_path):
    # 入力ファイルのメタデータを読み込む
    audio = MP4(input_path)
    mp3 = ID3()

    # タイトル、アーティスト、アルバムなどの情報をコピー
    if '\xa9nam' in audio:
        mp3.add(TIT2(encoding=3, text=audio['\xa9nam'][0]))
    if '\xa9ART' in audio:
        mp3.add(TPE1(encoding=3, text=audio['\xa9ART'][0]))
    if '\xa9alb' in audio:
        mp3.add(TALB(encoding=3, text=audio['\xa9alb'][0]))
    if 'trkn' in audio:
        mp3.add(TRCK(encoding=3, text=str(audio['trkn'][0][0])))
    if '\xa9day' in audio:
        mp3.add(TYER(encoding=3, text=audio['\xa9day'][0]))

    # アルバムアートをコピー
    if 'covr' in audio and len(audio['covr']) > 0:
        artwork = audio['covr'][0]
        mime = 'image/jpeg' if artwork.imageformat == MP4Cover.FORMAT_JPEG else 'image/png'
        mp3.add(APIC(encoding=3, mime=mime, type=3, desc='Cover', data=artwork))

    mp3.save(output_path)

def convert_folder(folder_path, output_folder):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(('.m4a', '.mp4')):
                input_path = os.path.join(root, file)
                output_path = os.path.join(output_folder, os.path.splitext(file)[0] + '.mp3')
                convert_file(input_path, output_path)
                copy_metadata(input_path, output_path)

if __name__ == '__main__':
    root = Tk()
    root.withdraw()  # GUIのメインウィンドウを表示しない
    folder_path = filedialog.askdirectory(title="変換するファイルが含まれるフォルダを選択")
    output_folder = filedialog.askdirectory(title="MP3ファイルを保存するフォルダを選択")
    convert_folder(folder_path, output_folder)
