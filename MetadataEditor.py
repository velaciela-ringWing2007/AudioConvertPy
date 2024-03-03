import os
from tkinter import Tk, Label, Entry, Button, filedialog
from mutagen.easyid3 import EasyID3


class MetadataEditor:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x600")  # ウィンドウサイズを調整
        self.root.title("MP3 Metadata Editor")

        # ファイル選択ボタン
        self.load_button = Button(root, text="Load MP3", command=self.load_file)
        self.load_button.pack(pady=10)

        # 各種メタデータのラベルとエントリーフィールド
        self.metadata_fields = ['title', 'artist', 'album', 'tracknumber', 'genre', 'date']
        self.entries = {}
        for field in self.metadata_fields:
            label = Label(root, text=field.capitalize() + ":")
            label.pack(pady=(5, 0))
            entry = Entry(root)
            entry.pack(pady=(0, 5))
            self.entries[field] = entry

        # 保存ボタン
        self.save_button = Button(root, text="Save Metadata", command=self.save_metadata)
        self.save_button.pack(pady=10)

        self.file_path = None

    def load_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if self.file_path:
            audio = EasyID3(self.file_path)
            for field in self.metadata_fields:
                self.entries[field].delete(0, 'end')
                self.entries[field].insert(0, audio.get(field, [''])[0])

    def save_metadata(self):
        if self.file_path:
            audio = EasyID3(self.file_path)
            for field, entry in self.entries.items():
                audio[field] = entry.get()
            audio.save()
            print("Metadata saved.")


if __name__ == "__main__":
    root = Tk()
    app = MetadataEditor(root)
    root.geometry("600x400")  # ウィンドウのサイズを600x400に設定
    root.mainloop()
