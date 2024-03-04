import ffmpeg
import os
from tkinter import Tk, Button, filedialog, messagebox


class AudioConvertPy:
    def __init__(self, root):
        self.root = root
        self.root.title("AudioConvertPy")
        self.root.geometry("300x100")  # ウィンドウサイズの設定

        self.load_button = Button(root, text="Load Folder", command=self.load_folder)
        self.load_button.pack(pady=5)

        self.convert_button = Button(root, text="Convert", command=self.convert_files)
        self.convert_button.pack(pady=5)

        self.folder_path = ""
        self.output_folder = ""

    def load_folder(self):
        self.folder_path = filedialog.askdirectory(title="変換するファイルが含まれるフォルダを選択")
        self.output_folder = filedialog.askdirectory(title="MP3ファイルを保存するフォルダを選択")
        if self.folder_path and self.output_folder:
            messagebox.showinfo("Folder Loaded", "Folders have been loaded successfully.")

    def get_bitrate(self, input_path):
        try:
            # ファイルの情報を取得
            probe = ffmpeg.probe(input_path)
            # 最初のオーディオストリームのビットレートを取得
            audio_streams = [stream for stream in probe['streams'] if stream['codec_type'] == 'audio']
            if audio_streams:
                # ビットレートを返す (kbps単位)
                return int(audio_streams[0].get('bit_rate', '0')) // 1000
        except ffmpeg.Error as e:
            print(e.stderr)
            return 0

    def convert_file(self, input_path, output_path, bitrate):
        # ビットレートが取得できない場合はデフォルト値を使用
        audio_bitrate = f"{bitrate}k" if bitrate else "192k"
        ffmpeg.input(input_path).output(output_path, format='mp3', audio_bitrate=audio_bitrate).run()

    def convert_files(self):
        if self.folder_path and self.output_folder:
            for root, dirs, files in os.walk(self.folder_path):
                for file in files:
                    if file.endswith(('.m4a', '.mp4')):
                        input_path = os.path.join(root, file)
                        output_path = os.path.join(self.output_folder, os.path.splitext(file)[0] + '.mp3')
                        bitrate = self.get_bitrate(input_path)
                        self.convert_file(input_path, output_path, bitrate)
            messagebox.showinfo("Conversion Complete", "All files have been converted successfully.")
        else:
            messagebox.showwarning("No Folder Selected", "Please load a folder first.")


if __name__ == '__main__':
    root = Tk()
    app = AudioConvertPy(root)
    root.mainloop()
